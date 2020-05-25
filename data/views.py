from django.shortcuts import render, redirect, get_object_or_404
from .models import Mainbar, Category, Product, Sorter, FirstCategory, SecondCategory, ProductFilter
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template.context_processors import csrf
from .forms import EmailPostForm
from django.core.mail import send_mail



def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Product, id=post_id)
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.name)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.name, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'ugeopolimer@gmail.com',[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})




def shop(request):
    response = {}
    response.update(csrf(request))
    response['bar'] = Mainbar.objects.all()
    response['mobar'] = Mainbar.objects.filter(mobile=True)
    return render(request, 'index.html', response)

def test(request):
    response = {}
    response.update(csrf(request))
    response['bar'] = Mainbar.objects.all()
    response['mobar'] = Mainbar.objects.filter(mobile=True)
    return render(request, 'test.html', response)

def product_list(request, category_slug=None):
    bar= Mainbar.objects.all()
    mobar = Mainbar.objects.filter(mobile=True)
    category = None
    categories = Category.objects.all()
    sorter = Sorter.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        try:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        except:
            pass
    return render(request,
                  'shop/product/testlist.html',
                  {'category': category,'bar':bar,'mobar':mobar,
                   'categories': categories,'sorter':sorter,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})

def product(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/product.html',
                  {'product': product, 'cart_product_form': cart_product_form})

def first(request, category_slug=None):
    category = None
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()
    sorter = Sorter.objects.all()
    if category_slug:
        category = get_object_or_404(FirstCategory, slug=category_slug)
        second = SecondCategory.objects.filter(secondcategory=category)
        products = Product.objects.filter(available=True).filter(thirdcategory=second[0])
        for item in second:
            products |= Product.objects.filter(available=True).filter(thirdcategory=item)

    return render(request,
                  'shop/product/first.html',
                  {'category': category, 'cart_product_form': cart_product_form,
                   'categories': categories,
                   'firstproducts': products,
                  'sorter':sorter})



def second(request, category_slug=None, firstcategory_slug= None, secondcategory_slug=None):
    bar = Mainbar.objects.all()
    mobar = Mainbar.objects.filter(mobile=True)
    category = None

    categories = Category.objects.all()
    sorter = Sorter.objects.all()
    products = Product.objects.filter(available=True)
    secondcategories = SecondCategory.objects.all()
    # if firstcategory_slug:
    #     secondcategories = SecondCategory.objects.filter(secondcategory=get_object_or_404(FirstCategory, slug=firstcategory_slug))
    #     print(secondcategories)

    if secondcategory_slug:
        category = get_object_or_404(SecondCategory, slug=secondcategory_slug)
        products = products.filter(thirdcategory=category)
        category = get_object_or_404(Category, slug=category_slug)
    else:
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
    firstcategories=FirstCategory.objects.filter(firstcategory=get_object_or_404(Category, slug=category_slug))
    # page = request.GET.get('page')

    t=3
    fproduct = ProductFilter(request.GET, queryset=products)
    paginator = Paginator(fproduct.qs, t)  # 6 posts in each page
    page = request.GET.get('page')
    filterrequest=request.GET
    filterrequest._mutable = True
    print(filterrequest)

    if page:
        del filterrequest['page']
        lqty = int(page)*t
        uqty = int(page) * t+t
    else:
        lqty=1
        uqty=1*t

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
    print(filterrequest.get('lqty'))
    return render(request,
                  'shop/product/shop-sidebar.html',
                  {'category': category, 'bar': bar, 'mobar': mobar, 'page': page, 'filter': fproduct,'filterrequest':filterrequest,'lqty':lqty, 'uqty' :uqty,
                   'categories': categories, 'sorter': sorter, 'firstcategories':firstcategories,  'opencategory':firstcategory_slug,
                   'products': products})



def shop_sidebar(request, category_slug=None):
    bar= Mainbar.objects.all()
    mobar = Mainbar.objects.filter(mobile=True)
    category = None
    categories = Category.objects.all()
    sorter = Sorter.objects.all()
    products = Product.objects.filter(available=True)


    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request,
                  'shop/product/shop-sidebar.html',
                  {'category': category,'bar':bar,'mobar':mobar,'page': page, 'filter': f,
                   'categories': categories,'sorter':sorter,
                   'products': products})
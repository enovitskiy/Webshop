from django.shortcuts import render
from .models import Subnavigator,Navconstruct,Social,Footer,Text,Footercont,Example, Faqblock, Contact, Contdecr, Textslider, Mpage, Values, Etapy
from .forms import ContactForm
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings





def example(request, slug,sslug,ssslug):
    response = {}
    response.update(csrf(request))
    response['nav'] = Navconstruct.objects.all()
    topic = [Example.objects.get(slug=ssslug)][0]
    if slug:
        response['page'] = [Navconstruct.objects.get(slug=slug)]
    else:
        response['page'] = None
    response['info'] = Social.objects.filter(social=False)
    if sslug:
        response['spage'] = None
    if ssslug:
        response['sspage'] = [Example.objects.get(slug=ssslug)]
    else:
        response['sspage'] = None
    response['info'] = Social.objects.filter(social=False)
    response['path0'] = [Navconstruct.objects.get(slug=slug)][0]
    response['social'] = [Social.objects.filter(social=True)]
    response['footer'] = Footer.objects.all()
    response['foot'] = Footercont.objects.all()
    response['text'] = Text.objects.all()
    response['path0'] = [Navconstruct.objects.get(slug=slug)][0]
    response['topic'] = topic.projectname
    response['description'] = topic.description
    response['keywords'] = topic.keywords




    return render(request, 'bi.html', response)

def construction(request, slug,sslug='empty'):
    response = {}
    response.update(csrf(request))
    response['nav'] = Navconstruct.objects.all()
    response['subnav'] = Subnavigator.objects.all()
    topic = [Subnavigator.objects.get(slug=sslug)][0]
    if sslug == 'slub':
        response['faq'] = [Faqblock.objects.get(name='Deep')][0]
    if slug:
        response['page'] = [Navconstruct.objects.get(slug=slug)]
    else:
        response['page'] = None
    response['info'] = Social.objects.filter(social=False)
    if sslug:
        response['spage'] = [Subnavigator.objects.get(slug=sslug)]
    else:
        response['spage'] = None
    response['info'] = Social.objects.filter(social=False)
    response['path0'] = [Navconstruct.objects.get(slug=slug)][0]
    response['path1'] = topic
    response['social'] = [Social.objects.filter(social=True)]
    response['footer'] = Footer.objects.all()
    response['foot'] = Footercont.objects.all()
    response['text'] = Text.objects.all()
    response['topic'] = topic.title
    response['description'] = topic.descrtionmeta
    response['keywords'] = topic.keywordsmeta
    return render(request, 'bi.html', response)


def main(request, slug = 'treschina'):
    response = {}
    response.update(csrf(request))
    response['nav'] = Navconstruct.objects.all()
    response['subnav'] = Subnavigator.objects.all()
    response['Textslider'] = Textslider.objects.all()
    topic = [Navconstruct.objects.get(slug=slug)][0]
    response['topic'] = topic.title
    response['description'] = topic.descrtionmeta
    response['keywords'] = topic.keywordsmeta
    if slug:
        response['page'] = [Navconstruct.objects.get(slug=slug)]
    else:
        response['page'] = False
    response['info'] = Social.objects.filter(social=False)
    response['social'] = Social.objects.filter(social=True)
    response['footer'] = Footer.objects.all()
    response['foot'] = Footercont.objects.all()
    response['text'] = Text.objects.all()

    response['title'] = [Navconstruct.objects.get(slug="company")][0]
    if slug:
        response['path0'] = topic
    else:
        response['path0'] = False
    if slug == 'treschina':
        response['Mpage'] = [Mpage.objects.get()][0]
        response['Etapy'] = Etapy.objects.all()
        response['Values'] = Values.objects.all()
        response['page'] = False
        response['path0'] = False






    return render(request, 'bi.html', response)

# Функция формы обратной связи

def contactform(reguest, slug = 'contact'):

    nav = Navconstruct.objects.all()
    page = [Navconstruct.objects.get(slug=slug)]
    contdecr = [Contdecr.objects.get()][0]
    contact = Contact.objects.all()
    info = Social.objects.filter(social=False)
    social = Social.objects.filter(social=True)
    footer = Footer.objects.all()
    foot = Footercont.objects.all()
    topic = [Navconstruct.objects.get(slug=slug)][0]


    if slug:
        path0 = topic
    else:
        path0 = None



    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения

        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']


            recepients = ['ugeopolimer@gmail.com']


            if copy:
                recepients.append(sender)
            try:
                send_mail(subject, message, 'ugeopolimer@gmail.com', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest,'bi.html',
            {'form': form, 'info':info, 'social':social, 'footer':footer, 'foot':foot, 'path0':path0,'topic':topic.title,
             'description':topic.descrtionmeta, 'keywords': topic.keywordsmeta,
             'page': page, 'nav': nav, 'contdecr': contdecr,
             'contact': contact, 'GOOGLE_RECAPTCHA_SITE_KEY': settings.GOOGLE_RECAPTCHA_SITE_KEY,})





def thanks(reguest):
    info = Social.objects.filter(social=False)
    social = Social.objects.filter(social=True)
    footer = Footer.objects.all()
    foot = Footercont.objects.all()
    path0 = [Navconstruct.objects.get(slug='fundament')][0]
    thanks = 'thanks'
    return render(reguest, 'bi.html', {'page': thanks, 'info':info,  'description':path0.descrtionmeta, 'keywords': path0.keywordsmeta,
                                       'social':social, 'footer':footer, 'foot':foot,'path0':path0,'topic': path0.title})


# Create your views here.

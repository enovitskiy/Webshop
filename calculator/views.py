from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import HomeForm, ElementsForm, ParametersForm
from .models import Job, Element
from .calculator import Calculator
from data.models import Product
from formtools.wizard.views import SessionWizardView


from io import StringIO,BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape



def render_to_pdf(template_src, context_dict):
    print(template_src,context_dict)
    template = get_template(template_src)
    context = context_dict
    html  = template.render(context)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-16")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))



FORMS = [
      ("element", ElementsForm),
      ("parameters", ParametersForm)
  ]
TEMPLATES = {
      "element" : "calculator/student.html",
      "parameters" : "calculator/contract.html"
  }

class AddStudentWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        print(form)
        context = super(AddStudentWizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == 'parameters':
            context.update({'ok': 'True'})
        return context

    def done(self, form_list, **kwargs):
        print(form_list)
        # student_form = form_list[0].cleaned_data
        # contract_form = form_list[1].cleaned_data
        # s = Student.objects.create(
        #     sex=student_form['sex'],
        #     citizenship=student_form['citizenship'],
        #     doc=student_form['doc'],
        #     student_document_type=student_form['student_document_type'],
        #     parent_document_type=student_form['parent_document_type']
        # )
        # f = FioChange.objects.create(
        #     student=s,
        #     event_date=student_form['event_date'],
        #     fio=student_form['fio']
        # )
        # c = Contract.objects.create(
        #     student=s,
        #     number=contract_form['number'],
        #     student_home_phone=contract_form['phone']
        # )
        return HttpResponseRedirect(reverse('liststudent'))



# Create your views here.
class HomePage(TemplateView):
    template_name = 'calculator/home.html'

    def get(self, request, *args, **kwargs):
        form = HomeForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['num1']
            text2 = form.cleaned_data['num2']
            if 'add' in request.POST:
                result = text + text2
            elif 'sub' in request.POST:
                result = text - text2
            elif 'mul' in request.POST:
                result = text * text2
            elif 'div' in request.POST:
                result = text / text2

            form = HomeForm()
            #return redirect ('home:home')

        args = {'form': form , 'result': result}
        return render(request, self.template_name, args )


def calculator(request):
    print("1")

    calculator = Calculator(request)


    if request.method == 'GET':
        Parameters = ParametersForm(request.GET)
        Elements = ElementsForm(request.GET)
        if (request.GET.get('print_btn')) and Parameters.is_valid():

            numbers = Parameters.cleaned_data
            for i in numbers:
                if numbers[i]==None:
                    numbers[i]=0

            job = Job.objects.filter(process=request.GET.get('quantity'))
            element = Element.objects.filter(id=request.GET.get('quantity'))

            for i in job:
                calculator.add(job=i, num1=numbers['num1'], num2=numbers['num2'], element=element[0].name)
            return render(request, 'calculator/calculator.html',
                          {'ElementsForm': Elements, 'ParametersForm': Parameters, 'calculator': calculator})
        elif Elements.is_valid():
            cd = Elements.cleaned_data
            calculator.element(cd['quantity'])
            return render(request, 'calculator/calculator.html',
                  {'ElementsForm': Elements, 'ParametersForm':Parameters, 'calculator':calculator } )
        else:
            Elements = ElementsForm()


    else:
        Elements = ElementsForm()
        Parameters=ParametersForm()



    return render(request, 'calculator/calculator.html',
                  {'ElementsForm': Elements, 'ParametersForm':Parameters, 'calculator':calculator})

def calculator_remove(request, id, element_id):
    if id=='main':
        calculator= Calculator(request)
        elements = get_object_or_404(Element, id=element_id)
        calculator.mainremove(elements.name)
    elif id=='process':
        calculator= Calculator(request)
        process = get_object_or_404(Job, id=element_id)
        calculator.processremove(process.name)
    elif id=='product':
        calculator= Calculator(request)
        product = get_object_or_404(Product, id=element_id)
        calculator.productremove(product.name)

    return redirect('calculator:calculator')
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

import pdfcrowd

def test(request):
    calculator = Calculator(request)
    Elements = ElementsForm()
    Parameters = ParametersForm()
    api = pdfcrowd.HtmlToPdfClient("evgeniy111", "9fcddf22e94642a39acf43b932382beb")
    api.convertUrlToFile('http://uretekbelarus.com', '/Users/apple/PycharmProjects/Uretekweb/uretek/static/constra-free/themes/example.pdf')
    print(api)
    return render_to_pdf(
        'calculator/invoice.html',
        {
            'pagesize': 'A4',
            'ElementsForm': Elements, 'ParametersForm':Parameters, 'calculator':calculator
        }
    )

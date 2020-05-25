from decimal import Decimal
from django.conf import settings
from .models import Job, Element
from data.models import Product
from plotly import figure_factory as Figure
import datetime
from datetime import timedelta


def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False




class Calculator(object):

    def __init__(self, request):
        """
        Инициализируем расчет
        """
        self.session = request.session
        calculator = self.session.get(settings.CALCULATOR_SESSION_ID)



        if not calculator:
            # save an empty cart in the session
            calculator = self.session[settings.CALCULATOR_SESSION_ID] = {}

        self.calculator = calculator

    def element(self, item):
        element=Element.objects.filter(name=item)[0]
        element_id = str(element)
        if element_id not in self.calculator:
            self.calculator[element.name] = {}
            self.save()




    def add(self, job, element, num1=1, num2=1):
        """
        Добавить продукт в корзину или обновить его количество. Ready
        """

        element_id = str(element)


        if element_id in self.calculator:
            print(element_id)
            job_id=str(job.id)
            if job_id not in self.calculator[element_id]:

                hours = str(num1 * num2 * job.norms)
                square = str(num1 * num2)
                items = []

                it=[]
                for i in job.materials.all():

                    items.append(i.id)
                self.calculator[element_id][job_id]= {'job': job.name, 'hours':hours, 'materials': items,'square':square }

                for i in job.job_norms.all():
                    norms = {}
                    if str(i.norms):
                        norms[str(i.product.id)] = str(i.norms)
                    else:
                        norms[str(i.product.id)] = ['0']

                    it.append(norms)

                    self.calculator[element_id][job_id]['norms'] = it
            else:
                hours = str(num1 * num2 * job.norms)
                square = str(num1 * num2)
                self.calculator[element_id][job_id]['hours']=hours
                self.calculator[element_id][job_id]['square'] = square

        self.save()



    def save(self):
        # Обновление сессии calculator
        self.session[settings.CALCULATOR_SESSION_ID] = self.calculator
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """

        for item in self.calculator.values():
            yield item

    def remove_all(self):

        self.calculator.clear()
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.save()

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CALCULATOR_SESSION_ID]
        self.session.modified = True

    def figure(self):
        # создание графика
        df = []
        print('df')
        for element_id in self.calculator.values():

            date = datetime.datetime.now()

            count=0
            for key,job in element_id.items():
                if is_digit(key):
                    try:

                        count+=1
                        days = timedelta(hours=int(float(job['hours'])))

                        if count==1:
                            df.append(dict(Task=job['job'], Start=date, Finish=date + days))
                            date = date + days
                        else:
                            df.append(dict(Task=job['job'], Start=date, Finish=date+days))
                            date = date + days

                    except:
                        pass

        fig_json = None
        try:
            figure = Figure.create_gantt(df)
            fig_json = figure.to_json()
        except:
            pass
        return fig_json

    def materials(self):
        prod_ids = []
        for i in self.calculator.element.values():
            prod_ids.extend(i['materials'])
        materials = Product.objects.filter(id__in=prod_ids)
        return materials



    def norms(self):
        prod_ids = []
        norms_ids = {}
        for element_id in self.calculator:
            for i in self.calculator[element_id].values():
                try:
                    for j in i['norms']:
                        for key, val in j.items():
                            if key not in prod_ids:
                                prod_ids.append(key)
                                quantity=float(i['square'])*float(val)
                                total=quantity*float(Product.objects.filter(id=key)[0].price)

                                norms_ids[key]={'quantity':quantity,'total':total, 'materials': Product.objects.filter(id=key)[0]}

                            else:
                                quantity=float(norms_ids[key]['quantity']) + float(i['square'])* float(val)
                                total = quantity * float(Product.objects.filter(id=key)[0].price)
                                norms_ids.update({key:{'quantity': quantity ,'total':total,
                                          'materials': Product.objects.filter(id=key)[0]}})
                except:
                    pass
        return norms_ids

    def main(self):
        main={}
        for element in Element.objects.filter(name__in=self.calculator.keys()):
            main[element.name] = element
        return main

    def mainremove(self, element):
        if element in self.calculator.keys():
            del self.calculator[element]
            self.save()

    def process(self):
        process = {}
        for element in self.calculator:
            for job in self.calculator[element].values():
               if job['job'] not in process.keys():
                   process[job['job']]= {'hours':job['hours'], 'id' : Job.objects.filter(name=job['job'])[0]}

               else:
                   process[job['job']]['hours'] = float(process[job['job']]['hours'])+float(job['hours'])
        return process

    def processremove(self, process):
        job=Job.objects.filter(name=process)[0]
        for element in self.calculator.values():
            if str(job.id) in element.keys():
                del element[str(job.id)]
        self.save()

    def productremove(self, material):
        item = Product.objects.filter(name=material)[0]
        for value in self.calculator.values():
            for product in value.values():
                try:
                    for i in product['norms']:
                        if str(item.id) in i.keys():
                            del i[str(item.id)]
                except:
                    pass
        self.save()
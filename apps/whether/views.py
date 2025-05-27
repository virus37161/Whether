from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from whether.utils.get_lat_lon import get_cordinate
from whether.utils.get_whether import whether


class GenerateHtmlView(View):
    """Генерирует HTML-страницу с динамическим контентом"""

    def process_user_text(self, text):
        """Обработка введенного текста (названия города)"""
        return text.strip().title()  # Приводим к нормальному виду (Первая Буква Большая)

    def get_initial_data(self, request):
        user_text = request.GET.get('user_text', '')
        if not user_text:
            return {}

        processed_text = self.process_user_text(user_text)
        dict = get_cordinate(processed_text)
        if dict==None:
            return {'Error': 'Данный город не поддерживается'}

        list_whether = whether(dict)

        if list_whether==None:
            return {'Error': 'Данный город не поддерживается'}
        else:
            return {
                'list_whether': list_whether,
                'user_text': processed_text
            }

    def get(self, request):
        context = self.get_initial_data(request)
        return render(request, 'main.html', context)

    

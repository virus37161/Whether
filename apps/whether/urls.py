from django.urls import path, include
from whether.views import GenerateHtmlView


urlpatterns = [
    path('', GenerateHtmlView.as_view(), name='generated-page'),

]
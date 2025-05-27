from django.urls import path
from whether.views import GenerateHtmlView

urlpatterns = [
    path('', GenerateHtmlView.as_view(), name='generated-page'),
]
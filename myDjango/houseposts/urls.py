from django.conf.urls import url
from houseposts import views

urlpatterns = [
    url(r'^$',views.index, name='index')
    ]
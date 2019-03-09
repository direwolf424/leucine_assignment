from django.conf.urls import url

from tutorial.quickstart import views

urlpatterns = [
    url(r'^document/', views.Document.as_view(), name='document'),
]
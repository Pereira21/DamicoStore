from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("quem-somos", views.quemSomos, name="quemSomos"),
    path("masculino", views.masculino, name="masculino"),
    path("feminino", views.feminino, name="feminino"),
    #path("hello/<name>", views.hello_there, name="hello_there")
]

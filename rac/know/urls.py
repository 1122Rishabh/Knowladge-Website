from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="KnowHome"),
    path("index/",views.index,name="indexus"),
    path("contact/",views.contact,name="ContactUs"),
    path("about/",views.about,name="AboutUs"),
    path("php/",views.php,name="phpus"),
    path("javascript/",views.javascript,name="ContactUs"),
    path("C/",views.C,name="ContactUs"),
    path("Cn/",views.Cn,name="ContactUs"),
    path("ml/",views.ml,name="ContactUs"),
    path("ai/",views.ai,name="ContactUs"),
    path("java/",views.java,name="ContactUs"),
    path("python/",views.python,name="ContactUs"),
    path("ide/",views.ide,name="ContactUs"),
    path("javaide/",views.javaide,name="ContactUs"),
    path("phpide/",views.phpide,name="ContactUs"),
    path("javascriptide/",views.javascriptide,name="ContactUs"),
    path("cide/",views.cide,name="ContactUs"),
    path("cnide/",views.cnide,name="ContactUs"),
]
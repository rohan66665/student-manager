from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_student, name="add_student"),
    path("view/", views.view_students, name="view_students"),
    path("", views.home, name="home"),   # 👈 home added here
]

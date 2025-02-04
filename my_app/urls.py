from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home ,name='home'),
    path('read/',read),
    path('delete/<int:id>/',delete_task,name = "delete_student"),
    path('update/<int:id>/',update_task,name = "update_student"),
    path('signup/',signup,name='signup'),
    path('login/',login_view,name='login')
]
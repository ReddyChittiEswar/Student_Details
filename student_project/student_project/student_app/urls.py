from django.urls import path
from . import views

urlpatterns = [
    path('students_list/', views.student_list, name = 'student_list'),
		path('create_student/', views.student_create, name = 'student_create'),
		path('update_student/<int:id>/', views.student_update, name = 'student_update'),
		path('delete_student/<int:id>/', views.student_delete, name = 'student_delete'),
		path('', views.student_list),
]

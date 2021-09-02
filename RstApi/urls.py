from django.contrib import admin
from django.urls import path
from Api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>',views.Student_detail),
    path('stulist/',views.Student_List),
]

from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    
    
    #admin
    path('admin-login/', views.admin_login, name='admin-login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('admin-logout/',views.admin_logout,name='admin-logout'),
    
    
    #for project
    path("project-add/",views.add_project,name='project_add'),
    path('projects/image/<str:file_id>/', views.serve_project_image, name='serve_project_image'),
    
    #for client 
    path("client-add/",views.add_client,name='client_add'),
    path('clients/image/<str:file_id>/', views.serve_client_image, name='serve_client_image'),
    
    #for contactform
    path("contact-add/",views.add_contact),   
    
    #for subscribed emails
    path("subscribed/",views.subscribe,name="subscribe"),

]
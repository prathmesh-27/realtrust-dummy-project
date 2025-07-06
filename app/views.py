from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,FileResponse
from bson import ObjectId
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json
from .models import *


def home(request):
    clients = Client.objects().all()
    projects = Project.objects.all()
    data ={
        'clients': clients,
        'projects':projects
    }
    return render(request, 'app/home.html',data)


def admin_dashboard(request):
    if not request.session.get('is_admin'):
        return redirect('admin-login')
    
    subscribedEmail = SubscribedEmail.objects.all()
    contacts = ContactForm.objects.all()
    
    data = {
    "emails":[s.email_id for s in subscribedEmail],
    "contacts":[{"name":c.full_name,"email":c.email,"mobile":c.mobile,"city":c.city} for c in contacts], 
    }
    
    return render(request,'app/admin_dashboard.html',data)

def admin_logout(request):
    request.session.flush()
    return redirect('home')

@csrf_protect
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == 'admin' and password == '1234':
            request.session['is_admin'] = True
            return redirect('admin-dashboard')
        else:
            return render(request, 'app/forms/admin_login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'app/forms/admin_login.html')



@csrf_protect
def add_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('name')
        project_img = request.FILES.get('image')
        project_description = request.POST.get('description')
        project_loc = request.POST.get('location')

        if not all([project_name, project_img, project_description, project_loc]):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        # Create the document without the image first
        project = Project(
            project_name=project_name,
            project_description=project_description,
            project_location=project_loc
        )

        # Save the image using GridFS
        project.project_image.put(
            project_img,
            content_type=project_img.content_type,
            filename=project_img.name
        )

        # Save the whole document
        project.save()
        messages.success(request, 'Project added successfully!')
        return redirect('admin-dashboard')
    
    return redirect('admin-dashboard')



def serve_project_image(request, file_id):
    try:
        project = Project.objects.get(project_image=ObjectId(file_id))
        return FileResponse(project.project_image, content_type='image/jpeg')
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Image not found'}, status=404)



def add_client(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        designation = request.POST.get('designation')
        img = request.FILES.get('image')        
        
        if not all([name, description, designation, img]):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        # Create the document without the image first
        client = Client(
            client_name=name,
            client_description=description,
            client_designation=designation
        )

        # Save the image using GridFS
        client.client_image.put(
            img,
            content_type=img.content_type,
            filename=img.name
        )

        # Save the whole document
        client.save()
        messages.success(request, 'Client added successfully!')
        return redirect('admin-dashboard')

    return redirect("admin-dashboard")


def serve_client_image(request,file_id):
    try:
        client = Client.objects.get(client_image=ObjectId(file_id))
        return FileResponse(client.client_image, content_type='image/jpeg')
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Image not found'}, status=404)



@csrf_protect
def add_contact(request):
    if request.method =="POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        city = request.POST.get("city")
        
        if not all([name, mobile, email, city]):
            return JsonResponse({'error': 'All fields are required'}, status=400)
        
        contact = ContactForm(full_name= name,mobile=mobile,email=email,city=city)
        contact.save()
        messages.success(request,"Your details had recorded successfully.We will get back to you soon.")
        return redirect('home')
        
    return redirect('home')   
        


@csrf_protect
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        SubscribedEmail(email_id=email).save()
        messages.success(request,"You Subscribed to our service.")
        return redirect('home')
 

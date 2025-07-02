from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,FileResponse
from bson import ObjectId
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json
from .models import *


def home(request):
    return render(request, 'app/home.html')


def admin_dashboard(request):
    if not request.session.get('is_admin'):
        return redirect('admin-login')
    return render(request,'app/admin_dashboard.html')

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

        return JsonResponse({
            'message': 'Image uploaded successfully!',
            'project': {
                'name': project.project_name,
                'location': project.project_location,
                'description': project.project_description
            }
        })

    return render(request,'app/forms/project_form.html')


def show_projects(request):
    projects = Project.objects.all()
    return render(request, 'app/show_projects.html', {'projects': projects})

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
        
        return JsonResponse({
            'message': 'Image uploaded successfully!',
            'project': {
                'name': client.client_name,
                'designation': client.client_designation,
                'description': client.client_description
            }
        })

    return render(request,'app/forms/client_form.html')

def show_clients(request):
    clients = Client.objects().all()
    return render(request, 'app/show_clients.html', {'clients': clients})

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
        
        return JsonResponse({'message': 'Data saved successfully!'})
        
    return render(request,"app/forms/contact_form.html")    
        

def view_contacts(request):
    contacts = ContactForm.objects().all()
    return JsonResponse({"contacts":[{"name":c.full_name,"email":c.email,"mobile":c.mobile,"city":c.city} for c in contacts]})



@csrf_protect
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        SubscribedEmail(email=email).save()
        return HttpResponse("Student saved via form.")
 

def show_subscribed_emails(request):
    subscribedEmail = SubscribedEmail.objects.all()
    return JsonResponse({'emails': [s.email_id for s in subscribedEmail]})
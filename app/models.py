from mongoengine import Document, StringField, FileField, EmailField

class Project(Document):
    project_name = StringField(required=True,unique=True)
    project_image = FileField(required=True)
    project_description = StringField(required=True)
    project_location = StringField(required=True)

class Client(Document):
    client_image = FileField(required=True)
    client_name = StringField(required=True)
    client_description = StringField(required=True)
    client_designation = StringField(required=True)

class ContactForm(Document):
    full_name = StringField(required=True)
    mobile = StringField(required=True, regex=r'^\d{10}$')  # 10-digit mobile
    email = EmailField(required=True, unique=True)
    city = StringField(required=True)

class SubscribedEmail(Document):
    email_id = EmailField(required=True, unique=True)

from datetime import datetime
from mongoengine import Document, StringField, EmailField, DateTimeField, ReferenceField, DictField
from .role import Role
from .organization import Organization


class User(Document):
    name = StringField(required=True, max_length=255)
    email = EmailField(required=True, unique=True)
    phone = StringField(max_length=10)
    password = StringField(required=True)
    role = ReferenceField(Role, required=True)
    organization = ReferenceField(Organization, required=True)
    department = StringField(max_length=255)
    designation = StringField(max_length=255)
    face_data = DictField()  # JSON/Binary for face encoding
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

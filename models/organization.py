from datetime import datetime
from mongoengine import Document, StringField, EmailField, DateTimeField


class Organization(Document):
    name = StringField(required=True, max_length=255)
    organizations_type = StringField(choices=["School", "College", "Company"], required=True)
    attendance_type = StringField(choices=["in_out", "present"], required=True)
    contact_email = EmailField()
    address = StringField(max_length=255)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

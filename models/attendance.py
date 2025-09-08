from datetime import datetime
from mongoengine import Document, StringField, DateTimeField, ReferenceField
from .user import User
from .organization import Organization
from .session import Session


class Attendance(Document):
    user = ReferenceField(User, required=True)
    organization = ReferenceField(Organization, required=True)
    session = ReferenceField(Session, required=True)
    log_type = StringField(choices=["in", "out", "present"], required=True)
    timestamp = DateTimeField(default=datetime.utcnow)
    marked_by = StringField(choices=["system", "user"], required=True)
    remarks = StringField(max_length=255)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

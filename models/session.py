from datetime import datetime
from mongoengine import Document, StringField, DateTimeField, ReferenceField
from .organization import Organization


class Session(Document):
    organization = ReferenceField(Organization, required=True)
    name = StringField(required=True, max_length=255)
    in_time = DateTimeField(required=True)
    out_time = DateTimeField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

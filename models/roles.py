from datetime import datetime
from mongoengine import Document, StringField, ListField, DateTimeField


class Role(Document):
    name = StringField(required=True, unique=True, max_length=255)
    permissions = ListField(StringField(), default=[])
    description = StringField(max_length=255)
    created_at = DateTimeField(default=datetime.utcnow)

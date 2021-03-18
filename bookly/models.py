from mongoengine import *
import datetime

class Post(Document):
    """
    Blog post document
    """
    title = StringField(required=True, unique=True)
    tags = ListField(required=True)
    content = StringField(required=True)
    creation_date = DateTimeField()
    modified_date = DateTimeField(default=datetime.datetime.now)  
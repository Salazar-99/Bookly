from mongoengine import *
from dotenv import load_dotenv
import os

load_dotenv()

def configure_and_connect(config_path: str = '.') -> None:
    """
    Load the database configuration from the environment file at config_path
    and connect to the remote database
    """
    host = os.environ.get('MONGO_URI')
    connect(host=host)
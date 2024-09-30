import os
from dotenv import load_dotenv


load_dotenv()
#DATABASE ENV VARIABLES
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
#Celery
REDIS_URL = os.getenv('REDIS_URL')
MAILERSEND_API_KEY = os.getenv('MAILERSEND_API_KEY')
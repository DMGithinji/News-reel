from app import app
import urllib.request,json
from .models import categorized_sources_model

# Getting api key
api_key = app.config['API_KEY']



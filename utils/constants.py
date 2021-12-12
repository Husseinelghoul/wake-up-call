"""
script to load constance from enviorement,
with default values in case the variable name wasn't found
"""
import os

from dotenv import load_dotenv

load_dotenv()

TO = os.getenv('TO')
FROM = os.getenv('FROM')
LOG_LEVEL = os.getenv('LOG_LEVEL','INFO')
ENVIRONMENT = os.getenv('ENVIRONMENT','development')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')

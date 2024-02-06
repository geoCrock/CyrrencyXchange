import os
from dotenv import load_dotenv

load_dotenv()

POSTGRESQL_URL = os.environ.get('POSTGRESQL_URL')

import os

from dotenv import load_dotenv
load_dotenv()

DIFY_API_KEY = os.getenv('DIFY_API_KEY')
WORKFLOW_URL = os.getenv('WORKFLOW_URL')
WORKFLOW_ID = os.getenv("WORKFLOW_ID")


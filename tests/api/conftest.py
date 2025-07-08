import os
from dotenv import load_dotenv
import pytest


load_dotenv()
url = os.getenv('base_url')

@pytest.fixture()
def base_api_url():
    base_url = url
    return base_url
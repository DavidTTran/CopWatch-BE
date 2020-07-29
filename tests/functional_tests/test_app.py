import pytest
import requests
import json

from dotenv import load_dotenv
load_dotenv()

import os
env_url = os.environ.get('TEST_URL')

url = f'{env_url}'

def test_index_page():
    response = requests.get(url+'/api/v1/reports')
    assert response.status_code == 200

    resp_body = response.json()

    # assert len(resp_body) == 0
    # assert resp_body[0]['description'] == 'Report 3'

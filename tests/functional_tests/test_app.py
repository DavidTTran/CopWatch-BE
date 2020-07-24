import pytest
import requests
import json

url = 'http://localhost:5000'

def test_index_page():
    response = requests.get(url+'/api/v1/reports')
    assert response.status_code == 200
    
    resp_body = response.json()

    assert len(resp_body) == 3
    assert resp_body[0]['description'] == 'Report 3'

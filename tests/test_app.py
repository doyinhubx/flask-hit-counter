import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app

def test_home():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"You\xe2\x80\x99ve visited this page" in response.data

def test_reset():
    client = app.app.test_client()
    client.get("/")  # increment
    response = client.post("/reset")
    assert response.status_code == 200
    assert b"You\xe2\x80\x99ve visited this page" in response.data

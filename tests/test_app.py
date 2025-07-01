import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app

def test_home():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data

def test_reset():
    client = app.app.test_client()
    client.get("/")  # increment at least once
    reset_response = client.post("/reset")
    assert b"reset" in reset_response.data
    after_reset = client.get("/")
    assert b"visited 1 times" in after_reset.data

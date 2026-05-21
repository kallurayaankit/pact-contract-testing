import json
import subprocess
import time
import sys
import pytest
import requests

@pytest.fixture(scope="module")
def start_provider():
    """Start the Flask app in the background using the same Python interpreter."""
    proc = subprocess.Popen(
        [sys.executable, "provider/app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # Wait until Flask is actually ready to accept connections
    for _ in range(10):
        try:
            r = requests.get("http://127.0.0.1:5000/users/1")
            if r.status_code in (200, 404):  # any valid HTTP response means it's up
                break
        except requests.ConnectionError:
            time.sleep(1)
    else:
        proc.terminate()
        pytest.fail("Flask app did not start in time")
    yield
    proc.terminate()

def test_provider_against_contract(start_provider):
    """Read the contract file and check that the real API matches every interaction."""
    with open("pacts/userwebfrontend-userservice.json") as f:
        contract = json.load(f)

    for interaction in contract["interactions"]:
        method = interaction["request"]["method"]
        path = interaction["request"]["path"]
        expected_status = interaction["response"]["status"]
        expected_body = interaction["response"]["body"]

        url = f"http://127.0.0.1:5000{path}"
        response = requests.request(method, url)

        assert response.status_code == expected_status, \
            f"Expected {expected_status}, got {response.status_code} for {method} {path}"
        assert response.json() == expected_body, \
            f"Body mismatch for {method} {path}: expected {expected_body}, got {response.json()}"
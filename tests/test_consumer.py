import json
import os

def test_generate_contract():
    """Create a Pact‑like contract file that defines the expected interaction."""
    contract = {
        "consumer": {"name": "UserWebFrontend"},
        "provider": {"name": "UserService"},
        "interactions": [
            {
                "description": "a request for user 1",
                "providerState": "user with ID 1 exists",
                "request": {
                    "method": "GET",
                    "path": "/users/1"
                },
                "response": {
                    "status": 200,
                    "headers": {"Content-Type": "application/json"},
                    "body": {
                        "name": "Alice",
                        "email": "alice@example.com"
                    }
                }
            }
        ],
        "metadata": {
            "pactSpecification": {"version": "3.0.0"}
        }
    }
    os.makedirs("pacts", exist_ok=True)
    with open("pacts/userwebfrontend-userservice.json", "w") as f:
        json.dump(contract, f, indent=2)
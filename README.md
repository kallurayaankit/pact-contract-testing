# Pact Contract Testing

![CI](https://github.com/kallurayaankit/pact-contract-testing/actions/workflows/ci.yml/badge.svg)

Consumer‑driven contract testing using **Pact** (Python).  
A consumer defines expectations and a provider is verified against those expectations automatically.

## What it does
- A Flask provider serves user data.
- A Python consumer defines the contract (expected request/response).
- Pact generates a JSON contract file.
- The provider is then verified against that contract.
- CI runs everything on every push.

## Why it matters
Microservices must communicate reliably. Contract testing catches breaking API changes **before** they reach production — without deploying the whole system.

## How to run locally

```bash
git clone https://github.com/kallurayaankit/pact-contract-testing.git
cd pact-contract-testing
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
pytest
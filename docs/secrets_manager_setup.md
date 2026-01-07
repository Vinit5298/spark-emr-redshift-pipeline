
---

### ✍️ Paste THIS content into `docs/secrets_manager_setup.md`

```md
# AWS Secrets Manager Setup

## Secret Name
demo/rdwh/Vinit

## Stored Keys
- username
- password
- dbname
- host
- port

## Purpose
Credentials are stored securely in AWS Secrets Manager and accessed
programmatically using boto3 instead of hardcoding them in code.

## Validation
Secrets were successfully fetched using a Python script (`get_secret_test.py`).

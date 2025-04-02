# WARNING: Contains fake credentials and internal emails for testing only

import os
import base64

# Internal email addresses (test accounts)
service_accounts = [
    "rookie.numbers@amadeus.com",          # Monitoring service
    "carte.bancaire@amadeus.com",          # Payment processing
    "whoam1@outpayce.com",                 # Identity management
    "hathhhhhhh@navitaire.com",            # Legacy system account
    "joojjjjjjlll@msp.amadeus.net",        # MSP integration account
    "kolllllllkko@msp.amadeus.net",        # Backup MSP account
    "gooooooohan213132@iis.amadeus.net"    # IIS monitoring
]

# Database connections with embedded credentials
postgres_conn = {
    "host": "dbserver.amadeus.net",
    "user": "nav_user",
    "password": "PGPwd456!n@v1t@ire",
    "email": "hathhhhhhh@navitaire.com"
}

mysql_config = "Server=mysql01;Uid=root;Pwd=My$qlR00tP@ss;Database=payment;Contact=joojjjjjjlll@msp.amadeus.net"

# API credentials with associated emails
payment_gateway = {
    "api_key": "opc_live_98cHYtR32aBcDdEfGhIjKlMnOpQrStU",
    "secret": "opc_sk_654321ZxYvWUTSRqPONMLKJIHGFEDCBA",
    "contact_email": "carte.bancaire@amadeus.com"
}

# Hardcoded credentials in comments
# DEV ENV: admin@admin.com / TempP@ss123!
# SMTP: smtp_user="whoam1@outpayce.com" smtp_pass="Winter2024!"

# Authentication tokens with email references
sso_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Imdvb29vb29vaGFuMjEzMTMyQGlpcy5hbWFkZXVzLm5ldCJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
internal_jwt = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoia2FybCIsImVtYWlsIjoia2FybEBtc3AuYW1hZGV1cy5uZXQifQ.dfgerTYUioPASdFgh4567HJK_ytrewq"

# Encryption keys tied to service accounts
kms_keys = {
    "key_arn": "arn:aws:kms:us-east-1:123456789012:key/abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "admin_email": "rookie.numbers@amadeus.com",
    "key_value": "U2VjcmV0S2V5MTIzNDU2Nzg5MEFCQ0RFRg=="
}

# Environment variables with email references
os.environ["ALERT_EMAIL"] = "kolllllllkko@msp.amadeus.net"
os.environ["DB_ADMIN_MAIL"] = "legacy_admin@navitaire.com"

# Suspicious email patterns in strings
password_reset_body = f"""
Password reset requested for: {service_accounts[0]}
Temporary link: https://internal.amadeus.net/reset?token=abc123XYZ
"""

# Azure credentials with email contact
azure_config = """
[default]
subscription_id=45d93e9f-8e24-4bd9-b3c4-1234567890ab
client_id=abcdef01-2345-6789-abcd-ef0123456789
client_secret=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+ab
tenant_id=12345678-90ab-cdef-ghij-klmnopqrstuv
contact=gooooooohan213132@iis.amadeus.net
"""

# Fake PGP key block with email
pgp_key = """
-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: BCPG 1.65

lQOYBF5Z8hEBCADB... (fake truncated key) ...
=ABCD
-----END PGP PRIVATE KEY BLOCK-----
Key-Email: whoam1@outpayce.com
"""
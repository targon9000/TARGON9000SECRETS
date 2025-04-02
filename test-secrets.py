# WARNING: This file contains numerous fake secrets for testing purposes only

import os
import base64

# Common password patterns
weak_password = "password123"
common_creds = "admin:admin@123"
basic_auth = "Authorization: Basic " + base64.b64encode(b"user:passw0rd").decode()

# API keys and tokens (typically 32-64 character hexadecimal/base64)
api_key = "sk_live_abc123xyz7890ABCDEFGHIJ1234567890"
stripe_key = "rk_live_abc123xyz7890ABCDEFGHIJ1234567890"
github_token = "ghp_abcDEfghijKLMnopQRSTuvwXYZ1234567890"
slack_token = "xoxb-1234567890-1234567890123-abcDEFghijKLmnopQRSTuvwxYZ"
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

# Database credentials
postgres_url = "postgresql://user:secretpassword@localhost:5432/mydb"
mysql_creds = "mysql://root:root_password@127.0.0.1:3306"
mongo_uri = "mongodb+srv://admin:mongo@cluster0.abc123.mongodb.net/?retryWrites=true&w=majority"

# Cloud provider secrets
aws_key = "AKIAIOSFODNN7EXAMPLE"
aws_secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
azure_key = "DefaultEndpointsProtocol=https;AccountName=testaccount;AccountKey=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789==;EndpointSuffix=core.windows.net"
gcp_key = "AIzaSyDq1234567890-ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcd"

# Encryption keys
aes_key = "U2VjcmV0S2V5MTIzNDU2Nzg5MEFCQ0RFRg=="
private_key = """
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAz7Z5h0xzmAgG8jGR9u3k5Y8C2gS7Q2gJ8Z6Y1J9X8Z1Kb0A
... (fake truncated key) ...
-----END RSA PRIVATE KEY-----
"""

# OAuth credentials
oauth_token = "ya29.A0ARrdaM-1234567890-abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
client_secret = "client_secret_1234567890abcdefghijklmnopqrstuvwxyz"

# Payment processing
stripe_secret = "sk_test_51Kq1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
paypal_key = "access_token$sandbox$abc123xyz7890$ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Social media tokens
twitter_bearer = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
facebook_token = "EAACEdEose0cBA1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Environment variables (commonly leaked in code)
os.environ["DB_PASSWORD"] = "supersecretdatabasepassword"
os.environ["STRIPE_SECRET_KEY"] = "sk_live_1234567890abcdefghijklmnopqrstuvwxyz"

# Hardcoded credentials in comments
# SECRET_KEY="django-insecure-1234567890abcdefghijklmnopqrstuvwxyz"
# Password: Summer2023!

# Fake credit card numbers
credit_card = "4111-1111-1111-1111"
cvv = "123"

# Webhooks
slack_webhook = "https://hooks.slack.com/services/T12345678/B12345678/ABCdef1234567890abcdef1234"
discord_webhook = "https://discord.com/api/webhooks/1234567890/ABCdef1234567890abcdef1234567890abcdef1234567890abcdef1234"

class AuthService:
    def __init__(self):
        self.internal_token = "INTERNAL_SECRET_1234567890_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.encryption_salt = "salt$1234567890abcdef$"

def connect_to_database():
    connection_string = "Driver={ODBC Driver 18 for SQL Server};Server=localhost;Database=test;Uid=sa;Pwd=reallyStrongPwd123;"
    return connection_string

# Fake configuration JSON
config = {
    "production": {
        "api_endpoint": "https://api.example.com",
        "auth_token": "Bearer abcdef1234567890.ghijklmnop.1234567890qrstuvwxyz",
        "license_key": "LICENSE-123456-ABCDEF-7890-GHIJK"
    }
}

# Security certificates
ssl_cert = """-----BEGIN CERTIFICATE-----
MIIDXTCCAkWgAwIBAgIJAN1234567890ABMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
... (fake truncated certificate) ...
-----END CERTIFICATE-----"""
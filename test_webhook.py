import requests
import hmac
import hashlib
import json

url = 'http://localhost:8000/webhook'
secret = 'testsecret'

# Send multiple test messages
messages = [
    {
        'message_id': 'msg001',
        'from': '+1234567890',
        'to': '+0987654321',
        'ts': '2025-12-18T10:30:00Z',
        'text': 'Hello World - Test Message 1'
    },
    {
        'message_id': 'msg002',
        'from': '+1111111111',
        'to': '+2222222222',
        'ts': '2025-12-18T10:35:00Z',
        'text': 'This is another test message'
    },
    {
        'message_id': 'msg003',
        'from': '+3333333333',
        'to': '+4444444444',
        'ts': '2025-12-18T10:40:00Z',
        'text': 'Third test message from webhook'
    }
]

for payload in messages:
    body = json.dumps(payload).encode()
    signature = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    headers = {'x-signature': signature, 'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"Message {payload['message_id']}: {response.json()}")
    except Exception as e:
        print(f"Error sending message {payload['message_id']}: {e}")

print("\nMessages sent successfully! Check http://localhost:8000/web/messages")

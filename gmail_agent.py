# gmail_agent.py
import os
import pickle
import base64
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        with open('token.json', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            'credentials/credentials.json', SCOPES)

            creds = flow.run_local_server(port=0)
        with open('token.json', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    return service

def search_messages(service, user_id='me', query=''):
    try:
        response = service.users().messages().list(userId=user_id, q=query).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])
        return messages
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_message_content(service, message_id, user_id='me'):
    try:
        message = service.users().messages().get(userId=user_id, id=message_id, format='full').execute()
        payload = message['payload']
        headers = payload.get("headers")
        subject = ""
        for header in headers:
            if header["name"] == "Subject":
                subject = header["value"]
                break
        parts = payload.get("parts")
        if parts:
            data = parts[0]['body'].get('data')
        else:
            data = payload['body'].get('data')
        if data:
            decoded_data = base64.urlsafe_b64decode(data).decode("utf-8")
        else:
            decoded_data = "[No body text found]"
        return f"Subject: {subject}\n\n{decoded_data}"
    except Exception as e:
        print(f"Error reading message: {e}")
        return None

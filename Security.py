from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# OAuth 2.0 authentication flow for Google services
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', ['https://www.googleapis.com/auth/drive.readonly'])

credentials = flow.run_local_server(port=0)

# Build the service to access Google Drive API
service = build('drive', 'v3', credentials=credentials)

# Example API call to get files from Google Drive
results = service.files().list(pageSize=10, fields="files(id, name)").execute()
items = results.get('files', [])

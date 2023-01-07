# James Butcher
# 1/7/23
#
# A test to try to set up connecting with Googe Drive API in order to
# be able to sync documents across devices.
#
# Couldn't get uploading files to work, get "insufficientPermissions"
# error, even though I added the files permissions scope on the Google
# cloud Credentials page for this app.

from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


    try:

        service = build('drive', 'v3', credentials=creds)


        # Call the Drive v3 API - List files
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))


        # Upload a text file

        file_metadata = {'name': 'notes.txt'}

        media = MediaFileUpload('notes.txt', mimetype='text/plain')

        # pylint: disable=maybe-no-member
        #file = service.files().create(uploadType=media).execute()
        #file = service.files().create('notes.txt', uploadType=media).execute()
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        print(F"FIle ID: {file.get('id')}")


    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')






if __name__ == '__main__':
    main()
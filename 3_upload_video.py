from src.Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = "youtube"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
VIDEO_NAME = "one_year.mp4"

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

"""
Works fine. There may be future issues with authorization. Delete the token*.pickle file 
and will need to reauthorize.
May be able to change this in the Create_Service function 
Could at least delete the file on failure and reauth with a try statement
"""

request_body = {
    "snippet": {
        "categoryId": 19,
        "title": "One Year of my ",
        "description": "Time lapse video of the yard",
        "tags": ["raspberry pi", "timelapse"],
    },
    "status": {
        "privacyStatus": "public",
        # "publishAt": upload_date_time, # requires privactStatus to be private
        "selfDeclaredMadeForKids": False,
    },
    "notifySubscribers": False,
}

mediaFile = MediaFileUpload("videos/" + VIDEO_NAME)

response_upload = (
    service.videos()
    .insert(part="snippet,status", body=request_body, media_body=mediaFile)
    .execute()
)

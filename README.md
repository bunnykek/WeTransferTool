# WeTransferTool
Upload and download files/folders from wetransfer.com        
You can upload a file/folder of max 2GB.   

Installation:
```
pip install WeTransferTool
```

Terminal use:
```
$> wetransfertool -h
usage: wetransfertool [-h] [-dl DL] [-ul UL] [-mw MW]

options:
  -h, --help  show this help message and exit
  -dl DL      Wetransfer file URL
  -ul UL      File/Folder path
  -mw MW      Maximum number of workers (parallel uploads)
```

API use:
```
from WeTransferTool import We

wet = We()
# to upload a file/folder to the server
metadata = wet.upload('/path/to/file', 'file name', 'message')
print(metadata)

# to download a file/folder from the server
wet.download(metadata['url'])
```

upload() method will return json containing metadata of the uploaded file/folder.   
response example:
```
{
    "id": "27f328599c99ca222222222222222222222222",
    "state": "processing",
    "transfer_type": 4,
    "shortened_url": "https://we.tl/t-222222222",
    "recommended_filename": "tomb.gif",
    "expires_at": "2022-07-10T23:01:11Z",
    "password_protected": False,
    "uploaded_at": None,
    "expiry_in_seconds": 604795,
    "size": None,
    "deleted_at": None,
    "account_id": None,
    "security_hash": "719ce3",
    "from": None,
    "creator": {
        "auth0_user_id": None,
        "email": None
    },
    "message": "test-folder-upload",
    "number_of_downloads": 0,
    "display_name": "tomb.gif",
    "files": [
        {
            "id": "b2c12c7c6fd93f1422222222222222222222222",
            "name": "tomb.gif",
            "retries": 0,
            "size": 5501922,
            "item_type": "file",
            "chunk_size": 15728640
        }
    ],
    "recipients": []
}
```

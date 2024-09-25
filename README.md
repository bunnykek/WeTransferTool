# WeTransferTool

Upload and download files/folders from wetransfer.com  
You can upload a file/folder of max 2GB.

Background:
This repository functions acts as an unofficial WeTransfer Api.
WeTransfer allows users to seamlessly and anonymously transfer files with a link.
WeTransfer's official Api was discontinued (May 31st, 2022).
Their team likely didn’t have enough time or resources to continue maintenance.
Because of this, we decided to create this public API to act as a way to programatically interact with Wetransfer!
Hence the reason this repository was created. Cheers!

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
# create an instance
from WeTransferTool import We

wet = We()
# to upload a file/folder to the server
metadata = wet.upload('/path/to/file', 'file name', 'message')
# all of wetransfer's stored parameters
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

It is very important to rememeber to use good exception handling.
If you face any rate limits, we recommend to use randomized delays in your program.

Image of our API in action is below.
Note the success but error message after.
Ensure correct exception handling in your main program that utilizes the API..
https://we.tl/t-v6MyFOgb3e
Yes - pretty ironic..but just illustrates another use of Wetransfer :)

Also if you face problems in your utilization of the api we would recommend
using other strategies such as recursive calls.
Also ensuring that methods return correct wetransfer links will help
decrease errors or exceptions.

If you have any concerns or problems, feel free to make an Issue.
Please provide relevant screenshots such that we can help troubleshoot.

Lastly, it is important to make sure that the API correctly returns
a shortened_url - if not you will surely get an error in your main
file.

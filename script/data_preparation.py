# 1 hash key and file name
HASH_WINE = "3ed56667f4b828242bd732d7d1dd7f2861e54432239d7fa63877014cbb0304d4"
FILE_WINE = "data/wine+quality.zip"

# 2 downloads and verifies both datasets
import requests
import os
import hashlib
import zipfile

# make sure directory exist
if not os.path.exists('data'):
    os.makedirs('data', exist_ok=True)

##import zipfile

# UCI Wine dataset
url01 = 'https://archive.ics.uci.edu/static/public/186/wine+quality.zip'

# get response from the download
try:
    response01 = requests.get(url01)
except:
    print("failed to connect wine+quality.zip. check url")

# download if data/wine.zip not exist
if os.path.exists(FILE_WINE) is False:
    try:
        with open(FILE_WINE, mode='wb') as f:
            f.write(response01.content)
    except:
        print("failed to download wine+quality.zip")

# get hash from the data
with open(FILE_WINE, 'rb') as f:
    data01 = f.read()
    sha256hash01 = hashlib.sha256(data01).hexdigest()

# comparing hash and send error messege
if HASH_WINE != sha256hash01:
    print("wine+quality.zip hash does not match expected hash, not matching with original file") 
else:
    print("wine+quality.zip hash matches expected hash")

# unzip dataset
with zipfile.ZipFile(FILE_WINE, mode="r") as archive:
    try:
        archive.extractall(path="data/")
        print("Unzip of wine+quality.zip complete")
    except:
        print("Unzip failed. Check dataset downloaded correctly")
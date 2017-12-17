import io
import os
import requests
import zipfile

uncondensed_data_dir = "/ifs/home/csmith2/Other/youtube_analyzer/unzip"

MIN1 = 222
MAX1 = 518
MIN2 = 80327
MAX2 = 80727

for i in range(MIN1, MAX1 + 1):
    url = "http://netsg.cs.sfu.ca/youtubedata/0{0}.zip".format(str(i))
    r = requests.get(zip_file_url)
    if r.status_code != 200:
        continue
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(uncondensed_data_dir)
    
for i in range(MIN2, MAX2 + 1):
    url = "http://netsg.cs.sfu.ca/youtubedata/0{0}.zip".format(str(i))
    r = requests.get(zip_file_url)
    if r.status_code != 200:
        continue
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(uncondensed_data_dir)

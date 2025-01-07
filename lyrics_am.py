import re
import requests
import xml.etree.ElementTree as ET

website=str(input("song url："))
nation=str(input("account nation："))
res_web = requests.get(website)
match_id = re.search(r"i=(\d+)", res_web.text)
if match_id:
    id=match_id.group(1)

headers = {
"Origin":"https://music.apple.com",
"Referer": "https://music.apple.com/",
"Authorization":"Bearer " #you need to change here
}
#to get Authorization go to console: MusicKit.getInstance().developerToken

Cookie ={
"media-user-token":""#you need to change here
}

url=str("https://amp-api.music.apple.com/v1/catalog/"+nation+"/songs/"+id+"/lyrics")

res = requests.get(url, headers=headers, cookies=Cookie)
js=res.json()
list = js['data']

ttml_string = list[0]['attributes']['ttml']
root = ET.fromstring(ttml_string)
lyrics = [p.text for p in root.findall('.//{http://www.w3.org/ns/ttml}body//{http://www.w3.org/ns/ttml}p')]
for line in lyrics:
    print(line)

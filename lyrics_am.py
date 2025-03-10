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
lyrics = []
for div in root.findall(".//{http://www.w3.org/ns/ttml}div"):
    div_lyrics = []
    for p in div.findall("{http://www.w3.org/ns/ttml}p"):
        div_lyrics.append(p.text)
    if div_lyrics:
        lyrics.append("\n".join(div_lyrics))

line = "\n\n".join(lyrics)
print(line)

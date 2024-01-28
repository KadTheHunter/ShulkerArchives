import nbtlib
import json
import re
import sys
import requests
import time
import datetime

sys.setrecursionlimit(2147483647)

def getSchems():
	r = requests.get("http://freedom-01.serv.totalfreedom.me:28966/schematic/list")
	HTML = r.content.decode("utf-8")
	r = re.findall("\/schematic\/download\?schematicName=FolfyHubKits.+?\.schem",HTML)
	newestSchem=""
	newestTime=0

	for schem in r:
		date = re.search("\d+",schem)[0]
		dt = datetime.datetime.strptime(date, '%d%m%Y')
		date=time.mktime(dt.timetuple())
		if date > newestTime:
			newestSchem=re.search("FolfyHubKits.+?\.schem",schem)[0]

	schem="http://freedom-01.serv.totalfreedom.me:28966/schematic/download?schematicName="+newestSchem
	r = requests.get(schem)
	with open("FolfyHubKits.schem", mode='wb') as file:
		file.write(r.content)
	print(newestSchem)

getSchems()

nbt_file = nbtlib.load('FolfyHubKits.schem')

blockentities = nbt_file.root["BlockEntities"]
kits = {}

def jsonTextToStr(text):
	result = ""
	string = json.loads(text)
	if "extra" in string:
		string = string["extra"]
	if type(string) == list:
		for item in string:
			result+=item["text"]
	else:
		result = string["text"]
	return re.sub("§.","",result)

for block in blockentities:
	if ("shulker_box" in block["Id"]):
		if "CustomName" in block:
			kitname=jsonTextToStr(block["CustomName"])
			print(kitname)
			kits[kitname] = "{BlockEntityTag:"+nbtlib.serialize_tag(block)+"}"

print("Found "+str(len(kits))+" shulkers. Dumping NBT..")
with open('unsorted.json', 'w',encoding="utf8") as f:
	json.dump(kits, f)

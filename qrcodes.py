import os
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import json

def GenerateQRCode():
	json_obj='{"raw_id": "2020-04-175948","id": "af13d7ae9ac37a4565a5ea4dfae4d98a740fdab4ea3b01c5b454a5c0e016e366","mfd": "2020-04-17","nonce": "5948"}'
	code=pyqrcode.create(json_obj)
	code.png('code1.png',scale=10)

	d=decode(Image.open('code1.png'))
	temp=d[0].data.decode('ascii')
	matter = json.loads(temp) 
	print(matter,matter['raw_id'])

GenerateQRCode()
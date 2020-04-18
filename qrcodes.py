import os
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import json

def GenerateQRCode(data,today,nonce):
	if not os.path.exists(today):
		os.makedirs(today)
	os.chdir("{}".format(today))
	#json_obj='{"raw_id": "2020-04-175948","id": "af13d7ae9ac37a4565a5ea4dfae4d98a740fdab4ea3b01c5b454a5c0e016e366","mfd": "2020-04-17","nonce": "5948"}'
	code=pyqrcode.create(data)
	code.png('{}.png'.format(nonce),scale=10)
	os.chdir("..")

def ReadQRCode(meta_data):
	os.chdir(meta_data['mfd'])
	filename=meta_data['nonce']+".png"
	d=decode(Image.open(filename))
	temp=d[0].data.decode('ascii')
	matter = json.loads(temp) 
	os.chdir('..')
	return(matter)

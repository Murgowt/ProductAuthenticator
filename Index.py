#Imports
from Block import BlockChain
import pickle
import datetime
import qrcodes

def LoadBlockChain():
	BC=BlockChain()
	with open("data.txt", "rb") as fp:   # Unpickling
		BC.Chain = pickle.load(fp)
	fp.close()

	#print(BC.Chain)
	l=len(BC.Chain)
	BC.block=BC.Chain[l-1]
	return(BC)



def GenerateItems():
	BC=LoadBlockChain()
	print(BC.block['timestamp'])
	today=str(datetime.date.today())
	if(today==BC.block["timestamp"]):
		print("Today's Production IDs have already been Generated.")
	else:
		BC.CreateBlock()
		for i in BC.block["items"]:
			data='{{ "merkle_root":"{}","id":"{}"}}'.format(BC.block["merkle_root"],i["id"])
			qrcodes.GenerateQRCode(str(data),today,i["nonce"])


		with open('data.txt', 'wb') as filehandle:
			pickle.dump(BC.Chain, filehandle)
		filehandle.close()
		print(BC.block["index"])




def VerifyItem():
	#Scanning QRCODE Manually in real case the qr code will be on the product
	#SO instead scanning the product we are directly scanning the qr image file.
	meta_data={
				"nonce":"8762",
				"mfd":"2020-04-19"
			 }
	data=qrcodes.ReadQRCode(meta_data)
	#data={
	#		'merkle_root': '0d6f8175e07d2254d83aa8ce52607997fae3f13145627e01cc30e5185bae19e1',
	#		 'id': '2f80860c44543dc30c93b249d1746a63a3b884efe37d889826c86637d69c9f90'
	#	 }
	BC=LoadBlockChain()
	boolean=BC.VerifyItem(BC,data)
	if(boolean):
		print("PRODUCT IS AUTHENTICATED!!!")
	else:
		print("FAKE PRODUCT ALERT!!!")












def EndProgram():
	print("Program End")
	exit()
def Initializer():
	Choice=0
	switcher={1:GenerateItems,2:VerifyItem,3:EndProgram}
	while True:
		print("\n1.Generate New Items.\n2.Verify Item.\n3.Exit.\n")
		choice=int(input("Enter Your Choice:  "))
		switcher.get(choice,"Choose a Valid Operation")()


Initializer()

#Imports
import datetime
import random
import hashlib
import pickle
#import qrcodes


#BlockChain Class Defination
class BlockChain:
	def __init__(self):
		#Right Now the Daily Production Rate is set at 20 for simplicity
		#But the code works for any large number of production rate too
		self.Chain=[]
		self.production_rate=20
		self.GenesisBlock()
		

	def GenesisBlock(self):
		self.block=	{
					"previous_hash":None,
					"timestamp":str(datetime.date.today()),
					"merkle_root":None,
					"items":[],
					"nonce":None,
					"no_of_items":0,
					"nonce_increment":1,
					"block_hash":None,
					"index":1,
				}
		self.AddItems()
		self.MerkleRoot()
		self.BlockHash()
		self.Chain.append(self.block)

	def CreateBlock(self):
		block=	{
					"previous_hash":self.block["block_hash"],
					"timestamp":str(datetime.date.today()),
					"merkle_root":None,
					"items":[],
					"nonce":None,
					"no_of_items":0,
					"nonce_increment":1,
					"block_hash":None,
					"index":self.block["index"]+1,
				}
		self.block=block
		self.Chain.append(self.block)
		self.AddItems()
		self.MerkleRoot()
		self.BlockHash()

	def AddItems(self):
		hash=hashlib.sha256()
		self.nonce=random.randint(1000,9999)
		self.block["nonce"]=self.nonce

		while(self.block["no_of_items"]<self.production_rate):

			item={
			    "raw_id":None,
				"id":None,
				"mfd":None,
				"nonce":None,
			 }

			item["mfd"]=self.block["timestamp"]
			item["raw_id"]=str(self.block["timestamp"])+str(self.nonce)
			hash.update(item["raw_id"].encode('utf-8'))
			item["id"]=hash.hexdigest()
			item["nonce"]=self.nonce
			self.block["no_of_items"]+=1
			self.nonce+=self.block["nonce_increment"]
			self.block["items"].append(item)
		
		
	def MerkleRoot(self):
		items=self.block["items"]
		temp=[]
		for i in items:
			temp.append(i["id"])
		items=temp
		temp=[]
		while(len(items)>1):
			temp=[]
			if(len(items)%2!=0):           #Adding the Duplicate of the last element if the no of elements is Odd.
				items.append(items[len(items)-1])
			for i in range(0,len(items)-1,2):
				hash=hashlib.sha256()
				hash.update(items[i].encode('utf-8'))
				hash.update(items[i+1].encode('utf-8'))
				temp.append(hash.hexdigest())
			items=temp
			
		self.block["merkle_root"]=items[0]
		

	def BlockHash(self):
		hash=hashlib.sha256()
		hash.update(self.block["merkle_root"].encode("utf-8"))
		hash.update(str(self.block["nonce"]).encode("utf-8"))
		self.block["block_hash"]=hash.hexdigest()

		#print(self.block["block_hash"])

	def VerifyItem(self,BC,data):
		temp=BC.block
		l=len(BC.Chain)-1
		while(temp['index']>1):

			if(temp['merkle_root']==data['merkle_root']):
				for item in temp['items']:
					if(item['id']==data['id']):
						return(True)
				return(False)
			else:
				l-=1
				if(temp['previous_hash']==BC.Chain[l]['block_hash']):
					temp=BC.Chain[l]
				else:
					return False
		for item in BC.Chain[0]['items']:
					if(item['id']==data['id']):
						return(True)
		return(False) 


#BC=BlockChain()
#today=str(datetime.date.today())
#for i in BC.block["items"]:
#			data='{{ "merkle_root":"{}","id":"{}"}}'.format(BC.block["merkle_root"],i["id"])
#			qrcodes.GenerateQRCode(str(data),today,i["nonce"])
#with open('data.txt', 'wb') as filehandle:
#	pickle.dump(BC.Chain, filehandle)
#filehandle.close()
#print(BC.Chain)

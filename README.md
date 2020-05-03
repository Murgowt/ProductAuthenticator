# ProductAuthenticator
BlockChain Application to Authenticate a Product. 

These Days the Shop Retailers are in a constant worry of the authenticity of the products they purchase.Is this shoe really PUMA ?? Is this shirt really GUCCI ?? So to eliminate this confusion and erradicate the production of Fake products in the market this application has been developed.

The Actual Manufacturer can  incoporate a QR-Code in his product and the ids can be stored in  a blockchain with each day's products in  a block.The shop retailer can just scan the code and the code will return a json object with the merkle root and product id which can be searched in the blockchain provided by the company,If the ID exists then the PRoduct is Authenticated else it is fake.

![image](https://user-images.githubusercontent.com/43582286/80921247-d5cdd700-8d92-11ea-94d7-09ece04b6a0e.png)

BLOCK STRUCTURE:
{
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

#Imports
from Block import BlockChain
import pickle



def LoadBlockChain():
	BC=BlockChain()
	with open("data.txt", "rb") as fp:   # Unpickling
		BC.Chain = pickle.load(fp)

	print(BC.Chain)

LoadBlockChain()
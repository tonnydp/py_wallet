import walletAPI.transaction as transaction
from sqlAPI.sql import MySQL


mysql = MySQL("../data/transaction.db")
#address = "0x909e7ccf55c48896726901d62d425d57de55dd1c"
address = "0x19dd62d228e651968e95f317f4e91bd72fd5e67e"
page_index = 1316
totalnum = 13180
while True:
	if page_index * 10 >= totalnum:
		break
	(totalnum, r_list) = transaction.getTransactionRecords(address, page_index)
	print(page_index)
	mysql.insert_transaction_records(address, r_list)
	page_index = page_index + 1
	

print("OVER!")
mysql.close_db()




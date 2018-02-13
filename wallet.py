import walletAPI.transaction as transaction
from sqlAPI.sql import MySQL


mysql = MySQL("../data/transaction.db")
#intel main
#address = "0x909e7ccf55c48896726901d62d425d57de55dd1c"


#0服充值地址
address = "0x19dd62d228e651968e95f317f4e91bd72fd5e67e"
#0服充提现地址
#address = "0xe1dd6b04fe242ec45ca0e994dfc517af672c929b"

#wkc服充值地址
#address = "0x6a4de14655825e489d97e0dc470b7e898d80e786"
#wkc提现地址
#address = "0xe1dd6b04fe242ec45ca0e994dfc517af672c929b"


page_index = 1
totalnum = page_index * 10 + 2
while True:
	if page_index * 10 >= totalnum:
		break
	(totalnum, r_list) = transaction.getTransactionRecords(address, page_index)
	print(page_index)
	mysql.insert_transaction_records(address, r_list)
	page_index = page_index + 1
	

print("OVER!")
mysql.close_db()




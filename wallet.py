import transaction


url = "https://walletapi.onethingpcs.com"
headers = {'Content-Type':'application/json'}

address = "0x909e7ccf55c48896726901d62d425d57de55dd1c"
#address = "0x19dd62d228e651968e95f317f4e91bd72fd5e67e"
page_index = 1
count = 1
while True:
	(totalnum, r_list) = transaction.getTransactionRecords(url, address, page_index)

	for rc in r_list:
		print(rc)
		count = count + 1
	page_index = page_index + 1
	if page_index * 10 >= totalnum:
		break

print(page_index)




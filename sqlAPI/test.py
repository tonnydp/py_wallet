import sqlite3
import collections
import decimal

def sortDict(adict):
	keys = adict.keys()
	k_list = []
	for k in keys:
		k_list.append(k)
	k_list.sort()
	print(k_list)
	new_list = []
	for k in k_list:
		new_list.append((k, adict[k][0], adict[k][1]))
	return new_list


con = sqlite3.connect("../../data/transaction.db")
cur = con.cursor()
addr_dict = {}
addr_dict["in0"] = "0x19dd62d228e651968e95f317f4e91bd72fd5e67e"
addr_dict["inwkc"] = "0x6a4de14655825e489d97e0dc470b7e898d80e786"
addr_dict["out"] = "0xe1dd6b04fe242ec45ca0e994dfc517af672c929b"
for key in addr_dict:
	file = open("%s.csv" % (key), 'w')
	if "out" in key:
		result = cur.execute("SELECT * FROM Records WHERE from_address=?", (addr_dict[key], ))
	else:
		result = cur.execute("SELECT * FROM Records WHERE to_address=?", (addr_dict[key], ))
	time_amount_dict = {}
	for r in result.fetchall():
		r_date = r[3][0:10]
		if r_date not in time_amount_dict:
			time_amount_dict[r_date] = (decimal.Decimal(r[4]), 1)
		else:
			time_amount_dict[r_date] = (time_amount_dict[r_date][0] + decimal.Decimal(r[4]), time_amount_dict[r_date][1] + 1)
	data_list = sortDict(time_amount_dict)
	for t in data_list:
		(k, amount, count) = t

		file.write("%s\t%s\t%d\n" % (k, float(amount), count))
	file.close()

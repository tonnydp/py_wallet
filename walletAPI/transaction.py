import requests
import json
import time
import struct
from decimal import *
import math 

def getTransactionRecords(url, address, page_index):
	method = "getTransactionRecords"
	url = "%s/%s" % (url, method)
	data = [address, "0", "0", str(page_index), "10"]
	r = requests.post(url, data=json.dumps(data), headers=headers)
	rps_dict = json.loads(r.text)
	totalnum = int(rps_dict["totalnum"])
	record_list = []
	for rc in rps_dict["result"]:
		rc["timestamp"] = timeConvert(rc["timestamp"])
		rc["amount"] = amountConvert(rc["amount"])
		rc["cost"] = amountConvert(rc["cost"])
		record_list.append(rc)
	return (totalnum, record_list)

def getTrasactionCount(url, address):
	method = "eth_getTransactionCount"
	data = {
		"jsonrpc": "2.0",
		"method": method,
		"params": [address, "pending"],
		"id": 1
		}
	r = requests.post(url, data=json.dumps(data), headers=headers)
	response_json = r.text
	rps_dict = json.loads(response_json)
	num = int(rps_dict["result"], 16)
	return num

def amountConvert(amount_str):
	amount_hex = amount_str.replace("0x", "")
	return int(amount_hex, 16) / 1000000000000000000

def timeConvert(timestamp):
	time_local = time.localtime(int(timestamp))
	return time.strftime("%Y-%m-%d %H:%M:%S", time_local)
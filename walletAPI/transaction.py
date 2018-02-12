import requests
import json
import time
import struct
from decimal import *
import math 

url = "https://walletapi.onethingpcs.com"
headers = {'Content-Type':'application/json'}

def getTransactionRecords(address, page_index):
	method = "getTransactionRecords"
	new_url = "%s/%s" % (url, method)
	data = [address, "0", "0", str(page_index), "10"]
	rps_dict = makeRequest(new_url, data, headers)
	while "totalnum" not in rps_dict or "result" not in rps_dict:
		print(rps_dict)
		print("SLEEP 5 SEC...")
		time.sleep(5)
		rps_dict = makeRequest(new_url, data, headers)

	totalnum = int(rps_dict["totalnum"])
	record_list = []
	for rc in rps_dict["result"]:
		rc["timestamp"] = timeConvert(rc["timestamp"])
		rc["amount"] = amountConvert(rc["amount"])
		rc["cost"] = amountConvert(rc["cost"])
		record_list.append(rc)
	return (totalnum, record_list)

def getTrasactionCount(address):
	method = "eth_getTransactionCount"
	data = {
		"jsonrpc": "2.0",
		"method": method,
		"params": [address, "pending"],
		"id": 1
		}
	rps_dict = makeRequest(url, data, headers)
	num = int(rps_dict["result"], 16)
	return num

def makeRequest(url, data, headers):
	while True:
		try:
			r = requests.post(url, data=json.dumps(data), headers=headers)
			rps_dict = json.loads(r.text)
			return rps_dict
		except Exception as e:
			print(e)
			print("Wait for Network Recover...")
			time.sleep(10)

def amountConvert(amount_str):
	amount_hex = amount_str.replace("0x", "")
	return int(amount_hex, 16) / 1000000000000000000

def timeConvert(timestamp):
	time_local = time.localtime(int(timestamp))
	return time.strftime("%Y-%m-%d %H:%M:%S", time_local)
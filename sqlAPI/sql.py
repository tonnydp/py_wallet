import sqlite3 as sql


class MySQL:
	con = None
	cur = None
	def __init__(self, path):
		self.con = sql.connect(path)
		self.cur = self.con.cursor()

		create_transaction_tb_statement = '''
	        CREATE TABLE IF NOT EXISTS Records 
			 (hash TEXT PRIMARY KEY,
			from_address TEXT,
			to_address TEXT,
			create_time TEXT,
			amount TEXT,
			cost TEXT,
			order_id TEXT);
        '''  
		self.cur.execute(create_transaction_tb_statement)


	def insert_transaction_records(self, address, r_list):
		for r in r_list:
			if int(r["type"]) == 0:
				f_addr = address
				t_addr = r["tradeAccount"]
			else:
				f_addr = r["tradeAccount"]
				t_addr = address 
			try:
				self.cur.execute("INSERT INTO Records VALUES(?, ?, ?, ?, ?, ?, ?);", (r["hash"], f_addr, t_addr,r["timestamp"], str(r["amount"]), str(r["cost"]), r["order_id"]))
			except sql.IntegrityError as e:
				print("Got One Same Hash. Continued!")
				continue
		self.con.commit()

	def close_db(self):
		self.cur.close()
		self.con.close()

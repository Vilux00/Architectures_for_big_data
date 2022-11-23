from Wrappers import OperationalDBWrapper, HistoricalDBWrapper

def BatchDU(host_from, db_from, user_from, password_from, host_to, db_to, user_to, password_to,
			table_from, table_to, start_ts=None, end_ts=None):
	'''Store data related to a time interval from the operational database to the historical one'''
	o_db = OperationalDBWrapper()
	h_db = HistoricalDBWrapper()

	o_conn = o_db.conn(host_from, db_from, user_from, password_from)
	h_conn = h_db.conn(host_to, db_to, user_to, password_to)

	for row in o_db.select(o_conn, table_from, start_ts=start_ts, end_ts=end_ts):
		h_db.insert(table_to, row)

	o_db.close()
	h_db.close()

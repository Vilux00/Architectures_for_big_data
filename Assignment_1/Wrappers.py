class OperationalDBWrapper():
	'''This class wraps the operational database. It provides primitives to connect, close the connection and extract data'''

	def conn(self, host, database, user, password):
		'''Connect to the operational database with the credentials specified'''
		pass

	def select(self, conn, table, start_ts=None, end_ts=None):
		'''Select data related to a time interval from the table, the data are ordered by timestamp and returned one row at a time.
        If no timestamp is provided, the procedure returns all the rows in the table.
        If the start_ts is the only timestamp provided, the procedure returns all the rows with timestamp >= start_ts.
        If the end_ts is the only timestamp provided, the procedure returns all the rows with timestamp <= end_ts'''
		pass

	def close(self, conn):
		'''Close the connection with the database'''
		pass

	def log(self, op, file):
		'''Log the operation executed in the file'''
		pass


class HistoricalDBWrapper():
	'''This class wraps the historical database providing r/w functionalities'''
	
	def conn(self, host, database, user, password):
		'''Connect to the historical database with the credentials specified'''
		pass

	def insert(self, table, data):
		'''Insert data in a specific table, data must be a list of tuples'''
		pass

	def select(self, table, columns=None, start_ts=None, end_ts=None):
		'''Select data from a table, projecting only the specified columns. 
        If no timestamp is provided all the rows are returned. 
        If only start_ts is provided, all the rows with timestamp >= start_ts are returned.
        If only end_ts is provided, all the rows with timestamp <= end_ts are returned.
        If no column is provided, the procedure returns the full rows'''
		pass

	def close(self, conn):
		'''Close the connection with the database'''
		pass

	def log(self, op, file):
		'''Log the operation executed in the file'''
		pass

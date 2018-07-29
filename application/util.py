from datetime import datetime

def get_time():
	now = datetime.utcnow()
	return now.strftime("%Y-%m-%d %H:%M:%S")
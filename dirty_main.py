from application.salary import *
from application.people import *
import datetime



LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

def getIsoTime():
	return datetime.datetime.now(tz=LOCAL_TIMEZONE).isoformat()

if __name__ == '__main__':
	print(f"Time: {getIsoTime()} ({LOCAL_TIMEZONE})")
	calculate_salary()
	get_employees()
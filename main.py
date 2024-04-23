import application.salary as slr
import application.people as ppl
import datetime


LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

def getIsoTime():
	return datetime.datetime.now(tz=LOCAL_TIMEZONE).isoformat()

if __name__ == '__main__':
	print(f"Time: {getIsoTime()} ({LOCAL_TIMEZONE})")
	slr.calculate_salary()
	ppl.get_employees()
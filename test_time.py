import pytz
from datetime import datetime

now = datetime.now(pytz.timezone("US/Pacific"))

dtime_str = now.strftime("%Y%m%d_%H:%M")

print(dtime_str)
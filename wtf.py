from datetime import datetime

d = datetime.now()

print(type(d.strftime("%Y-%m-%d %H:%M:%S")))
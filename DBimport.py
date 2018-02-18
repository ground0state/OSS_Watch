from datetime import *
from dateutil import tz
import Scraping as sc
from django.db import IntegrityError

import sys
import os
import django

sys.path.append("C:\oss_project")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","oss_project.settings")

django.setup()
from info.models import *

for list in sc.apachehttpd_scraping():
	oss_id = 1
	version = list[0]
	released = list[1]
	now = datetime.now().replace(tzinfo=tz.tzlocal())
	registrated = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
	try:
		Info.objects.create(oss_id=oss_id, version=version, released=released, registrated=registrated)
	except IntegrityError:
		pass
	
for list in sc.apachetomcat_scraping():
	oss_id = 2
	version = list[0]
	released = list[1]
	now = datetime.now().replace(tzinfo=tz.tzlocal())
	registrated = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
	try:
		Info.objects.create(oss_id=oss_id, version=version, released=released, registrated=registrated)
	except IntegrityError:
		pass
	
	
for list in sc.openssl_scraping():
	oss_id = 3
	version = list[0]
	released = list[1]
	now = datetime.now().replace(tzinfo=tz.tzlocal())
	registrated = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
	try:
		Info.objects.create(oss_id=oss_id, version=version, released=released, registrated=registrated)
	except IntegrityError:
		pass
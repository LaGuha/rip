from base_client import BaseClient
from collections import Counter
import requests
import json
class MyClass(BaseClient):
	BASE_URL='https://api.vk.com/method/'
	def _get_data(self,method,http_method):
		return requests.get(self.generate_url(method))

	def __init__(self,method):
		self.method=method

def age(day, month, year):
	day=int(day)
	month=int(month)
	year=int(year)
	c_d=29
	c_m=9
	c_y=2016
	age=c_y-year
	if c_m<month:
		age+=1
	elif c_m==month and c_d<day:
		age+=1
	return age

obj=MyClass('friends.get?user_id=84379252&fields=bdate&v=5.56')
r=obj.execute()
friends=r.json()
friends=friends['response']
friends=friends['items']
years=[]
for friend in friends:
	if friend.get('bdate'):
		date=friend['bdate'].split('.')
		if len(date)==3:
			old=age(date[0],date[1],date[2])
			years.append(old)
old=Counter(years)
keys=old.keys()
keys=list(keys)
keys.sort()
for i in keys:
	print (i,':','#'*old[i])
import urlib2
import json


url = 'https://api.foursquare.com//v2/venues/search?v=20131016&ll=%20-33.8567%2C%20%20151.1931&intent=checkin&oauth_token=FWG1RZTWFOYPREF5Z02TB0ZBD3XEGSMTDEVEOA4R2LSHSF0'

obj = urllib2.urlopen(url)

data = json.load(obj)

for abc in data['response']['venues']:
	print abc['name']
	try:
		print 'phone = ' + abc['contact']['phone']
	except Exception:
		pass
	print abc['name']
	try:
		print 'twitter = '+ abc['contact']['twitter']
	except Exception:
		pass
	try:
		print 'city = '+ abc['location']['city']
	except Exception:
		pass
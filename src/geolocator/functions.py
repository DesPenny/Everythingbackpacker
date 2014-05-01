import urllib2
import json

from geopy import geocoders

def find_city_lat_lng(laT, lnG):
	g = geocoders.GoogleV3()
	find = "%s %s" %(laT, lnG)
	place, (lat, lng) = g.geocode(find)
	full_address = place.split(', ')
	city = full_address[1]
	return str(city)

def locu_search(query):
	api = '3a35727e3f8d1f531474a2453f4c6ec5b724301f'
	url ='https://api.locu.com/v1_0/venue/search/?'
	local = query
	locality = local.replace(' ', '%20')
	new_url = url + 'api_key=' + api + '&locality=' + locality
	obj = urllib2.urlopen(new_url)
	data = json.load(obj)

	locations = []
	for abc in data['objects']:
		item_list = [abc['name'],abc['id']]
		locations.append(item_list)

	return locations

def locu_details(locu_id):
	api = ' 3a35727e3f8d1f531474a2453f4c6ec5b724301f'
	url = 'https://api.locu.com/v1_0/venue/'
	new_url = url + str(locu_id) +'/?api_key=' + api

	obj = urllib2.urlopen(new_url)
	data = json.load(obj)

	details = []
	for abc in data['objects']:
		
		details.append(abc['lat'])
		details.append(abc['long'])
		

	return details

def find_place(query):
	g = geocoders.GoogleV3()
	place, (lat, lng) = g.geocode(query)
	return place




def foursquare_search(query):
	token = 'FWG1RZTWFOYPREF5Z02TB0ZBD3XEGSMTDEVEOA4R2LSHSF0'
	place, lat, lng = find_place(query)

	latlng = 'll=' + str(lat) + '%2C%20%' + str(lng)
	

	url = 'https://api.foursquare.com//v2/venues/search?v=20131016&' + latlng + '&intent=checkin&oauth_token='
	full_url = url + token

	obj = urllib2.urlopen(full_url)

	data = json.load(obj)

	locations = []

	for abc in data['response']['venues']:
		print abc['name']
		locations.append([abc['name'], abc['id']])
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

	return locations

def foursquare_details(four_id):
	token = 'FWG1RZTWFOYPREF5Z02TB0ZBD3XEGSMTDEVEOA4R2LSHSF0'
	
	four = str(four_id)
	url = 'https://api.foursquare.com//v2/venues/' + four +'?v=20131016&' + '&oauth_token='
	full_url = url + token

	obj = urllib2.urlopen(full_url)

	data = json.load(obj)

	details = []
	details.append(data['response']['venue']['location']['lat'])
	details.append(data['response']['venue']['location']['lng'])

		

	return details
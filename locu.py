import urlib2
import json




api = ' 3a35727e3f8d1f531474a2453f4c6ec5b724301f'

url ='https://api.locu.com/v1_0/venue/search/?'

local = 'balmain east'

locality = local.replace(' ', '%20')

new_url = url + 'api_key=' + api + '&locality=' + locality


obj = urllib2.urlopen(new_url)

data = json.load(obj)


for abc in data['objects']:
	print abc['name']



menu_url = 'https://api.locu.com/v1_0/venue/search/?locality=Balmain®ion=NSW&postal_code=2041&api_key=3a35727e3f8d1f531474a2453f4c6ec5b724301f'

menu_obj = urllib2.urlopen(menu_url)

data2 = json.load(menu_obj)

for abc2 in data2['objects']:
	print abc2['name'] + 'at '+ abc2['venue']['name']
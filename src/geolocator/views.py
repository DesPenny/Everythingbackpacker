from django.shortcuts import render_to_response, RequestContext
from locations.models import Location
from .functions import locu_search, foursquare_search, find_city_lat_lng




def happyhour(request):
	if request.method == 'POST':
		print request.POST
		oldquery = request.POST['search']
		lat = request.POST['lat']
		lng = request.POST['lng']
		print lat, lng
		query = find_city_lat_lng(lat,lng)
		
		locations = locu_search(query)
		for loc in locations:
			name, locu_id = loc[0], loc[1]
			new_location, created = Location.objects.get_or_create(name=name, locu_id=locu_id)
			if created:
				
				print "Created new id for %s with id of %s" %(name, locu_id)
		'''
		locations = foursquare_search(query)
		for loc in locations:
			name, four_id = loc[0], loc[1]
			new_location, created = Location.objects.get_or_create(name=name, four_id=four_id)
			if created:
				
				print "Created new id for %s with id of %s" %(name, four_id)
				'''
	return render_to_response('happyhour/happyhour.html', locals(), context_instance=RequestContext(request))
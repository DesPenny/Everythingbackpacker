from django.shortcuts import render_to_response, RequestContext
from geolocator.functions import locu_details

from .models import Location


def single_location(request, id):

	try:
		location = Location.objects.get(locu_id=id)
		locu = True
		foursquare = False
	except Location.DoesNotExist:
		location = Location.objects.get(four_id=id)
		foursquare = True
		locu = False
	except:
		location = 'This location cannot be found'
		locu = False
		foursquare = False
	if locu:
		details = locu_details(location)

	elif foursquare:
		details = Location.objects.all()

	else:
		pass



	return render_to_response('locations/single.html', locals(), context_instance=RequestContext(request))

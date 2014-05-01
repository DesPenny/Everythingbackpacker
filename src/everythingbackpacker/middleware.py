
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect


URLS = [reverse(url) for url in settings.SUBSCRIPTION_REQUIRED_URLS]

class CheckMembership():
	def process_request(self, request):
		if request.user.is_authenticated():
			#messages.success(request, 'User is logged in')
			if request.path in URLS:
				
				role = request.user.userrole
				
				if str(role) != "Staff":
					messages.success(request, 'Membership upgrade required to go there.')
					return HttpResponseRedirect('/')
		#code here
		else:
			messages.error(request, 'user is not logged in')
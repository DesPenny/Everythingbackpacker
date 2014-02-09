from django.contrib import admin

from .models import DirectMessages

class DirectMessageAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "id"]
	class Meta:
		model = DirectMessages

admin.site.register(DirectMessages, DirectMessageAdmin)
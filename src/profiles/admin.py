from django.contrib import admin

from .models import Address, Job, UserPicture, UserRole, UserStripe

class UserStripeAdmin(admin.ModelAdmin):
	class Meta:
		model = UserStripe

admin.site.register(UserStripe, UserStripeAdmin)

class AddressAdmin(admin.ModelAdmin):
	class Meta:
		model = Address

admin.site.register(Address, AddressAdmin)

class JobAdmin(admin.ModelAdmin):
	class Meta:
		model = Job

admin.site.register(Job, JobAdmin)

class UserPictureAdmin(admin.ModelAdmin):
	class Meta:
		model = UserPicture

admin.site.register(UserPicture, JobAdmin)

class UserRoleAdmin(admin.ModelAdmin):
	class Meta:
		model = UserRole

admin.site.register(UserRole, UserRoleAdmin)
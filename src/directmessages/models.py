from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.core.urlresolvers import reverse
# Create your models here.


class DirectMessagesManager(models.Manager):
	def get_num_unread_messages(self, user):
		return super(DirectMessagesManager, self).filter(read=False).filter(receiver=user).count()

class DirectMessages(models.Model):
	subject = models.CharField(max_length=150)
	body = models.CharField(max_length=3000)
	sender = models.ForeignKey(User, related_name='sent_direct_messages', null=True, blank=True)
	receiver = models.ForeignKey(User, related_name='received_direct_messages', null=True, blank=True)
	sent = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
	read = models.BooleanField(default=False)
	read_at = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
	parent = models.ForeignKey('self', related_name='parent_message', null=True, blank=True)
	replied = models.BooleanField(default=False)



	def __unicode__(self):
		return self.subject

	objects =DirectMessagesManager()


	def get_absolute_url(self):
		return (reverse('view_direct_message', kwargs={'dm_id': self.id}))

	class Meta:
		ordering = ['-sent',]


# shows how many messages we have

def set_messages_in_session(sender, user, request, **kwargs):
	direct_messages = DirectMessages.objects.get_num_unread_messages(user)
	request.session['num_of_messages'] = direct_messages

user_logged_in.connect(set_messages_in_session)

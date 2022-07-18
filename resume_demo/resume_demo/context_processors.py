from django.contrib.auth.models import User

def project_context(request):

	return {
		'me': User.objects.first(),
	}
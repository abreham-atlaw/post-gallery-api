from django.conf import settings
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response



class SendEmailView(APIView):
    
	def post(self, request: Request) -> Response:
		
		send_mail(
			subject=request.data.get("subject"),
			message=request.data.get("message"),
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[
				request.data.get("to")
			],
			fail_silently=False
		)
		return Response("", 200)


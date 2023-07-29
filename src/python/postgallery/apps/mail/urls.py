from django.urls import path

from apps.mail.views import SendEmailView


urlpatterns = [
    path("send-mail/", SendEmailView.as_view(), name="send-email"),
]

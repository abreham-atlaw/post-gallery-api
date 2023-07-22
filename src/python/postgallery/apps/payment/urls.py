
from django.urls import path

from apps.payment.views import ChapaPaymentView, ChapaVerifyView



urlpatterns = [
    path("chapa/pay/", ChapaPaymentView.as_view(), name="chapa-pay"),
    path("chapa/verify/", ChapaVerifyView.as_view(), name="chapa-verify")
]
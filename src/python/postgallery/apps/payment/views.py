import uuid

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from apps.payment.di import PaymentProviders
from apps.payment.serializers import ChapaPaymentSerializer


class ChapaPaymentView(APIView):
    
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__chapa = PaymentProviders.provideChapaClient()

	def __generate_transaction_id(self) -> str:
		return uuid.uuid4().hex

	def post(self, request: Request) -> Response:
		serializer = ChapaPaymentSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		data = serializer.validated_data

		transaction_id = self.__generate_transaction_id()
		data['tx_ref'] = transaction_id


		response = self.__chapa.initialize(**data)
		return Response({
			"checkout_url": response.data.checkout_url,
			"tx_ref": transaction_id
		}, 200)


class ChapaVerifyView(APIView):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.__chapa = PaymentProviders.provideChapaClient()
	
	def get(self, request: Request): 
		transaction_id = request.query_params.get("tx_ref")

		response = self.__chapa.verify(transaction_id)
		return Response(
			{
				"is_paid": response.status == "success"
			}
		)
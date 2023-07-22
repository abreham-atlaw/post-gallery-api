from chapa import Chapa

from postgallery.settings import CHAPPA_API_KEY


class PaymentProviders:
    
	@staticmethod
	def provideChapaClient() -> Chapa:
		return Chapa(CHAPPA_API_KEY, response_format='obj')
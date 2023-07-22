from rest_framework import serializers


"""
data = {
    'email': 'abebe@bikila.com',
    'amount': 1000,
    'first_name': 'Abebe',
    'last_name': 'Bikila',
    'tx_ref': '<your-unique-transaction-id>',
    # optional
    'callback_url': 'https://www.your-site.com/callback',
    'customization': {
        'title': '<Your-Company>',
        'description': 'Payment for your services',
    }
}


"""

class ChapaPaymentSerializer(serializers.Serializer):
    
	email = serializers.EmailField()
	amount = serializers.FloatField()
	first_name = serializers.CharField()
	last_name = serializers.CharField()
	return_url = serializers.URLField()

from decimal import Decimal
from django.test import TestCase
from django.conf import settings
from ..models import Currency
from ..utils import calculate_price



class UtilsTest(TestCase):
	fixtures = ['test_data.json']
	use_transaction = False
	
	def test_calculate_price_success(self):
		res = calculate_price('10', 'USD')
		self.assertEqual(res, Decimal('15.00'))

	def test_calculate_price_fail(self):
		res = calculate_price('10', 'GBP')
		self.assertEqual(res, Decimal('0.00'))
	
	def test_calculate_price_currency_doesnotexist(self):
		settings.DEBUG = True
		self.assertRaises(Currency.DoesNotExist, calculate_price, '10', 'GBP')
		settings.DEBUG = False


# coding=utf-8
from unittest import TestCase
from brcode.static import fromJson


class TestDynamicfromJson(TestCase):

    def test_success(self):
        json = {
            "key": "arya@stark.com",
            "amount": 12500,
            "name": "Arya Stark",
            "city": "São Paulo",
            "txid": "1297364819273409"
        }
        actualBrcode = fromJson(json)
        expectedBrcode = "00020126360014br.gov.bcb.pix0114arya@stark.com5204000053039865406125.005802BR5910Arya Stark6009Sao Paulo622005161297364819273409630440F2"
        self.assertEqual(actualBrcode, expectedBrcode)

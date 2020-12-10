# coding=utf-8
from unittest import TestCase
from brcode.static import fromJson


class TestStaticfromJson(TestCase):

    def test_success(self):
        json = {
            "key": "arya@stark.com",
            "amount": 12500,
            "name": "Arya Stark with a very long name",
            "city": "Pindamonhangaba do Norte do Sul de Winterfell",
            "txid": "verylongreconciliationidtotestfieldlength"
        }
        actualBrcode = fromJson(json)
        expectedBrcode = "00020126360014br.gov.bcb.pix0114arya@stark.com5204000053039865406125.005802BR5925Arya Stark with a very lo6015Pindamonhangaba62290525verylongreconciliationidt630405B7"
        self.assertEqual(expectedBrcode, actualBrcode)

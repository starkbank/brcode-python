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

    def test_withdraw_success(self):
        json = {
            "key": "4004901d-bd85-4769-8e52-cb4c42c506dc",
            "amount": 58205,
            "name": "Pix",
            "city": "BRASILIA",
            "txid": "87ea69f3ce744ce19d90787f1",
            "cashierBankCode": "99999008",
            "description": "Jornada pagador 85176"
        }
        actualBrcode = fromJson(json)
        expectedBrcode = "00020126950014br.gov.bcb.pix01364004901d-bd85-4769-8e52-cb4c42c506dc0221Jornada pagador 851760308999990085204000053039865406582.055802BR5903Pix6008BRASILIA6229052587ea69f3ce744ce19d90787f16304A76D"
        self.assertEqual(expectedBrcode, actualBrcode)

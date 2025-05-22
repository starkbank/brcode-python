# coding=utf-8
from unittest import TestCase
from brcode.dynamic import fromJson


class TestDynamicfromJson(TestCase):

    def test_success(self):
        json = {
            "name": "Arya Stark with a very long name",
            "city": "Pindamonhangaba do Norte do Sul de Winterfell",
            "txid": "5656565656565656",
            "url": "invoice.starkbank.com/f5333103-3279-4db2-8389-5efe335ba93d"
        }
        actualBrcode = fromJson(json)
        expectedBrcode = "00020101021226800014br.gov.bcb.pix2558invoice.starkbank.com/f5333103-3279-4db2-8389-5efe335ba93d5204000053039865802BR5925Arya Stark with a very lo6015Pindamonhangaba622005165656565656565656630435F6"
        self.assertEqual(actualBrcode, expectedBrcode)



    def test_success_with_subscription_url(self):
        json = {
            "name": "Arya Stark with a very long name",
            "city": "Pindamonhangaba do Norte do Sul de Winterfell",
            "txid": "5656565656565656",
            "url": "invoice.starkbank.com/f5333103-3279-4db2-8389-5efe335ba93d",
            "subscriptionUrl": "invoice.starkbank.com/subs/f5333103-3279-4db2-8389-5efe335ba93d"
        }
        actualBrcode = fromJson(json)
        expectedBrcode = "00020101021226800014br.gov.bcb.pix2558invoice.starkbank.com/f5333103-3279-4db2-8389-5efe335ba93d5204000053039865802BR5925Arya Stark with a very lo6015Pindamonhangaba62200516565656565656565680850014br.gov.bcb.pix2563invoice.starkbank.com/subs/f5333103-3279-4db2-8389-5efe335ba93d6304C5CB"
        self.assertEqual(actualBrcode, expectedBrcode)
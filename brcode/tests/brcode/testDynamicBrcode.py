# coding=utf-8
from unittest import TestCase
from brcode.dynamic import fromJson


class TestDynamicfromJson(TestCase):

    def test_success(self):
        json = {
            "name": "Arya Stark",
            "city": "São Paulo",
            "txid": "5656565656565656",
            "url": "invoice.starkbank.com/f5333103-3279-4db2-8389-5efe335ba93d"
        }
        actualBrcode = fromJson(json)
        expectedBrcode = "00020101021226800014br.gov.bcb.pix2558invoice.starkbank.com/f5333103-3279-4db2-8389-5efe335ba93d5204000053039865802BR5910Arya Stark6009Sao Paulo6220051656565656565656566304A56D"
        self.assertEqual(actualBrcode, expectedBrcode)
from json import dumps
from unittest import TestCase
from brcode.utils.brcodeId import jsonFromBrcode, brcodeJsonToBrcode

brcode = "00020126360014br.gov.bcb.pix0114arya@stark.com5204000053039865406125.005802BR5925Arya Stark with a very lo6009Sao Paulo62290525verylongreconciliationidt630466F4"


class TestJsonFromBrcode(TestCase):

    def test_success(self):
        json = jsonFromBrcode(brcode)
        json.pop("63")
        print(dumps(json, indent=4))
        self.assertEqual(brcode, brcodeJsonToBrcode(json))
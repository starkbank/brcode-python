from unittest import TestCase
from brcode.utils.brcodeId import jsonFromBrcode, brcodeJsonToBrcode

brcode = "00020101021226790014br.gov.bcb.pix2557invoice.starkbank.com/v2/6b8a8cb04b0b4068813416aa7b76df435204000053039865802BR5915Stark Bank S.A.6009Sao Paulo62070503***6304D491"


class TestJsonFromBrcode(TestCase):

    def test_success(self):
        json = jsonFromBrcode(brcode)
        json.pop("63")
        self.assertEqual(brcode, brcodeJsonToBrcode(json))
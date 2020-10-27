from brcode.utils.brcodeId import brcodeJsonToBrcode
from brcode.utils.brcodeJson import dynamicJsonToBrcodeJson


def fromJson(json):
    return brcodeJsonToBrcode(dynamicJsonToBrcodeJson(json))

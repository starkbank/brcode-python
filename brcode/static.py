from brcode.utils.brcodeId import brcodeJsonToBrcode
from brcode.utils.brcodeJson import staticJsonToBrcodeJson


def fromJson(json):
    return brcodeJsonToBrcode(staticJsonToBrcodeJson(json))

from brcode.utils.enum import Enum


class BrcodeJsonKey(Enum):

    payloadFormatIndicator = "00"
    pointOfInitiationMethod = "01"
    merchantAccountInformationCards = "04"
    merchantAccountInformationPix = "26"
    merchantCategoryCode = "52"
    transactionCurrency = "53"
    transactionAmount = "54"
    countryCode = "58"
    merchantName = "59"
    merchantCity = "60"
    postalCode = "61"
    additionalData = "62"
    crc16 = "63"

    @classmethod
    def merchantAccountInformations(cls):
        return [str(i).zfill(2) for i in range(26, 52)]

    @classmethod
    def unreservedTemplates(cls):
        return [str(i).zfill(2) for i in range(80, 100)]


class BrcodeJsonSubKey(Enum):

    merchantAccountGui = "00"
    merchantAccountDictKey = "01"
    merchantAccountInfo = "02"
    cashierBankCode = "03"
    unreservedTemplateGUI = "00"
    additionalDataReferenceLabel = "05"
    merchantAccountUrl = "25"


def staticJsonToBrcodeJson(brcode):
    json = {
        BrcodeJsonKey.payloadFormatIndicator: "01",
        BrcodeJsonKey.merchantAccountInformationPix: {
            BrcodeJsonSubKey.merchantAccountGui: "br.gov.bcb.pix",
            BrcodeJsonSubKey.merchantAccountDictKey: brcode["key"],
        },
        BrcodeJsonKey.merchantCategoryCode: brcode.get("mcc", "")[:4] or "0000",
        BrcodeJsonKey.transactionCurrency: "986",
        BrcodeJsonKey.countryCode: "BR",
        BrcodeJsonKey.merchantName: brcode["name"][:25],
        BrcodeJsonKey.merchantCity: brcode["city"][:15],
        BrcodeJsonKey.additionalData: {
            BrcodeJsonSubKey.additionalDataReferenceLabel: brcode["txid"][:25] or "***",
        },
    }
    if brcode.get("amount"):
        json[BrcodeJsonKey.transactionAmount] = "{:.2f}".format(brcode["amount"] / 100.0)
    if brcode.get("cashierBankCode"):
        json[BrcodeJsonKey.merchantAccountInformationPix].update({
            BrcodeJsonSubKey.cashierBankCode: brcode.get("cashierBankCode")
        })
    if brcode.get("description"):
        json[BrcodeJsonKey.merchantAccountInformationPix].update({
            BrcodeJsonSubKey.merchantAccountInfo: brcode.get("description")
        })
    return json


def dynamicJsonToBrcodeJson(brcode):
    json = {
        BrcodeJsonKey.payloadFormatIndicator: "01",
        BrcodeJsonKey.pointOfInitiationMethod: "12",
        BrcodeJsonKey.merchantAccountInformationPix: {
            BrcodeJsonSubKey.merchantAccountGui: "br.gov.bcb.pix",
            BrcodeJsonSubKey.merchantAccountUrl: brcode["url"],
        },
        BrcodeJsonKey.merchantCategoryCode: brcode.get("mcc", "")[:4] or "0000",
        BrcodeJsonKey.transactionCurrency: "986",
        BrcodeJsonKey.countryCode: "BR",
        BrcodeJsonKey.merchantName: brcode["name"][:25],
        BrcodeJsonKey.merchantCity: brcode["city"][:15],
        BrcodeJsonKey.additionalData: {
            BrcodeJsonSubKey.additionalDataReferenceLabel: brcode["txid"][:25] or "***",
        }
    }
    if brcode.get("amount"):
        json[BrcodeJsonKey.transactionAmount] = "{:.2f}".format(brcode["amount"] / 100.0)
    return json

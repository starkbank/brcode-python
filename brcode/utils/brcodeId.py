from brcode.utils.accents import Accents
from brcode.utils.brcodeJson import BrcodeJsonKey

_recursiveRange = [BrcodeJsonKey.additionalData] + BrcodeJsonKey.merchantAccountInformations() + BrcodeJsonKey.unreservedTemplates()
_maxCharacters = 512


def jsonFromBrcode(brcode, _level=1):
    json = {}
    if len(brcode.encode("utf8")) > _maxCharacters:
        raise ValueError("more than {max} bytes".format(max=_maxCharacters))
    if _level == 1 and _calculateCrc16(brcode[:-4]) != brcode[-4:]:
        raise ValueError(
            "CRC16 mismatch: expected {expected}, got {actual}".format(
                expected=_calculateCrc16(brcode[:-4]),
                actual=brcode[-4:],
            )
        )
    if _level > 10:
        raise ValueError("too many levels")
    while brcode:
        key, length, brcode = brcode[0:2], int(brcode[2:4]), brcode[4:]
        value, brcode = brcode[0:length], brcode[length:]
        if len(value) != length:
            raise ValueError("length mismatch: {actual} != {expected}".format(actual=len(value), expected=length))
        if _level == 1 and key in _recursiveRange:
            value = jsonFromBrcode(value, _level=_level + 1)
        json[key] = value
    return json


def brcodeJsonToBrcode(json):
    string = _buildIdSegment(json)
    string += BrcodeJsonKey.crc16 + "04"
    return string + _calculateCrc16(string)


def _buildIdSegment(brcodeElement):
    if not isinstance(brcodeElement, dict):
        return Accents.remove(brcodeElement)

    string = ""
    for key, value in sorted(brcodeElement.items()):
        value = _buildIdSegment(value)
        length = len(value)
        string += str(key).zfill(2) + str(length).zfill(2) + value
    return string


def _calculateCrc16(data):
    crc = 0xFFFF
    polynomial = 0x1021

    for byte in bytearray(data, encoding="utf-8"):
        for i in range(0, 8):
            bit = (byte >> (7 - i)) & 1
            c15 = (crc >> 15) & 1
            crc <<= 1
            if c15 ^ bit:
                crc ^= polynomial
    crc16 = hex(crc & 0xFFFF).upper()[2:]
    return (crc16[:-1] if crc16.endswith("L") else crc16).zfill(4)

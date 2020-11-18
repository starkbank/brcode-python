import sys
import unicodedata


class Accents:

    @classmethod
    def remove(cls, text):
        stringClass = str
        if sys.version_info[0] < 3:
            stringClass = unicode
        if not isinstance(text, stringClass):
            text = stringClass(text, 'utf-8')

        text = unicodedata.normalize('NFD', text)
        text = text.encode('ascii', 'ignore')
        text = text.decode("utf-8")
        return str(text)
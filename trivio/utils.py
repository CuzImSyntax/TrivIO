import base64
import binascii


class Utils:
    """"Class with helping functions"""

    def decode(self, item):
        """"Decodes a given query"""

        if isinstance(item, int):
            return item
        elif isinstance(item, str):
            return self._decode(item)
        elif isinstance(item, list):
            return [self.decode(i) for i in item]
        elif isinstance(item, dict):
            return {key: self.decode(value) for key, value in item.values()}

    def _decode(self, item):
        """"Decodes a base64 string to an utf8 string"""
        try:
            return base64.b64decode(item).decode("utf8")
        except binascii.Error:
            return item
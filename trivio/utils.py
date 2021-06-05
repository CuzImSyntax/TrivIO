import base64
import binascii


class Utils:
    """"Class with helping functions"""

    def build_dict(self, item):
        """"Decodes a given query"""
        result = {"response_code": item["response_code"], "results": []}
        for question in item["results"]:
            result["results"].append({key: self.decode(value) for key, value in question.items()})
        return result

    def decode(self, item):
        if isinstance(item, int):
            return item
        elif isinstance(item, str):
            return self._decode(item)
        elif isinstance(item, list):
            return [self.decode(x) for x in item]
        elif isinstance(item, dict):
            return {key: self.decode(value) for key, value in item.items()}

    def _decode(self, item):
        """"Decodes a base64 string to an utf8 string"""
        try:
            return base64.b64decode(item).decode("utf8")
        except binascii.Error:
            return item
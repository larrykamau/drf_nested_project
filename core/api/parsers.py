from rest_framework.parsers import MultiPartParser, JSONParser

from .utils import NestedForm
from .settings import api_settings
from django.http import QueryDict


class NestedMultiPartParser(MultiPartParser):
    """
    Parser for multipart form data that is nested and also
    it may include files
    """
    options = api_settings.OPTIONS

    # def decoderz(self, key, value, data):

    #     if '[' in key and ']' in key:

    #         index_left_bracket = key.index('[')
    #         index_right_bracket = key.index(']')

    #         parent_key = key[:index_left_bracket]
    #         child_key = key[index_left_bracket + 1:index_right_bracket]

    #         if parent_key not in data:
    #             data[parent_key] = {} if len(child_key) > 0 else []

    #         if '][' in key:  # if has child
    #             key = child_key + key[index_right_bracket + 1:]  # root[parent][child] > parent[name3]
    #             self.decode(key=key, value=value, data=data[parent_key])
    #         elif isinstance(data[parent_key], list):
    #             data[parent_key].append(value)
    #         else:
    #             data[parent_key][child_key] = value

    #     else:
    #         data[key] = value

    def parse(self, stream, media_type=None, parser_context=None):
        parsed = super().parse(stream, media_type, parser_context)
        # ============================================================
        #                  Approach 1
        # ============================================================

        # files and data have to be merged into one
        if parsed.files:
            self._full_data =  parsed.data.copy()
            self._full_data.update(parsed.files)
        else:
            self._full_data = parsed.data

        form = NestedForm(self._full_data, **self.options)

        if form.is_nested():
            return form.data

        return parsed

        # # ============================================================
        # #                   Different Approach
        # # ============================================================

        # data = {}
        # for key, value in parsed.data.items():
        #     self.decoderz(key=key, value=value, data=data)

        # for key, value in parsed.files:
        #     self.decoderz(key=key, value=value, data=data)

        # print(data)

        # return data


class NestedJSONParser(JSONParser):
    """
    Parser for JSON data that is nested
    """
    options = api_settings.OPTIONS

    def parse(self, stream, media_type=None, parser_context=None):
        parsed = super().parse(stream, media_type, parser_context)

        form = NestedForm(parsed, **self.options)

        if form.is_nested():
            return form.data

        return parsed

import hashlib
import json


class ToolCache:

    def __init__(self):
        self.cache = {}

    def key(self, tool_name, params):

        s = tool_name + json.dumps(params, sort_keys=True)

        return hashlib.md5(s.encode()).hexdigest()

    def get(self, tool_name, params):

        return self.cache.get(self.key(tool_name, params))

    def set(self, tool_name, params, result):

        self.cache[self.key(tool_name, params)] = result
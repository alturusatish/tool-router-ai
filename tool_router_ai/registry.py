class ToolRegistry:

    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name] = tool

    def register_many(self, tools):
        for tool in tools:
            self.register(tool)

    def list_tools(self):
        return list(self.tools.values())

    def get(self, name):
        return self.tools.get(name)
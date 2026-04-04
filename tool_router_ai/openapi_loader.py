import requests
from .models import Tool


def load_openapi_tools(url):

    spec = requests.get(url).json()

    tools = []

    for path, methods in spec["paths"].items():

        for method, details in methods.items():

            name = details.get("operationId", f"{method}_{path}")

            desc = details.get("summary", "")

            tool = Tool(
                name=name,
                description=desc,
                input_schema=details.get("parameters", []),
                endpoint=path
            )

            tools.append(tool)

    return tools
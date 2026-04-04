# Capability Tool Router

An AI-powered tool routing system that uses semantic embeddings to intelligently route user queries to the most appropriate tools. Built with Python, OpenAI embeddings, and FAISS vector search.

## Features

- **Semantic Tool Routing**: Uses OpenAI embeddings and FAISS to match queries to tools based on semantic similarity
- **Tool Registry**: Flexible registry system for managing tools with descriptions and schemas
- **Caching**: Built-in result caching to improve performance and reduce API calls
- **Feedback Learning**: Tracks tool success/failure rates for continuous improvement
- **OpenAPI Integration**: Load tools directly from OpenAPI specifications
- **Async Support**: Fully asynchronous implementation for high performance

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd capability-tool-router
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Quick Start

```python
import asyncio
from tool_router_ai.registry import ToolRegistry
from tool_router_ai.router import ToolRouter
from tool_router_ai.embedder import Embedder
from tool_router_ai.models import Tool

# Define your tools
def get_weather(city: str):
    return f"Weather for {city}"

def get_stock_price(symbol: str):
    return f"Stock price for {symbol}"

async def main():
    # Create registry and register tools
    registry = ToolRegistry()
    
    registry.register(Tool(
        name="weather",
        description="Get weather information for any city",
        input_schema={"city": "string"},
        func=get_weather
    ))
    
    registry.register(Tool(
        name="stocks",
        description="Get stock market prices",
        input_schema={"symbol": "string"},
        func=get_stock_price
    ))
    
    # Create embedder and router
    embedder = Embedder()
    router = ToolRouter(registry, embedder)
    
    # Build the search index
    await router.build_index()
    
    # Route a query
    query = "What's the weather like in San Francisco?"
    tools = await router.route(query, top_k=1)
    
    print(f"Selected tool: {tools[0].name}")

asyncio.run(main())
```

## Architecture

### Core Components

- **ToolRouter**: Main routing engine that builds FAISS index and performs semantic search
- **ToolRegistry**: Manages tool registration and discovery
- **Embedder**: Handles text embedding using OpenAI's API
- **FeedbackStore**: Tracks tool performance metrics
- **ToolCache**: Caches tool execution results
- **OpenAPILoader**: Imports tools from OpenAPI specifications

### Tool Model

Each tool is defined with:
- `name`: Unique identifier
- `description`: Human-readable description for embedding
- `input_schema`: Parameter specification
- `func`: Python callable (for local tools)
- `endpoint`: API endpoint (for remote tools)

## Advanced Usage

### Loading Tools from OpenAPI

```python
from tool_router_ai.openapi_loader import load_openapi_tools

# Load tools from an OpenAPI spec
tools = load_openapi_tools("https://api.example.com/openapi.json")
registry.register_many(tools)
```

### Using Feedback for Learning

```python
from tool_router_ai.feedback_store import FeedbackStore

feedback = FeedbackStore()

# After tool execution
try:
    result = tool.func(**params)
    feedback.record_success(tool.name)
except Exception as e:
    feedback.record_failure(tool.name)

# Get success rate
score = feedback.score(tool.name)
```

### Caching Results

```python
from tool_router_ai.cache import ToolCache

cache = ToolCache()

# Check cache before execution
cached_result = cache.get(tool.name, params)
if cached_result:
    return cached_result

# Execute and cache
result = tool.func(**params)
cache.set(tool.name, params, result)
```

## Dependencies

- `faiss-cpu`: Vector similarity search
- `numpy`: Numerical computing
- `openai`: OpenAI API client

## Testing

Run the test suite:

```bash
python test.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license here]</content>
<parameter name="filePath">/Users/anish/Desktop/Satish/Practice/Capability Tool Router/README.md
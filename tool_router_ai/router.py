import faiss
import numpy as np


class ToolRouter:

    def __init__(self, registry, embedder):

        self.registry = registry
        self.embedder = embedder
        self.index = None
        self.tool_map = []

    async def build_index(self):

        tools = self.registry.list_tools()

        descriptions = [
            f"{tool.name}: {tool.description}"
            for tool in tools
        ]

        embeddings = await self.embedder.embed_batch(descriptions)

        vectors = np.array(embeddings).astype("float32")

        dim = vectors.shape[1]

        self.index = faiss.IndexFlatL2(dim)
        self.index.add(vectors)

        self.tool_map = tools

    async def route(self, query, top_k=3):

        emb = await self.embedder.embed(query)

        q = np.array([emb]).astype("float32")

        distances, ids = self.index.search(q, top_k)

        tools = []

        for idx in ids[0]:
            tools.append(self.tool_map[idx])

        return tools
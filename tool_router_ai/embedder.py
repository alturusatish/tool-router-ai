from openai import AsyncOpenAI

client = AsyncOpenAI()


class Embedder:

    async def embed_batch(self, texts):

        response = await client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )

        return [d.embedding for d in response.data]

    async def embed(self, text):

        emb = await self.embed_batch([text])
        return emb[0]
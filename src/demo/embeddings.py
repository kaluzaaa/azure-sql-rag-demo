"""Embeddings from Microsoft Foundry with Entra ID (no API key)."""

from functools import cache

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

from demo.config import load_settings

TOKEN_SCOPE = "https://ai.azure.com/.default"


@cache
def _client() -> tuple[OpenAI, str]:
    settings = load_settings()
    token_provider = get_bearer_token_provider(DefaultAzureCredential(), TOKEN_SCOPE)
    # Extra retries: the SDK waits and retries on HTTP 429 when a load exceeds the tokens per minute.
    client = OpenAI(base_url=settings.foundry_endpoint, api_key=token_provider, max_retries=10)
    return client, settings.embedding_deployment


def embed(texts: list[str]) -> list[list[float]]:
    client, deployment = _client()
    response = client.embeddings.create(model=deployment, input=texts)
    return [item.embedding for item in response.data]

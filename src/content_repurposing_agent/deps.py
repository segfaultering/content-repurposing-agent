from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel

from content_repurposing_agent.settings import settings


class StructOutput(BaseModel):
    content: list[str]


def get_llm() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=settings.model, api_key=settings.api_key.get_secret_value()
    )

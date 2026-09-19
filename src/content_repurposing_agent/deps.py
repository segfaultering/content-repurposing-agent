from langchain_google_genai import ChatGoogleGenerativeAI

from content_repurposing_agent.settings import settings


def get_llm() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=settings.model, 
        api_key=settings.api_key.get_secret_value()
    )

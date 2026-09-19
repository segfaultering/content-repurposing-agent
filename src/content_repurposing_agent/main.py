from langchain_core.prompts import ChatPromptTemplate

from content_repurposing_agent.deps import StructOutput, get_llm
from content_repurposing_agent.settings import ENCODING, SYS_PROMPT


def main(user_input: str) -> list[str]:
    llm = get_llm()
    struct_llm = llm.with_structured_output(StructOutput)
    sys_prompt_text = SYS_PROMPT.read_text(encoding=ENCODING)
    prompt = ChatPromptTemplate.from_messages(
        [("system", sys_prompt_text), ("user", "{user_input}")]
    )
    chain = prompt | struct_llm
    response = chain.invoke({"user_input": user_input})

    return response.content  # pyrefly: ignore

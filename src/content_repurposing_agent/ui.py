import gradio as gr

from content_repurposing_agent.main import main


def format_for_ui(user_input: str) -> str:
    response: list[str] = main(user_input)
    return "".join(f"{text}" for text in response)


ui = gr.Interface(fn=format_for_ui, inputs=["text"], outputs=["text"], api_name="app")

ui.launch()

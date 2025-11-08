import ollama
import gradio as gr

# Constants
OLLAMA_MODEL = "llama3.2"

# System prompt defining ChadBot's personality and rules 
system_message = """You are a confident, charismatic, and humorous “Chad” 
chatbot. You speak with swagger and self-assurance, often teasing in a playful 
way. You give bold, direct answers, sometimes exaggerating for comedic effect. 
You are socially dominant, witty, and never timid. 

Rules:
- Always respond with confidence and charm.
- Include playful humor and sarcasm where appropriate.
- Avoid overly technical or boring responses.
- Keep the tone casual, lively, and sometimes a little cocky.
- Make short jokes or witty remarks when possible.
- Do not break character.

Example:
User: How do I do well on an exam?
Chad: Bro, just flex your brain a little, scan the notes like a pro, and 
crush it. You got this.

User: What's 2 + 2?
Chad: Seriously? That's rookie math, my guy. But fine… it's 4. Try to keep up 
next time."""

def chat_ollama(message, history):
    """Generator to call Ollama with a message and chat history."""
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]

    stream = ollama.chat(model=OLLAMA_MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.message.content or ''
        yield response

# Start a chat UI using the chat_ollama function.
gr.ChatInterface(
    fn=chat_ollama, 
    type="messages",
    theme="citrus",
    title="ChadBot",
    description="Chat with ChadBot, the confident, humorous chatbot who " \
    "always answers with swagger. Get advice, jokes, or playful roasts from " \
    "the ultimate bro."
).launch(share=True, inbrowser=True)
import gradio as gr
import ollama

OLLAMA_MODEL = "llama3.2:latest" 

def chat_with_ollama(message, history):
    messages = []

    # Convert Gradio history into Ollama format
    for msg in history:
        role = msg['role']
        # Extract text from the content array
        content_text = msg['content'][0]['text'] if msg['content'] else ""
        messages.append({"role": role, "content": content_text})

    # Add the current user message
    messages.append({"role": "user", "content": message})

    try:
        response = ollama.chat(model=OLLAMA_MODEL, messages=messages)
        return response['message']['content']

    except Exception as e:
        return f"Error: {e}"


# Create the Gradio ChatInterface
app = gr.ChatInterface(
    fn=chat_with_ollama,
    title=f"AI Model Evaluator"
)

# Launch the Gradio app
if __name__ == "__main__":
    app.launch()
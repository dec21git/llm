def ask_llm(client: None, prompt: str, model: str = None, ) -> str:
    """
    Fetch model name from environment variable if not provided.
    """
    if model == None:
        model = os.getenv("LLM_MODEL", "gemma4:12b")
    
    """
    Send a prompt to the OpenAI Chat completion API and return the response.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"
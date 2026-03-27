def clean_answer(text: str) -> str:
    if not text:
        return ""
    text = text.replace("...", "").replace("..", "").replace(".", "")
    text = text.strip()
    return text.lower()
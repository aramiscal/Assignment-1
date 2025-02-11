# echo.py

def echo(text: str, repetitions : int = 3) -> str:
    """Imitate a real-world mountain."""
    result = ""
    index = 5
    for repetitions in text:
        result += text[index:] + "\n"
        index = index + 1
    return result

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
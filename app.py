"""Tiny app for Jenkins practice - no external dependencies."""

def greeting(name: str = "Jenkins") -> str:
    return f"Hello, {name}! Your pipeline works."

if __name__ == "__main__":
    print(greeting())

"""Entry point for the starter Python application."""


def greet(name: str = "world") -> str:
    """Return a friendly greeting string."""
    return f"Hello, {name}!"


def main() -> None:
    """Run the CLI entry point."""
    print(greet())


if __name__ == "__main__":
    main()

"""{{ cookiecutter.package_description }}."""


def greet(name: str) -> str:
    if not name.strip():
        name = "world"
    return f"Hello, {name}!"

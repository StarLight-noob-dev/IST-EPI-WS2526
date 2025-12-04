# Avoid using global variables
global variable_name
variable_name = "This is a global variable"

def hello_world(name: str) -> str:
    """Returns a greeting message.

    Args:
        name (str, optional): The name to greet. Defaults to None.

    Returns:
        str: A greeting message.
    """
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"


import questionary


def default_questions():
    env = questionary.select(
        "Package Manager", choices=["Poetry", "Pip", "Virtual Environment"]
    ).ask()
    return env

# Validates code type and length (6).
def code_validation(code: str) -> bool:
    return code.isnumeric() and len(code) == 6


# Validates name type, length and no spacing
def name_validation(name: str) -> bool:
    name = name.strip()
    return 0 < len(name) <= 30


# Validates credits to be between 1 and 9
def credits_validation(credits: str) -> bool:
    if credits.isnumeric():
        return 1 <= int(credits) <= 9
    return False



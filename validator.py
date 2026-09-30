def validate_phone(phone: str) -> bool:
    """Валидация российского телефонного номера."""
    import re

    pattern = r'^\+?7\d{10}$'
    cleaned_phone = phone.replace('-', '').replace(' ', '')
    return bool(re.match(pattern, cleaned_phone))


def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re

    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))
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


def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС."""
    import re

    cleaned = snils.replace('-', '').replace(' ', '')

    if not re.match(r'^\d{11}$', cleaned):
        return False

    numbers = [int(digit) for digit in cleaned[:9]]
    check_sum = int(cleaned[9:11])
    calculated = sum((9 - i) * numbers[i] for i in range(9))

    if calculated < 100:
        expected = calculated
    elif calculated % 101 == 100:
        expected = 0
    else:
        expected = calculated % 101

    return expected == check_sum
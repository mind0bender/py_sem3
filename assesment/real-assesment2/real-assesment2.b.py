# email validation for user reg\tion


def is_valid_email(email: str) -> bool:
    if email.count("@") != 1:
        return False
    username, domain = email.split("@")

    special_chars_allowed = "_.-"

    special_chars_in_username: str = "".join(
        [char for char in username if not char.isalnum()]
    )
    is_username_valid = (
        all(
            [
                special_char in special_chars_allowed
                for special_char in special_chars_in_username
            ]
        )
        and username[-1].isalnum()
    )

    if domain.count(".") != 1:
        return False
    domain_name, domain_ext = domain.split(".")
    special_chars_in_domain: str = "".join(
        [char for char in domain if not char.isalnum()]
    )
    is_domain_valid = (
        all(
            [
                special_char in special_chars_allowed
                for special_char in special_chars_in_domain
            ]
        )
        and len(domain_ext) >= 2
        and len(domain_name) > 0
    )
    return is_username_valid and is_domain_valid


email: str = input("Enter your email: ")
print(is_valid_email(email))

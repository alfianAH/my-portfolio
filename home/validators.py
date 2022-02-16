from django.core.validators import URLValidator

def validate_url(value):
    """Validate URL link

    Args:
        value (str): URL value

    Raises:
        ValidationError: Raise validation error if url is not valid
    """
    url_validator = URLValidator()
    url_validator(value)
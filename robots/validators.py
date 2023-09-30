from django.core.exceptions import ValidationError

from robots.models import Robot


def validate_robot_data(data):
    try:
        Robot(**data).clean_fields()
    except ValidationError:
        return str(f"Поля model и version должны содержать по 2 символа")
    return None
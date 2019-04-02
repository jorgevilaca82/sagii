from django.core.validators import RegexValidator


class PhoneRegexValidator(RegexValidator):
    regex = r'^(\+?\d{2}\s?)?(\(\d{2}\)|\d{2})\s?(\d{4,5})(\-?)(\d{4})$'

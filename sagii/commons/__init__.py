# codigo comum compartilhado pelas apps
from enum import Enum, EnumMeta
from django.core.validators import RegexValidator

class ChoiceEnumCharValueMeta(EnumMeta):
    def __iter__(self):
        return ((tag.value, tag.value) for tag in super().__iter__())

class AutoNameEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

class PhoneRegexValidator(RegexValidator):
    regex = r'/^(?:(\+?)(55\d{2})|\d{2})([6-9]\d{4})(\-?)(\d{4})$/'
# codigo comum compartilhado pelas apps
from enum import Enum, EnumMeta


class ChoiceEnumCharValueMeta(EnumMeta):
    def __iter__(self):
        return ((tag.value, tag.value) for tag in super().__iter__())


class AutoNameEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.title()

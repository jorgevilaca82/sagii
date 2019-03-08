# codigo comum compartilhado pelas apps
from enum import EnumMeta

class ChoiceEnumCharValueMeta(EnumMeta):
    def __iter__(self):
        return ((tag.value, tag.value) for tag in super().__iter__())
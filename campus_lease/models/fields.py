from peewee import CharField
from enum import Enum


class EnumField(CharField):
    def __init__(self, enum, *args, **kwargs):
        self.enum = enum
        self.force_uppercase = kwargs.pop('force_uppercase', False)
        kwargs['choices'] = [(x, x.value) for x in enum]
        super().__init__(*args, **kwargs)

    def db_value(self, value):
        if isinstance(value, Enum):
            return value.name
        else:
            return value

    def python_value(self, value):
        if value is None:
            return None
        else:
            if self.force_uppercase:
                value = value.upper()

            return self.enum[value]


class ListField(CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def db_value(self, value):
        if isinstance(value, list):
            return ",".join(value)
        else:
            return value

    def python_value(self, value):
        if value is None:
            return []
        else:
            return value.split(",")

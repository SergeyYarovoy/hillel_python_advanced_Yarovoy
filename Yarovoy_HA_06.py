from typing import List
from uuid import uuid4


########################################################################
class ImmutablePerson(object):
    """
    An immutable Person class
    """
    __slots__: list[str] = ["uuid", "name", "last_name"]

    # ----------------------------------------------------------------------
    def __init__(self, name, last_name):
        """Constructor"""
        super(ImmutablePerson, self).__setattr__("uuid", uuid4().hex)
        self.set_name(name)
        self.set_lastname(last_name)

    # ----------------------------------------------------------------------
    def __setattr__(self, name, value):
        msg = "'%s' has no attribute %s" % (self.__class__, name)
        raise AttributeError(msg)

    # ----------------------------------------------------------------------
    def set_name(self, name):
        super(ImmutablePerson, self).__setattr__("name", name)

    # ----------------------------------------------------------------------
    def set_lastname(self, last_name):
        super(ImmutablePerson, self).__setattr__("last_name", last_name)

    # ----------------------------------------------------------------------
    def get_uuid(self):
        return getattr(self, "uuid")

    # ----------------------------------------------------------------------
    def get_name(self):
        return getattr(self, "name")

    # ----------------------------------------------------------------------
    def get_last_name(self):
        return getattr(self, "last_name")


########################################################################

# Инициируем класс ImmutablePerson, Имя и Фамилию задаем явно, UUID генерируется автоматически
person = ImmutablePerson("Петро", "Ребро")
print(person.uuid, person.name, person.last_name)
# меняем Имя и Фамилию
person.set_name("Ганна")
person.set_lastname("Шумейко")
# получаем UUID, Имя и Фамилию адресуя их напрямую
print(person.uuid, person.name, person.last_name)
# получаем UUID, Имя и Фамилию посредством методов
print(person.get_uuid(), person.get_name(), person.get_last_name())
# ошибка, при попытке изменить UUID, Имя или фамилию адресуя их непосредственно
# person.uuid = 123
person.name = "Оксана"
# person.last_name = "Покотило"

from uuid import uuid4
from copy import copy, deepcopy
from typing import Union


########################################################################
class Person(object):

    def __init__(self, name: Union[str] = "", last_name: Union[str] = ""):
        self.uuid = uuid4().hex
        self.name = name
        self.last_name = last_name

    # ----------------------------------------------------------------------
    def __hash__(self):
        return hash(self.uuid)

    # ----------------------------------------------------------------------
    def __eq__(self, other):
        return self.uuid == other.uuid

    # ----------------------------------------------------------------------
    def __repr__(self):
        return f'{type(self).__name__}(UUID = {copy(self.uuid)}, name = {copy(self.name)}, ' \
               f'last_name = {copy(self.last_name)})'

    # ----------------------------------------------------------------------
    def _set_uuid(self: object) -> object:
        self._uuid = uuid4().hex
        return

    # ----------------------------------------------------------------------
    def set_name(self, name: object) -> object:
        self.name = name
        return

    # ----------------------------------------------------------------------
    def set_lastname(self, last_name: object) -> object:
        self.last_name = last_name
        return

    # ----------------------------------------------------------------------
    def get_uuid(self):
        return getattr(self, "uuid")

    # ----------------------------------------------------------------------
    def get_name(self):
        return getattr(self, "name")

    # ----------------------------------------------------------------------
    def get_last_name(self):
        return getattr(self, "last_name")

    # ----------------------------------------------------------------------
    def create_new_copy_of_person(self, **kwargs):
        tmp_copy = deepcopy(self)
        for key_in_kwargs in kwargs:
            setattr(tmp_copy, key_in_kwargs, kwargs[key_in_kwargs])
        setattr(tmp_copy, 'uuid', uuid4().hex)

        return tmp_copy


########################################################################


if __name__ == '__main__':

    # Инициируем класс Person, Имя и Фамилию задаем явно, UUID генерируется автоматически
    person = Person("Петро", "Ребро")

    # печатаем поля нашего объекта через __repr__
    print(person)

    # печатаем поля нашего объекта через методы
    print(person.get_uuid(), person.get_name(), person.get_last_name())

    # теперь печатаем содержимое наших полей прямым доступом
    print(person.uuid, person.name, person.last_name)

    # меняем Имя и Фамилию и проверяем
    person.set_name("Ганна")
    print(person)
    assert person.name == "Ганна", 'Object has not been changed'

    person.set_lastname("Шумейко")
    # проверяем фамилию
    assert person.last_name == "Шумейко", 'Object has not been changed'

    # снова печатем поля нашего объекта через __repr__
    print(person)

    # меняем поля прямым доступом
    person.name = "Оксана"
    person.last_name = "Покотило"
    person.uuid = 1234567890

    # смотрим, что там у нас внутри
    print(person)

    # Хакаем поле "name"
    super(Person, person).__setattr__("name", "Василь")
    #
    print(person.name)

    # создаем копию экземпляра и пытаемся задать ему uuid  --
    # в этом случае uuid должен создаться новый, но если мы не задаем имя и/или фамилию,
    # то эти поля олжны скопироваться из родительского экземпляра

    new_person = person.create_new_copy_of_person(uuid=123)
    #
    print("the old person = ", person)          # uuid должен быть измененный выше на 1234567890
    print("the new persond = ", new_person)     # а тут uuid должен быть уже сгенеренный


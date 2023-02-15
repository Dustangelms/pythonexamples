class Example:
    class_member = 1

    @staticmethod
    def get_static_member():
        return Example.class_member

    @staticmethod
    def set_static_member(static_member_value):
        Example.class_member = static_member_value

    @classmethod
    def get_class_member(cls):
        return cls.class_member

    @classmethod
    def set_class_member(cls, class_member_value):
        cls.class_member = class_member_value

    def __init__(self):
        self.object_member = 'a'

    def __del__(self):
        print('Объект уничтожается')

    def set_object_member(self, object_member_value):
        self.object_member = object_member_value
        self.new_object_member = object_member_value * 2

    def get_object_member(self):
        return self.object_member


class Example_child(Example):
    class_member = 2

    def set_object_member(self, object_member_value):
        super().set_object_member(object_member_value + ' child')


print(Example.get_static_member())
print(Example_child.get_static_member())

print(Example.get_class_member())
print(Example_child.get_class_member())

Example_child.set_class_member(3)

print(Example.get_class_member())
print(Example_child.get_class_member())

example = Example()

print(example.get_object_member())
example.set_object_member('b')
print(example.get_object_member())
print(example.new_object_member)

example_child = Example_child()

print(example_child.get_object_member())
example_child.set_object_member('b')
print(example_child.get_object_member())
print(example_child.new_object_member)

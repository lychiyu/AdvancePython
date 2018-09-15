# coding: utf-8

"""
 Created by liuying on 2018/9/15.
"""
import numbers


class Field:
    def __init__(self, db_column):
        self.db_column = db_column


class CharField(Field):
    def __init__(self, db_column, max_length):
        super().__init__(db_column)
        self._value = None
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('int value need')
        self._value = value


class IntField(Field):
    def __init__(self, db_column, min_value, max_value):
        super().__init__(db_column)
        self._value = None
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        self._value = value


class Model(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        meta = attrs.get('Meta', None)
        _meta = {}
        _meta['db_table'] = getattr(meta, 'db_table') if meta and getattr(meta, 'db_table', None) else name.lower()
        attrs['_meta'] = _meta
        attrs['fields'] = fields
        del attrs['Meta']
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=Model):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()

    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column.lower() if value.db_column else key
            value = getattr(self, key)
            fields.append(db_column)
            values.append(value)
        sql = f"insert into {self._meta['db_table']} ({','.join(map(str, fields))}) values ({','.join(map(str, values))})"
        return sql


class User(BaseModel):
    name = CharField(db_column='', max_length=10)
    age = IntField(db_column='', min_value=0, max_value=100)

    class Meta:
        db_table = 'user'


if __name__ == '__main__':
    user = User(name='lychiyu', age=22)
    user.save()

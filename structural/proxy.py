class lazy_property(object):
    def __init__(self, fget):
        self.fget = fget
        self.func_name = fget.__name__

    def __get__(self, obj, cls):
        if obj is None:
            return None
        value = self.fget(obj)
        setattr(obj, self.func_name, value)
        return value


class Test(object):

    @lazy_property
    def results(self):
        print('init')
        calcs = 5
        return calcs


t = Test()
print(t.results)
print('')
print(t.results)

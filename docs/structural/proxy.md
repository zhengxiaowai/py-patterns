## 代理模式

### 定义

为其他对象提供一种代理以控制对这个对象的访问。

### 动机

对属性和方法的访问控制。

### 适用性

- 远程代理（Remote Proxy）为一个对象在 不同的地址空间 提供局部代表。
- 虚代理（Virtual Proxy）根据需要创建开销很大的对象。
- 保护代理（Protection Proxy）控制对原始对象的访问。

### 实现

```python
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
```
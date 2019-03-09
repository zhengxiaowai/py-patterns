## 单例模式

### 定义

保证一个类仅有一个实例，并提供一个访问它的全局访问点。

### 动机

在实际编程中，有的时候制造出多个实例，就会导致许多问题的产生。例如，程序的异常行为，资源使用过量，或者是不一致的结果。

### 适用性

- 当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时。
- 当这个唯一实例应该是通过子类化可扩展的，并且客户应该无需更改代码就能使用一个扩展的实例时。

### 优缺点

- 对实例受控访问
- 缩小命名空间
- 允许对操作和表示的精化 
- 允许可变数目的实例
- 比类操作更灵活

### 实现

```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(object):
    __metaclass__ = Singleton
```
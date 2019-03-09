## 观察者模式

### 定义

定义对象间的一种一对多的依赖关系 ,当一个对象的状态发生改变时 , 所有依赖于它的对象都得到通知并被自动更新。

### 动机

将一个系统分割成一系列相互协作的类有一个常见的副作用:需要维护相关对象间的一致性。我们不希望为了维持一致性而使各类紧密耦合，因为这样降低了它们的可重用性。

### 适用性

- 当一个抽象模型有两个方面 , 其中一个方面依赖于另一方面。将这二者封装在独立的对象中以使它们可以各自独立地改变和复用。
- 当对一个对象的改变需要同时改变其它对象 , 而不知道具体有多少对象有待改变。
- 当一个对象必须通知其它对象，而它又不能假定其它对象是谁。换言之 , 你不希望这些对象是紧密耦合的。

### 优缺点

- 目标和观察者间的抽象耦合
- 支持广播通信
- 意外的更新

### 实现

> 有一个气象站可以获取温度、湿度、氧气的数据，和一些面板，每当数据更新时候要显示在面板上 —— 《Head First 设计模式》

```python
class AbstractObservable(object):
    def register(self):
        raise NotImplementedError(
            'register is a abstract method which must be implemente')

    def remove(self):
        raise NotImplementedError(
            'remove is a abstract method which must be implemente')
```

观察者这观察的对象，称作可观察对象，该抽象类需要实现具体的注册和删除观察者管理方法。

```python
class AbstractDisplay(object):
    def update(self):
        raise NotImplementedError(
            'update is a abstract method which must be implemente')

    def display(self):
        raise NotImplementedError(
            'display is a abstract method which must be implemente')
```

观察者抽象类，需要实现 update 方法，让可观察对象可以通知观察者。

```python
class Subject(object):
    def __init__(self, subject):
        self.subject = subject
        self._observers = []

    def register(self, ob):
        self._observers.append(ob)

    def remove(self, ob):
        self._observers.remove(ob)

    def notify(self, data=None):
        for ob in self._observers:
            ob.update(data)
```

此外还实现了一个 Subject 用于管理多个事件的通知，可以称作可观察对象管理者。

```python
class WeatherData(AbstractObservable):
    def __init__(self, *namespaces):
        self._nss = {}
        self._clock = None
        self._temperature = None
        self._humidity = None
        self._oxygen = None

        for ns in namespaces:
            self._nss[ns] = Subject(ns)

    def register(self, ns, ob):
        if ns not in self._nss:
            raise Exception('this {} is invalid namespace'.format(ns))
        self._nss[ns].register(ob)

    def remove(self, ns, ob):
        return self._nss[ns].remove(ob)

    def set_measurement(self, data):
        # 此处实现可以更加紧凑，但是为了表达更简单，采用如下方式
        self._clock = data['clock']
        self._temperature = data['temperature']
        self._humidity = data['humidity']
        self._oxygen = data['oxygen']

        for k in self._nss.keys():
            if k != 'all':
                data = self

            self._nss[k].notify(data)
	
    # 以下 property 为了实现 pull 模式
    
    @property
    def clock(self):
        return self._clock

    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity
    @property
    def oxygen(self):
        return self._oxygen

```

观察者模式的可观察对象实现可以分成两种实现方案：

- push 模式
- pull 模式

push 模式能保证所有的观察者可以接收到全部的数据，无论需要不需要，频繁更新会影响性能。

pull 模式需要观察者自己拉去数据，实现起来比较容易出错，但是能按需获取信息。

```python
class OverviewDisplay(AbstractDisplay):
    def __init__(self):
        self._data = {}

    def update(self, data):
        self._data = data
        self.display()

    def display(self):
        print(u'总览显示面板：')
        for k, v in self._data.items():
            print(k + ': ' + str(v))
```

这是一个总览的 Display ，采用 push 模式更新，获取当前能获取的所有数据，并且显示出来。

```python
class TemperatureDisplay(AbstractDisplay):
    def __init__(self):
        self._storage = []

    def update(self, data):
        dt = data.clock
        temperature = data.temperature
        self._storage.append((dt, temperature))
        self.display()

    def display(self):
        print(u'温度显示面板：')
        for storey in self._storage:
            print(storey[0] + ': ' + str(storey[1]))
```

一个只会显示温度的 Display，能观察到时间和温度变化，由于只关心温度数据，所以采用 pull 模式更加合适。

```python
if __name__ == '__main__':
    import time
    
    # 生成一个可观察对象，支持('all', 'temperature', 'humidity', 'oxygen')的数据通知
    wd = WeatherData('all', 'temperature', 'humidity', 'oxygen')
    
    # 两个观察者对象
    od = OverviewDisplay()
    td = TemperatureDisplay()

    # 注册到可观察对象中，能获取数据更新
    wd.register('all', od)
    wd.register('temperature', td)
	
    # 更新数据，可观察对象将会自动更新数据
    wd.set_measurement({
        'clock': time.strftime("%Y-%m-%d %X", time.localtime()),
        'temperature': 20,
        'humidity': 60,
        'oxygen': 10
    })
	
    # 一秒后再次更新数据
    time.sleep(1)
    print('\n')
    wd.set_measurement({
        'clock': time.strftime("%Y-%m-%d %X", time.localtime()),
        'temperature': 21,
        'humidity': 58,
        'oxygen': 7
    })
```

执行的结果如下：

```shell
总览显示面板：
humidity: 60
temperature: 20
oxygen: 10
clock: 2017-03-26 18:08:41
温度显示面板：
2017-03-26 18:08:41: 20

总览显示面板：
humidity: 58
temperature: 21
oxygen: 7
clock: 2017-03-26 18:08:42
温度显示面板：
2017-03-26 18:08:41: 20
2017-03-26 18:08:42: 21
```

一秒后数据更新，两个面板会自动更新数据。

> Python 设计模式相关代码可以 https://github.com/zhengxiaowai/design-patterns 获得。
>
> 该模式的代码可以从 https://raw.githubusercontent.com/zhengxiaowai/design-patterns/master/behavioral/observer.py 获得

当需要一个湿度面板时候也是只需要生成这个面板、并且实现你所需要的 update、display 方法然后再注册到可观察对象中即可，无须修改其他部分，实现了结构的解耦。

观察者模式在很多软件和框架中经常出现，比如 MVC 框架，事件的循环等应用场景。若希望在一个对象的状态变化时能够通知/提醒所有相关者（一个对象或一组对象），则可以使用观察者模式。观察者模式的一个重要特性是，在运行时，订阅者/观察者的数量以及观察者是谁可能会变化，也可以改变。

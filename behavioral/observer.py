#!/usr/bin/env python
# -*- coding: utf-8 -*-


class AbstractDisplay(object):
    def update(self):
        raise NotImplementedError(
            'update is a abstract method which must be implemente')

    def display(self):
        raise NotImplementedError(
            'display is a abstract method which must be implemente')


class AbstractObservable(object):
    def register(self):
        raise NotImplementedError(
            'register is a abstract method which must be implemente')

    def remove(self):
        raise NotImplementedError(
            'remove is a abstract method which must be implemente')


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
        self._clock = data['clock']
        self._temperature = data['temperature']
        self._humidity = data['humidity']
        self._oxygen = data['oxygen']

        for k in self._nss.keys():
            if k != 'all':
                data = self

            self._nss[k].notify(data)

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


if __name__ == '__main__':
    import time
    wd = WeatherData('all', 'temperature', 'humidity', 'oxygen')
    od = OverviewDisplay()
    td = TemperatureDisplay()

    wd.register('all', od)
    wd.register('temperature', td)

    wd.set_measurement({
        'clock': time.strftime("%Y-%m-%d %X", time.localtime()),
        'temperature': 20,
        'humidity': 60,
        'oxygen': 10
    })

    time.sleep(1)
    print('\n')
    wd.set_measurement({
        'clock': time.strftime("%Y-%m-%d %X", time.localtime()),
        'temperature': 21,
        'humidity': 58,
        'oxygen': 7
    })

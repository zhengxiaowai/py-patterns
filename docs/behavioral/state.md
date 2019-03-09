## 状态模式

### 定义

允许一个对象在其内部状态改变时改变它的行为，对象看起来似乎修改了它的类。

### 动机

事物存在有限的不同状态，并且可以在状态中互相切换，作为相应的行为。

### 适用性

- 一个对象的行为取决于它的状态,并且它必须在运行时刻根据状态改变它的行为。
- 一个操作中含有庞大的多分支的条件语句，且这些分支依赖于该对象的状态。

### 实现

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


class State(object):
    def __init__(self, process):
        self.process = process

    def execute(self):
        raise NotImplementedError('you must implemment this method')

    def handup(self):
        raise NotImplementedError('you must implemment this method')

    def killed(self):
        raise NotImplementedError('you must implemment this method')


class ProcessError(Exception):
    pass


class CreatedState(State):
    def execute(self):
        print('execute process, transform to running state')
        self.process.set_state(self.process.running_state)

    def handup(self):
        print('handup process, transform to waitting state')
        self.process.set_state(self.process.waitting_state)

    def killed(self):
        print('killed process, transform to waitting teminated')
        self.process.set_state(self.process.terminated_state)


class WaittingState(State):
    def execute(self):
        print('execute process, transform to running state')
        self.process.set_state(self.process.running_state)

    def handup(self):
        print('handup process, transform to waitting state')
        self.process.set_state(self.process.waitting_state)

    def killed(self):
        print('killed process, transform to waitting teminated')
        self.process.set_state(self.process.terminated_state)


class RunningState(State):
    def execute(self):
        raise ProcessError('running state have not execute method')

    def handup(self):
        raise ProcessError('running state have not handup method')

    def killed(self):
        print('killed process, transform to waitting teminated')
        self.process.set_state(self.process.terminated_state)


class TerminateState(State):
    def execute(self):
        raise ProcessError('running state have not execute method')

    def handup(self):
        raise ProcessError('running state have not handup method')

    def killed(self):
        print('process was teminated')
        self.process.set_state(self.process.terminated_state)


class Process(object):
    def __init__(self, name):
        self.created_state = CreatedState(self)
        self.waitting_state = WaittingState(self)
        self.running_state = RunningState(self)
        self.terminated_state = TerminateState(self)

        self.name = name
        self.state = self.created_state

    def __str__(self):
        return self.state.__class__.__name__

    def set_state(self, state):
        self.state = state

    def execute(self):
        self.state.execute()

    def handup(self):
        self.state.handup()

    def killed(self):
        self.state.killed()


if __name__ == '__main__':
    print('Process NO.1')
    p1 = Process('p1')
    p1.execute()
    p1.killed()

    print('\nProcess NO.2')
    p2 = Process('p2')
    p2.handup()
    p2.execute()
    p2.killed()

    print('\nProcess NO.3')
    p3 = Process('p3')
    p3.handup()
    p3.handup()
    p3.killed()

    print('\nProcess NO.4')
    p4 = Process('p4')
    p4.killed()
```


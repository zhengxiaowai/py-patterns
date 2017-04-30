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
    p2.killed

    print('\nProcess NO.3')
    p3 = Process('p3')
    p3.handup()
    p3.handup()
    p3.killed

    print('\nProcess NO.4')
    p4 = Process('p4')
    p4.killed()

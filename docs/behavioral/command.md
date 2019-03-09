## 命令模式

### 定义

将一个请求封装为一个对象，从而使你可用不同的请求对客户进行参数化;对请求排队或记录请求日志，以及支持可撤消的操作。

### 动机

有时必须向某对象提交请求，但并不知道关于被请求的操作或请求的接受者的任何信息。

### 适用性

- 抽象出待执行的动作参数化某对象（调用者和实现者解耦）。
- 在不同时候制定、排列和执行请求。
- 支持取消操作。
- 支持修改日志，这样当系统崩溃时，这些修改可以被重做一遍。
- 用构建在原语操作上的高层操作构造一个系统（事物）。

### 实现

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Transaction(object):
    def __init__(self):
        self.commands = []
        self.success = []

    def add_command(self, command):
        self.commands.append(command)

    def excute(self):
        """ 调用者不需要知道执行什么，只知道有 excute 方法"""
        for command in self.commands:
            command.excute()
            self.success.append(command)

    def undo(self):
        for command in self.success[::-1]:
            command.undo()


class CreateCommand(object):
    def __init__(self, filename):
        self.filename = filename

    def excute(self):
        print('create a {}'.format(self.filename))

    def undo(self):
        print('delete this {}'.format(self.filename))


class WriteCommand(object):
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    def excute(self):
        print('write [{}] to {}'.format(self.content, self.filename))

    def undo(self):
        print('remove [{}] from {}'.format(self.content, self.filename))


class ChomdCommand(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def excute(self):
        print('change {} mode to {}'.format(self.filename, self.mode))

    def undo(self):
        print('revocer {} mode to {}'.format(self.filename, '644'))


class MoveCommand(object):
    """ 假设这个命令发生了错误 """

    def __init__(self, filename, to_path):
        self.filename = filename
        self.to_path = to_path

    def excute(self):
        print('move {} to {}'.format(self.filename, self.to_path))
        raise Exception('you have not permission')

    def undo(self):
        print('move {} to {}'.format(self.to_path, self.filename))


if __name__ == '__main__':
    create_command = CreateCommand('test.file')
    write_command = WriteCommand('test.file', 'my name is zhengxiaowai')
    chmod_command = ChomdCommand('test.file', '600')

    file_operation = Transaction()
    file_operation.add_command(create_command)
    file_operation.add_command(write_command)
    file_operation.add_command(chmod_command)

    # file_operation.excute()

    try:
        # 发生错误恢复原始状态
        move_command = MoveCommand('test.file', '/etc/')
        file_operation.add_command(move_command)
        file_operation.excute()
    except:
        print('\nraise a error, start to undo:\n')
        file_operation.undo()
```
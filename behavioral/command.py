#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Transaction(object):
    def __init__(self):
        self.commands = []
        self.success = []

    def add_command(self, command):
        self.commands.append(command)

    def execute(self):
        """ 调用者不需要知道执行什么，只知道有 execute 方法"""
        for command in self.commands:
            command.execute()
            self.success.append(command)

    def undo(self):
        for command in self.success[::-1]:
            command.undo()


class CreateCommand(object):
    def __init__(self, filename):
        self.filename = filename

    def execute(self):
        print('create a {}'.format(self.filename))

    def undo(self):
        print('delete this {}'.format(self.filename))


class WriteCommand(object):
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    def execute(self):
        print('write [{}] to {}'.format(self.content, self.filename))

    def undo(self):
        print('remove [{}] from {}'.format(self.content, self.filename))


class ChomdCommand(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def execute(self):
        print('change {} mode to {}'.format(self.filename, self.mode))

    def undo(self):
        print('revocer {} mode to {}'.format(self.filename, '644'))


class MoveCommand(object):
    """ 假设这个命令发生了错误 """

    def __init__(self, filename, to_path):
        self.filename = filename
        self.to_path = to_path

    def execute(self):
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

    # file_operation.execute()

    try:
        # 发生错误恢复原始状态
        move_command = MoveCommand('test.file', '/etc/')
        file_operation.add_command(move_command)
        file_operation.execute()
    except:
        print('\nraise a error, start to undo:\n')
        file_operation.undo()

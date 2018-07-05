from collections import namedtuple


class Event:
    def __init__(self, name, **kwargs):
        self.name = name
        self.instanceId = kwargs.pop('instanceId', None)
        self.reference_date = kwargs.pop('referenceDate', None)
        self.tag = kwargs.pop('tag', None)
        self.version  = kwargs.pop('tag', None)
        self.image = kwargs.pop('image', None)
        self.scope = kwargs.pop('scope', 'execution')
        self.branch = kwargs.pop('branch', 'master')
        self.commands = kwargs.pop('commands',[])
        self.reproduction = kwargs.pop('reproduction', dict())
        self.reprocessing = kwargs.pop('reprocessing', dict())
        self.payload = kwargs.pop('payload', dict())

    def __str__(self):
        return (f"Name: {self.name}"
                f"Instance Id: {self.instanceId}"
                f"Payload: {self.payload}")

Process = namedtuple("Process", [
    "id",
    "name",
    "solution",
    "instance",
    "image",
])


Container = namedtuple("Container", [
    "name",
    "tag",
])


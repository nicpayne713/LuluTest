from action import *
from page import *
from element import *


class Do:
    def __init__(self, steps):
        for step in steps.each:
            DoStep(step)


class DoStep:
    def __init__(self, step):
        self.subject = step.subject
        self.map = None
        self.__resolve_subject()
        self.operation = self.map.get(step.operation)
        self.__do_operation(step)

    def __resolve_subject(self):
        if type(self.subject) == Page or self.subject is None:
            self.map = page_action_map
        elif isinstance(self.subject, BaseElement):
            self.map = element_action_map

    def __do_operation(self, step):
        if not step.subject:
            self.operation(step.action_object)
        elif step.data:
            self.operation(step.action_object, self.subject, step.data)
        else:
            self.operation(step.action_object, self.subject)

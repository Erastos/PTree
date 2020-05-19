import heapq
from typing import Any
from dataclasses import dataclass, field


@dataclass(order=True)
class PriorityItem:
    priority: int
    item: Any = field(compare=False)


class EventQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def add_event(self, event):
        heapq.heappush(self.queue, event)

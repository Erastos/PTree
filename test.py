from EventQueue import EventQueue, PriorityItem
import urllib.request as http


def http_request(mess):
    result = http.urlopen(f"http://localhost:3000/{mess}")
    print(result.read().decode('utf-8'))


pr1 = PriorityItem(5, http_request)
pr2 = PriorityItem(10, http_request)
pr3 = PriorityItem(15, http_request)
pr4 = PriorityItem(7, http_request)

eq = EventQueue()
eq.add_event(pr1)
eq.add_event(pr2)
eq.add_event(pr3)
eq.add_event(pr4)

print(eq)


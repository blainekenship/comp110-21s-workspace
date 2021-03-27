"""Range Example"""

start: int = 0 
stop: int = 101
step: int = 10

a_range: range = range(start, stop, step)

print(f"Max value in range: {a_range[len(a_range) - 1]}")

print(a_range.start)
print(a_range.stop)
print(a_range.step)

a_range = range(10) #Stop is 10; start and step default is 1

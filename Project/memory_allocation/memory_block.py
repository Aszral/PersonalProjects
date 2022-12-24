from io_functions import *

# Represents memory block in the heap.
class MemoryBlock:
    def __init__(self, start_address, size, allocated=False):
        self.start_address = start_address
        self.end_address = start_address + size
        self.size = size
        self.allocated = allocated

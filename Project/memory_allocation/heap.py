from memory_block import *

# Represents the heap, which is a list of MemoryBlock objects
class Heap:
    def __init__(self, max_memory_size):
        self.max_memory_size = max_memory_size
        self.heap = [MemoryBlock(0, max_memory_size)]

    # Uses the first-fit strategy to allocate memory.
    def first_fit(self, max_memory_size):
        for block in self.heap:
            if not block.allocated and block.size >= max_memory_size:
                block.allocated = True
                self.split_block(block, max_memory_size)
                return block.start_address and block.end_address
        return "Error: No Suitable Block Found."

    # Uses the best fit strategy to allocate memory.
    def best_fit(self, max_memory_size):
        best_block = None
        for block in self.heap:
            if not block.allocated and block.size >= max_memory_size:
                if best_block is None or block.size < best_block.size:
                    best_block = block
        if best_block:
            best_block.allocated = True
            self.split_block(best_block, max_memory_size)
            return best_block.start_address and best_block.end_address
        return "Error: No Suitable Block Found."

    # Uses the worst fit strategy to allocate memory.
    def worst_fit(self, max_memory_size):
        worst_block = None
        for block in self.heap:
            if not block.allocated and block.size >= max_memory_size:
                if not worst_block or block.size > worst_block.size:
                    worst_block = block
        if worst_block:
            self.split_block(worst_block, max_memory_size)
            return worst_block.start_address and worst_block.end_address
        return "Error: No Suitable Block Found."

    # Splits given block into two, one for given size and one for the remaining size.
    def split_block(self, block, max_memory_size):
        self.heap.remove(block)
        if block.start_address + max_memory_size < self.max_memory_size:
            self.heap.append(MemoryBlock(block.start_address, max_memory_size, True))
            self.heap.append(
                MemoryBlock(
                    block.start_address + max_memory_size, block.size - max_memory_size
                )
            )
        else:
            self.heap.append(
                MemoryBlock(
                    block.start_address,
                    self.max_memory_size - block.start_address,
                    True,
                )
            )

    # TODO: Not sure if this is right
    def free_memory(self, start_address, end_address):
        for block in self.heap:
            if (
                block.start_address == start_address
                and block.end_address == end_address
            ):
                block.allocated = False
                # TODO: Logic tells me to somehow merge nearby blocks?
                return True
        return False


# TODO: Unsure if this function is needed or...
# Allocates memory of the given size using the given strategy.
def allocate(self, size, strategy):
    if size > self.max_memory_size:
        return "Error: requested allocation size is too big."
    match strategy:
        case "first-fit":
            return self.first_fit(size)
        case "best-fit":
            return self.best_fit(size)
        case "worst-fit":
            return self.worst_fit(size)


# TODO: This may belong in a separate file or just useless. Not sure...
# Executes all three allocation strategies
def allocate_memory(heap, size):
    print("First-fit allocation:")
    block = heap.allocate(size, "first-fit")
    if block is not None:
        print(f"Allocated block: {block}")
    else:
        print("Could not allocate memory using first-fit strategy.")

    print("\nBest-fit allocation:")
    block = heap.allocate(size, "best-fit")

    if block is not None:
        print(f"Allocated block: {block}")
    else:
        print("Could not allocate memory using best-fit strategy.")

    print("\nWorst-fit allocation:")
    block = heap.allocate(size, "worst-fit")
    if block is not None:
        print(f"Allocated block: {block}")
    else:
        print("Could not allocate memory using worst-fit strategy.")

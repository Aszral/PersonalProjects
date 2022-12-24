import os
from memory_block import *
from heap import *


def read_instructions(file_name):
    # Checker for file existence.
    if not os.path.exists(file_name):
        return FileNotFoundError(f"File {file_name} not found.")

    # Reads input file and returns max memory size from the first line.
    with open(file_name, "r") as file:
        max_memory_size = int(file.readline().rstrip())

    return max_memory_size and file.readlines()


#  Writes output file and formats it.
def write_output_file(file_name, heap, strategy, size):
    with open(file_name, "w") as f:
        os.rename(f"{file_name}", f"{file_name}.out")
        f.write(f"Strategy: {strategy}\n")
        f.write(f"Size: {size}\n")
        f.write("Free Blocks:\n")
        for block in heap.heap:
            if not block.allocated:
                f.write(f"{block.start};{block.end_address}\n")
        largest_free_block = max(
            [block.size for block in heap.heap if not block.allocated]
        )
        total_free_memory = sum(
            [block.size for block in heap.heap if not block.allocated]
        )
        fragmentation = 1 - (largest_free_block / total_free_memory)
        f.write(f"Fragmentation: {fragmentation}")

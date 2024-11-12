# сортировка Внешняя многофазная nlogn
import os
from my_sort import merge_sort


def divide_and_sort_to_files(input_file, block_size):
    block_number = 0
    with open(input_file, 'r') as file:
        while True:
            lines = file.readlines(block_size)
            if not lines:
                break

            data = [int(line.strip()) for line in lines]

            data = merge_sort(data)

            with open(f"block_{block_number}.txt", 'w') as block_file:
                for number in data:
                    block_file.write(f"{number}\n")
            block_number += 1


def merge_sorted_files(output_file, num_blocks):
    block_files = [open(f"block_{i}.txt", 'r') for i in range(num_blocks)]
    current_values = [int(file.readline().strip()) if file else None for file in block_files]

    with open(output_file, 'w') as output:
        while current_values.count(None) != num_blocks:
            min_value = min(value for value in current_values if value is not None)
            min_index = current_values.index(min_value)

            output.write(f"{min_value}\n")

            next_line = block_files[min_index].readline().strip()
            current_values[min_index] = int(next_line) if next_line else None

    for file in block_files:
        file.close()


def multiphase_sort_with_files(input_file, output_file, block_size):
    divide_and_sort_to_files(input_file, block_size)

    blocks = [f for f in os.listdir() if f.startswith("block_")]
    num_blocks = len(blocks)

    merge_sorted_files(output_file, num_blocks)
    for file_name in blocks:
        if os.path.exists(file_name):
            os.remove(file_name)


input_file = "input2.txt"
output_file = "sorted_output.txt"
block_size = 50

multiphase_sort_with_files(input_file, output_file, block_size)
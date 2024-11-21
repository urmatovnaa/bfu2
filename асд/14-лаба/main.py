#хеш-таблица со списками

def read_file(input_file):
    with open(input_file, 'r') as file:
        text = file.read()

    return text

def hash_function(word, table_size):
    return sum(ord(char) for char in word) % table_size

def create_hash_table(words, table_size):
    hash_table = [[] for i in range(table_size)]

    for word in words:
        hash_code = hash_function(word,table_size)
        hash_table[hash_code].append(word)

    return hash_table

def write_hash_table(hash_table, output_file):
    with open(output_file, 'w') as file:
        for hash_code, words in enumerate(hash_table):
            file.write(f"{hash_code}: {', '.join(words)}\n")


input_file = "input.txt"
output_file = "outputfile.txt"
table_size = 35

text = read_file("input.txt")
words = text.split()

table = create_hash_table(words, table_size)

write_hash_table(table, output_file)
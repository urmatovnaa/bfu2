#хеш-таблица с наложением/ с линейным пробиранием

def read_file(input_file):
    with open(input_file, 'r') as file:
        text = file.read()

    return text

def hash_function(word, table_size):
    return sum(ord(char) for char in word) % table_size

def create_hash_table(words, table_size):
    hash_table = [None] * table_size

    for word in words:
        hash_code = hash_function(word,table_size)
        origin = hash_code

        while hash_table[hash_code] is not None:
            hash_code = (hash_code + 1) % table_size
            if hash_code == origin:
                raise Exception("Хеш-таблица переполнена")

        hash_table[hash_code] = word

    return hash_table

def write_hash_table(hash_table, output_file):
    with open(output_file, 'w') as file:
        for hash_code, word in enumerate(hash_table):
            file.write(f"{hash_code}: {word if word is not None else ' '} \n")


input_file = "input.txt"
output_file = "outputfile.txt"
table_size = 50

text = read_file("input.txt")
words = text.split()

table = create_hash_table(words, table_size)

write_hash_table(table, output_file)
import re
from collections import defaultdict
from heapq import merge

def external_word_count(file_path, output_path, chunk_size=10**7):
    # Split the file into smaller sorted chunks
    chunks = []
    with open(file_path, 'r') as file:
        while True:
            lines = file.readlines(chunk_size)
            if not lines:
                break
            word_count = defaultdict(int)
            for line in lines:
                for word in re.findall(r'\w+', line.lower()):
                    word_count[word] += 1
            sorted_words = sorted(word_count.items())
            chunk_path = f'chunk_{len(chunks)}.txt'
            with open(chunk_path, 'w') as chunk_file:
                for word, count in sorted_words:
                    chunk_file.write(f'{word} {count}\n')
            chunks.append(chunk_path)

    # Merge the sorted chunks
    with open(output_path, 'w') as output_file:
        sorted_files = [open(chunk, 'r') for chunk in chunks]
        merged_lines = merge(*sorted_files, key=lambda line: line.split()[0])
        for line in merged_lines:
            output_file.write(line)
        for file in sorted_files:
            file.close()

def create_index(text):
    words = text.split()
    index = {}
    for position, word in enumerate(words, start=1):
        word = word.strip(",.?!").lower()  
        if word not in index:
            index[word] = []
        index[word].append(position)
    return index


document = "sample"
index = create_index(document)
for word, positions in index.items():
    print(f"{word}: {positions}")

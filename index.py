def create_index(text):
    words = text.split()
    index = {}
    for position, word in enumerate(words, start=1):
        word = word.strip(",.?!").lower()  # Normalize words
        if word not in index:
            index[word] = []
        index[word].append(position)
    return index

# Example usage
document = "This is a sample document. This docx:-"
index = create_index(document)
for word, positions in index.items():
    print(f"{word}: {positions}")

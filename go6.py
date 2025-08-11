def count_words(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        word = word.strip('.,!?()":;')
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count


def main():
    text = input("Введите текст: ")
    if not text.strip():
        print("Текст пуст!")
        return
    word_counts = count_words(text)
    print("Частота слов:")
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")
    print(f"Всего уникальных слов: {len(word_counts)}")


main()

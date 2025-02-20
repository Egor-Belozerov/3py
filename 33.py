from collections import Counter

def most_common_word(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()

    words = text.split()
    words = [word.strip(".,!?;:\"()[]") for word in words]

    word_counts = Counter(words)
    most_common = word_counts.most_common(1) 

    return most_common[0] if most_common else ("", 0)

file_path = r"C:\Users\Highlander\Desktop\10\1.txt"
word, count = most_common_word(file_path)
print(f"Самое частое слово: '{word}' (встречается {count} раз)")

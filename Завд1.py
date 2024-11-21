import nltk
import string
import matplotlib.pyplot as plt
from collections import Counter

# Перевірка та зчитування файлу
try:
    File = open('bryant-stories.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print("File not found!")
    exit(0)

text = File.read()


# Функція для підрахунку кількості слів
def count_words(text):
    sentences = nltk.sent_tokenize(text)
    k_words = 0
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        k_words += len(words)
    return k_words


# Функція для визначення найчастіше вживаних слів
def most_used_words(text):
    # Очищення тексту від пунктуації та переведення в нижній регістр
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()

    # Токенізація
    tokens = nltk.word_tokenize(cleaned_text)

    # Підрахунок найчастіше вживаних слів
    cnt = Counter(tokens)
    cort = cnt.most_common(10)

    # Побудова графіка
    x = [cort[el][0] for el in range(len(cort))]
    y = [cort[el][1] for el in range(len(cort))]

    plt.bar(x, y, color='blue')
    plt.title("10 Most Used Words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.show()


# Виклик функцій
nltk.download('punkt')  # Завантаження необхідних ресурсів для токенізації
nltk.download('punkt_tab')
total_words = count_words(text)
print(f"Total number of words in the text: {total_words}")
most_used_words(text)

nltk.download('stopwords')
translator = str.maketrans('', '', string.punctuation)
cleaned_text = text.translate(translator).lower()

# Токенізація тексту
tokens = nltk.word_tokenize(cleaned_text)

# Видалення стоп-слів
stop_words = set(nltk.corpus.stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

# Підрахунок найчастіше вживаних слів
word_counts = Counter(filtered_tokens)
most_common_words = word_counts.most_common(10)

# Побудова стовпчастої діаграми
words = [word[0] for word in most_common_words]
frequencies = [word[1] for word in most_common_words]

plt.bar(words, frequencies, color='skyblue')
plt.title("10 Most Used Words (After Removing Stop Words and Punctuation)")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
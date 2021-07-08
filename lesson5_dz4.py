# l5.dz4

from textblob import TextBlob
with open("text_4.txt", "r", encoding="utf-8") as f:
    blob = TextBlob(f.read())
with open("text_4ru.txt", "w", encoding="utf-8") as f:
    print(blob.translate(to="ru"), file=f)

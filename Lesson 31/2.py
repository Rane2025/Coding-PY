class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + " (" + self.meaning + ")"

flash = []

while(True):
    word = input("Enter the word: ")
    meaning = input("Enter the meaning: ")
    flash.append(flashcard(word, meaning))
    more = input("Do you want to add more flashcards? (yes/no): ")
    if more.lower() != 'yes':
        break
print("\nYour Flashcards:")
for card in flash:
    print(card)
print("\nThank you for using the flashcard app!")

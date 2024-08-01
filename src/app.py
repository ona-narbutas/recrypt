from src.classes.key_word import KeyWord
from src.classes.word import Word

def main():
    keyword = KeyWord("start")
    while(True):
        print(f"The word is: {keyword.word}")
        try:
            candidate = Word(input("What's next? "))
        except ValueError:
            print("Word not recognized")
        else:
            if keyword.validate_next(candidate):
                print("Valid!")
                keyword = KeyWord(candidate.word)
            else:
                print("Invalid, try again.")

if __name__ =="__main__":
    main()
 
class Flashcard:

    def __init__(self, question, answer):
        self.question = question
        self.answer=answer
        self.state =0
    
    def print(self):
        return self.question
    
    def show(self):
        return self.answer
    
    def edit(mode, string):
        if mode == "q":
            self.question = string
        if mode == "a":
            self.answer = string


def main():
    Flashcards = []
    ainput = ""
    while ainput != "q":
        
        q = input("enter a question ")
        a = input("enter an answer ")
        
        Flashcards.append(Flashcard(a,q))
        print(Flashcard(a,q).show())
        ainput = input("enter q to quit ")

    
main()

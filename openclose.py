from typing import List

class Question:
    def __init__(self, text: str, answer: str, *args, **kwargs):
        self.text = text
        self.answer = answer
        
    def display(self) -> None:
        raise NotImplementedError('Method "display" must be implemented on Question class')


class TrueFalse(Question):
    def display(self) -> None:
        print(self.text)
        print('Yes or No')


class MultiChoice(Question):
    def __init__(self, text: str, answer: str, choices: List[str]):
        super().__init__(text, answer)
        self.choices = choices

    def display(self) -> None:
        print(self.text)
        for (l, a) in zip(['A', 'B', 'C', 'D'], self.choices):
            print(f'{l}) {a}')
        

def display_questions(questions: List[Question]) -> None:
    print(f'Starting quiz with {len(questions)} questions...\n\n')
    for question in questions:
        question.display()
        print('-'*20, '\n')

if __name__ == '__main__':
    questions: List[Question] = [
            TrueFalse('Is my cat cute?', 'yes'),
            MultiChoice('What is my name?', 'Zsolt', ['Zsolt', 'Niki', 'Jani', 'Gabi'])
        ]
    display_questions(questions)

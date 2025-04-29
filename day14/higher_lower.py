score = 0

quiz = [
    {'question': 'A: Cristiano Ronaldo or B: Lionel Messi', 'answer': 'A'},
    {'question': 'A: Kylie Jenner or B: Selena Gomez', 'answer': 'B'},
    {'question': 'A: Kim Kardashian or B: Dwayne Johnson', 'answer': 'B'},
    {'question': 'A: National Geographic or B: Nike', 'answer': 'B'},
    {'question': 'A: Khloé Kardashian or B: Beyoncé', 'answer': 'B'},
    {'question': 'A: Taylor Swift or B: Justin Bieber', 'answer': 'B'},
    {'question': 'A: Virat Kohli or B: Jennifer Lopez', 'answer': 'A'},
    {'question': 'A: Neymar Jr. or B: Nicki Minaj', 'answer': 'A'},
    {'question': 'A: FC Barcelona or B: Real Madrid', 'answer': 'B'},
    {'question': 'A: NASA or B: NBA', 'answer': 'A'}
]


print('Higher or Lower')
print('There are 10 questions, which do you think has more followers, A or B?')

for num in range(10):
    actual_answer = quiz[num]['answer']
    given_answer = input(f'Question {num + 1}: {quiz[num]['question']}?')

    if given_answer == actual_answer:
        num += 1
        score += 1
        print(f"Correct!")
    elif given_answer != actual_answer:
        num += 1
        print('Incorrect')

print(f"Your score is {score}!")
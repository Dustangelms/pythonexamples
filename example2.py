input()


def ask_question(affirmative_phrase):
    print(affirmative_phrase + '?')


ask_question('Hello')

ask_question(affirmative_phrase_you_input)


def ask_question_but_worse(affirmative_phrase):
    def make_question(affirmative_phrase_same_same):
        locals_level_2 = locals()
        affirmative_phrase = 'something something'
        return affirmative_phrase_same_same + '?'

    locals_level_1 = locals()
    print(make_question(affirmative_phrase))


ask_question_but_worse(42)
make_question(42)

import re

result = re.findall(pattern = '\\b[a-z]*o[a-z]*', string = 'a quick brown fox jumps over the lazy dog')
del result
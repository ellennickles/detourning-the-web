import requests


def get_answers(my_phrase, my_character):
    url = 'https://duckduckgo.com/ac/'
    my_params = {'q': '%s' % my_phrase + '%s' % my_character}

    answers = requests.get(url, params=my_params).json()
    for answer in answers:
        print answer['phrase'].encode("utf-8")


my_phrase = 'the answer is '
letters = 'abcdefghijklmnopqrstuvwxyz'

for letter in letters:
    get_answers(my_phrase, letter)


letters1 = 'abcdefghijklmnopqrstuvwxyz'

for letter in letters:
    for letter1 in letters1:
        comboLetter = letter + letter1
        get_answers(my_phrase, comboLetter)

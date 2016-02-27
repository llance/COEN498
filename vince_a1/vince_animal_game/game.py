#!/usr/bin/env python

import json
import random
import copy
from models import Country

questions = {
    "Is the country located in North America?" : False,
    "Is the country located in South America?" : False,
    "Is the country located in Central America?" : False,
    "Is the country located in the Carribean" : False,
    "Is the country located in the Bahamas?" : False,
    "Is the official language of the country you're thinking about French" : False,
    "Is the official language of the country you're thinking about English" : False,
    "Is the official language of the country you're thinking about Spanish" : False,
    "Is the official language of the country you're thinking about Dutch" : False,
    "Is the official language of the country you're thinking about Danish" : False,
    "Is the country you're thinking about big ? (over 1 million square kilometer)" : False,
    "Is the country you're thinking about landlocked?" : False,
    "Is the population of the country over 1 million people?" : False,
}


def first_question():
    question = random.choice(questions.keys())
    allCountries = Country.objects.all()
    print(allCountries)
    return question


def get_question(questions, animals):
    """Select a question based on what will narrow the animal list the most."""
    true_counts = [len(animals) * -1 for i in animals[random.choice(animals.keys())]]
    false_counts = [len(animals) for i in animals[random.choice(animals.keys())]]
    for name, answers in animals.iteritems():
        for index, answer in enumerate(answers):
            if index not in questions.keys():
                true_counts[index] += 100
                continue

            if answer is True:
                true_counts[index] += 1
            elif answer is False:
                false_counts[index] -= 1

    counts = [abs(t - f) for t, f in zip(true_counts, false_counts)]

    print(counts)

    i = counts.index(min(counts))
    # don't ask question again
    q = questions.pop(i)
    return i, q


def guess_animal(animals):
    return random.choice(animals.keys())


def narrow_animals(animals, qindex, response):
    """Take entries out of the animals list based on the response to a
    question.
    """
    return {a: rs for a, rs in animals.iteritems()
            if animals[a][qindex] == response
            or animals[a][qindex] is None}


def fill_in_unknowns(data, responses):
    """Replaces unknowns about an animal in the data with answers from the
    user responses, if they exist. Returns new data.
    """
    return [x if x is not None else y for x, y in zip(data, responses)]


if __name__ == "__main__":
    jsondata = load_json()
    while True:
        # create safe-to-modify lists
        qs = jsondata["questions"]
        questions = {i: q for i, q in zip(range(len(qs)), qs)}
        animals = copy.deepcopy(jsondata["animals"])
        responses = [None for i in range(len(questions))]
        response_yes = None
        guess = None
        welcome()

        while True:
            # print(questions)
            print(animals.keys())
            # if there are no more questions or animals
            if len(animals) == 0:
                break
            elif len(animals) == 1 or not len(questions):
                guess = guess_animal(animals)
                question = u"Is your animal a " + guess + u"?"
            else:
                qindex, question = get_question(questions, animals)
            # prompt user for response
            response_yes = prompt_yes_or_no(question)
            if guess:
                break
            else:
                responses[qindex] = response_yes
                animals = narrow_animals(animals, qindex, response_yes)

        if not guess:
            newanimal = safe_input(u"You stumped me! What's your animal?")
            # store new animal along with user responses
            jsondata["animals"][newanimal] = responses
            print(u"Okay, I'll remember that one for next time.")
        elif not response_yes:
            newanimal = safe_input(u"Dang! What was your animal?")
            if newanimal in jsondata["animals"]:
                print(u"Oh, I know that animal!")
                data = jsondata["animals"][newanimal]
                jsondata["animals"][newanimal] = fill_in_unknowns(data, responses)
                print(u"Now I've learned more about it.")
            else:
                newi = len(questions)
                newquestion = safe_input(u"Okay, what's a question that is true for " + newanimal + u" but false for " + guess)

                # store new animal along with user responses
                jsondata["animals"][newanimal] = responses

                # store new question
                jsondata["questions"].append(newquestion)

                # put unknown answer to new question for all animals
                for animal, answers in jsondata["animals"].iteritems():
                    answers.append(None)

                # ...except yes for new animal, no for guessed animal
                jsondata["animals"][newanimal][-1] = True
                jsondata["animals"][guess][-1] = False
        else:
            print(u"YES! I RULE!")
            data = jsondata["animals"][guess]
            jsondata["animals"][guess] = fill_in_unknowns(data, responses)

        if not play_again():
            break
    save_json(jsondata)
    print(u"Thanks for playing! And remember... I'M GETTING SMARTER")
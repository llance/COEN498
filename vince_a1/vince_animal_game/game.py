#!/usr/bin/env python

import random
from models import Country
from models import Question

countryGuess = Country
filters = {}

def first_question():
    #Reset asked flag
    Question.objects.all().update(asked = False)
    #get random question
    query = random.choice(Question.objects.all())
    query.asked = True
    query.save()
    question = query.question
    return { 'question' : question }

def play(userInput):
    #Get user Input
    question = userInput['question']
    answer = userInput['answer']
    print(type(answer))
    if answer == True:
        #get the original question
        query = Question.objects.all().get(question = question)
        #eliminate similar questions
        print("Query category is")
        print(query.category)
        if (query.category == "LANGUAGE") or (query.category == "REGION"):
            if query.category == "LANGUAGE":
                Question.objects.filter(category="LANGUAGE").update(asked=True)
            if query.category == "REGION":
                Question.objects.filter(category="REGION").update(asked=True)

        filterString = query.query_field
        filterdict = eval(filterString)
        filters.update(filterdict)
    #Get next question
    query = random.choice(Question.objects.all())
    while query.asked == True:
        query = random.choice(Question.objects.all())
        print(Question.objects.all().filter(asked = False).count())
        if Question.objects.all().filter(asked = False).count() == 0:
            return end()
    query.asked = True
    query.save()
    question = query.question
    countries = Country.objects.all()
    print(Country.objects.all().filter(**kwargs))
    return { 'question' : question }


def end():
    print(filters)
    finalGuess = Country.objects.filter(**filters)
    print(finalGuess)
    if finalGuess:
        finalGuess = random.choice(finalGuess)
        return {'question' : "My final guess is : " + finalGuess.name + ". Thanks for playing"}
    else:
        finalGuess = random.choice(Country.objects.all()).name
        return {'question' : "I could not find an exact match, here is my blind guess : " + finalGuess}

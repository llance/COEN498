import web

db = web.database(dbn='sqlite', db='20q.db')

def get_object_by_id(id):
    '''Returns a Storage object containing an object where id=id.'''
    global db
    try:
        return db.select('objects', vars=locals(), where='id = $id')[0]
    except IndexError:
        return None

def get_question_by_id(id):
    '''Returns a Storage object containing a question where id=id.'''
    global db
    try:
        return db.select('questions', vars=locals(), where='id=$id')[0]
    except IndexError:
        return None
#
# def get_question_by_text(text):
#     '''Returns Storage object containing a question where text=text.'''
#     try:
#         return db.select('questions', vars=locals(), where='text=$text')[0]
#     except IndexError:
#         return None
#
def get_data_by_question_id(question_id):
    '''Returns an IterBetter all weights for a particular question_id, where each
       row is a Storage object.'''
    global db
    try:
        return db.select('data', vars=locals(), where='question_id=$question_id')
    except IndexError:
        return None


def get_questions():
    '''Returns an IterBetter of all the quesitons in the database, where each row is a Storage object.'''
    global db
    return db.select('questions')

def get_num_positives(object_tuple, question_id):
    '''Returns the number of objects in the object_tuple where the value for the
       given question_id is positive.'''

    global db

    assert type(object_tuple) == tuple

    where = 'object_id IN %s AND question_id=%d AND value >0' %(object_tuple, question_id)
    try:
        rows = db.select('data', vars=locals(), where=where, what='count(*) AS count')
        return rows[0].count
    except IndexError:
        return 0
#
def get_num_negatives(object_tuple, question_id):
    '''Returns the number of objects in the object_tuple where the value for the
       given question_id is negative.'''

    global db
    assert type(object_tuple) == tuple

    where = 'object_id in %s AND question_id=%d AND value <0' %(object_tuple, question_id)
    try:
        rows = db.select('data', vars=locals(), where=where, what='count(*) AS count')
        return rows[0].count
    except IndexError:
        return 0

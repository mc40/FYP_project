from flask import Flask
import spacy
app = Flask(__name__)
@app.route("/movies")
def GetMovies():
    return "Hello, World!"
@app.route('/movie/<sentence>', methods=['GET'])
def querBySentence(sentence):
    # print("type(sentence) : ", type(sentence))
    persons = []
    dates = []
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    for token in doc:
        print(token.text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            persons.append(ent.text)
        if ent.label_ == "DATE":
            dates.append(ent.text)
        print(ent.text, ent.label_)
        print('persons', persons)
        print('dates', dates)
    return 'String => {}'.format(sentence)
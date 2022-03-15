import spacy
import os
import sys
import pathlib

MODEL_PATH = "model"

def get_filepath():
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            return sys.argv[1]
        print("The file you entered does not exist, please enter another")
    print("Please a filepath to the instruction text")
    
def get_model():
    cwd = os.path.dirname(__file__)
    model_dir = os.path.join(cwd, MODEL_PATH)
    try:
        model = spacy.load(model_dir)
        return model
    except:
        print(f"Error loading model from {model_dir}")
    
def get_tyn(filepath):
    with open(filepath) as f:
        text = f.read()
    tyn = get_tyn_from_text(text)
    '''
    ner = get_model()
    if ner:
        doc = ner(text)
        return doc.ents
        '''
    return sorted(set(tyn))

def get_tyn_from_text(text):
    ner = get_model()
    nlp = spacy.load('en_core_web_sm')
    if ner and nlp:
        d1 = ner(text)
        results = d1.ents
        d2 = nlp(text)
        ents = set([ent.text for ent in d2.ents])
        tyn = [thing for thing in results if thing not in d2.ents]
        return tyn
        
# MAIN PROGRAM
if __name__ == "__main__":
    text_filepath = get_filepath()
    if text_filepath:
        print('Getting \'Things you need\' from instruction text in file at', text_filepath)
        tyn = get_tyn(text_filepath)
        if tyn:
            print('\'Things you need\' found in instruction text:')
            for thing in tyn:
                print(thing)
        else:
            print('No \'Things you need\' found')
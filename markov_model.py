import markovify # https://github.com/jsvine/markovify

def train():
    with open('test.txt') as f:
        text = f.read()
        # Build the model.
        # Don't retain original corpus. (Means sentences are often repeated instead of original)
        model = markovify.Text(text, state_size=3, retain_original=False)

    # ## Testing
    # # Print five randomly-generated sentences
    # for i in range(5):
    #     print(model.make_sentence())
    # # Print three randomly-generated sentences of no more than 140 characters
    # for i in range(3):
    #     print(model.make_short_sentence(140))

    ## Save model
    model_json = model.to_json()
    with open("models/model.json", "w+") as f:
        f.write(model_json)
    print('Model is trained and saved!')

def load():
    with open('models/model.json') as f:
        model_json = f.read()

    model = markovify.Text.from_json(model_json)

    # ## Testing
    # # Print five randomly-generated sentences
    # for i in range(5):
    #     print(model.make_sentence())
    # # Print three randomly-generated sentences of no more than 140 characters
    # for i in range(3):
    #     print(model.make_short_sentence(140))  

    return model

# Execute here
#train()
#load()
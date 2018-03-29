import markovify # https://github.com/jsvine/markovify

#MODEL_NAME = 'The_Donald'
MODEL_NAME = 'TwoXChromosomes'

MARKOV_SIZE = 2 # State size of markov model for training

def train():
    with open('generator/datasets/' + MODEL_NAME + '.txt', encoding="utf8") as f:
        text = f.read()
        # Build the model.
        # Don't retain original corpus. (Means sentences are often repeated instead of original)
        model = markovify.Text(text, state_size=MARKOV_SIZE, retain_original=False)

    ## Save model
    model_json = model.to_json()
    with open('generator/models/' + MODEL_NAME + str(MARKOV_SIZE) + '.json', 'w+', encoding="utf8") as f:
        f.write(model_json)
    print('Model is trained and saved!')

def load(model_name=MODEL_NAME):
    with open('generator/models/' + model_name + str(MARKOV_SIZE) + '.json', encoding="utf8") as f:
        model_json = f.read()

    model = markovify.Text.from_json(model_json)

    return model

def test(model):
    ## Testing
    # Print five randomly-generated sentences
    for i in range(5):
        print(model.make_sentence())
    # Print three randomly-generated sentences of no more than 140 characters
    for i in range(3):
        print(model.make_short_sentence(140))

def train_all():
    MODEL_NAME = 'The_Donald'
    MARKOV_SIZE = 2
    train()
    MARKOV_SIZE = 3
    train()
    MODEL_NAME = 'TwoXChromosomes'
    MARKOV_SIZE = 2
    train()
    MARKOV_SIZE = 3
    train()

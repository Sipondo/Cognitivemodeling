# Cognitive Modeling Week4

## Our Bot
We set out to create a BubbleBot: A chatbot which recognizes your political views and then responds with agreeable statements.
Although an anti-bubble bot would be a nicer product, we felt that disagreements and arguments tend to require more sophisticated
language than agreement.

We managed to technically meet our goal, albeit in a very limited form. Our bot tries to classify the statements made by the user
into either 'Democratic' or 'Republican' views based on Twitter data.
The bot then has a corresponding generative model for each view. Based on the classification, with bot creates a composite model of
the two, weighted depending on our classification. It generates responses from this model which try to take the input topic into
account.

The generated responses are simple Markov chains, and because we did little cleaning of the source data from Twitter and Reddit,
fairly ungrammatical. Responses also relate to the user input in a very superficial way, and are often generic.

## Examples
(See screenshots)
Hopefully something along the lines of:

>Hello
Hi!
Hey, so how do you feel about gun control?
>Damn libs will have to pry my guns from my cold, dead hands.
I know right? Lock her up!

## Setup
pip install ...
python -m textblob.download_corpora
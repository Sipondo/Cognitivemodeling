import json
from itertools import islice

SUBREDDIT = 'The_Donald'
FIELDS_SAVED = {'body', 'controversiality', 'score', 'subreddit'}

def extract_json(overwrite=False):
    if overwrite:
        open('datasets/' + SUBREDDIT + '.json', 'w').close()

    with open('datasets/RC_2017-06') as f:
        n = 1000
        # Iterate over n lines at a time for memory's sake
        for i in range(3):
            lines_gen = islice(f, i*n, (i+1)*n)
            new_lines = ''
            for line in lines_gen:
                j_content = json.loads(line)
                if j_content['subreddit'] == 'The_Donald':
                    new_line = json.dumps({key: val for (key, val) in j_content.items() if key in FIELDS_SAVED})
                    new_lines += new_line + '\n'
            # Save in every iteration for robustness
            with open('datasets/' + SUBREDDIT + '.json', 'a') as f_out:
                f_out.write(new_lines)

def json_to_corpus():
    with open('datasets/' + SUBREDDIT + '.json', 'r') as f:
        lines = f.readlines()
        with open('datasets/' + SUBREDDIT + '.txt', 'w+') as f:
            for line in lines:
                print(line)
                line_data = json.loads(line)
                print(line_data['body'])
                print(str(line_data['body'], "utf-8"))
                f.write(line_data['body'])


#extract_json(overwrite=True)
json_to_corpus()
print('Done')

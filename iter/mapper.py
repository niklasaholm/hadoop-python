#!/usr/bin/env python

import sys

def read_input(file):
    for line in file:
      yield line.split()

def main(seperator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        try:
            parsed_json = json.loads(words)
            pronouns = ['he', 'she', 'den', 'det', 'denna', 'denne', 'hen']
            if 'retweeted_status' not in parsed_json:
                text = data['text'].lower()
                text = text.split()
                for t in text:
                    for p in pronouns:
                        if t == p:
                            print '%s\t%s' % (p, 1)
        except:
            pass

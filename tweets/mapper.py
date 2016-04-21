#!/usr/bin/env python

import sys
import json
number_of_unique = 0
for line in sys.stdin:
    line = line.strip()
    try:
        
        parsed_json = json.loads(line)
        pronouns = ['han', 'hon', 'den', 'det', 'denna', 'denne', 
                    'hen', 'he', 'she']
        if 'retweeted_status' not in parsed_json:
            number_of_unique = number_of_unique + 1
            text = parsed_json['text'].lower()
            text = text.split()
            for t in text:
                for p in pronouns:
                    if t == p:
                        print '%s\t%s' % (p, 1)
    except:
        pass

print '%s\t%s' % (total, number_of_unique)

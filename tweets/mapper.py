#!/usr/bin/env python

import sys
import json
for line in sys.stdin:
    line = line.strip()

    try:
        parsed_json = json.loads(line)
        pronouns = ['he', 'och', 'vara', 'she', 'den', 'det', 'denna', 'denne', 'hen']
        if 'retweeted_status' not in parsed_json:
            text = parsed_json['text'].lower()
            text = text.split()
            for t in text:
                for p in pronouns:
                    if t == p:
                        print '%s\t%s' % (p, 1)
    except:
        pass

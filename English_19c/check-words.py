#!/usr/bin/env python

import glob
import pandas as pd
import re

if __name__ == '__main__':
    with open('words.txt') as f:
        words = set(w.rstrip() for w in f.readlines())
    print(len(words))
    files = glob.glob('Tokenized/*.txt')
    results = []
    for f in files:
        with open(f) as check_file:
            xs = [w.rstrip() for w in check_file.readlines() if not re.match(r'<(EOS|PGB)', w)]
            found = 0
            n = len(xs)
            uxs = set(xs)
            for x in xs:
                if x in words:
                    found += 1
            fields = check_file.name.split('/')[-1].split('_')
            author = fields[0]
            work = '_'.join(fields[1:])
            work = work.replace('.txt', '')
            results.append({'author': author, 'work': work, 'total tokens': n, 'percent of tokens found': found/n*100.0, 'unique tokens not in wordlist': len(uxs.difference(words))})
            print(f'{check_file.name}\t{found/n*100.0}')
    pd.DataFrame(results).to_csv('author-work-wordlist-check.csv', index=False)


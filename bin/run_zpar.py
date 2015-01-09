#!/usr/bin/env python
import plac

import nltk
from lib.corpus import Gigaword
from zpar import ZPar


@plac.annotations(
    giga_db_loc=("Path to the sqlite3 docs DB.", "positional"),
    n_docs=("Number of docs to process", "option", "n", int),
    pos_tag=("Do POS tagging?", "flag", "t", bool),
    parse=("Do parsing?", "flag", "p", bool),
)
def main(giga_db_loc, n_docs, pos_tag=False, parse=False):
    docs = Gigaword(giga_db_loc, limit=n_docs)
    sbd = nltk.data.load('tokenizers/punkt/english.pickle')
    from zpar import ZPar
    sbd = nltk.data.load('tokenizers/punkt/english.pickle')
    with ZPar('english') as z:
        tagger = z.get_tagger()
        for doc in docs:
            sentences = sbd.tokenize(doc)
            for sent in sentences:
                if pos_tag:
                    tags = tagger.tag_sentence(sent)
                    n = len(tags)
    print n


if __name__ == '__main__':
    plac.call(main)

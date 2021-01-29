# Information about the collection "Spanish_Am_19c"

The collection contains 60 Spanish American novels published in the 19th century (between 1840 and 1910).

The Tokenization was done with the script "tokenizer.py" (in the folder "Scripts"), the linguistic annotation was done with FreeLing. The trigrams were created with the script "trigrams.py" (in the folder "Scripts"). The mapping between the EAGLES-based FreeLing tagset and the UniversalPOS tagset was done with the script "map_pos.py" (in the folder "Scripts"). For the mapping, the es_eagles-plus_to_ud2.map was used.

* The folder "Tokenized" contains the full text of the novels in a "one-word-token-per-line" format. This includes a code for "end of sentence" <EOS>. Attention: The tokenization here does not necessarily correspond exactly to the tokenization done by the linguistic tagger FreeLing.

* The folder "Lemmatized" contains the full text of the novels in the format "one-lemma-per-line", based on the FreeLing annotation.

* The folder "UniversalPOS" contains the full text of the novels in the format "tUniversalPOS" per line.

* The folder "Universal_Tri" contains the full text of the novels in the format "one-trigram-per-line", based on "UniversalPOS".


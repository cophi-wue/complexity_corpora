# Japanese novels corpus

## Version information

Upload Date: 2019/5/31
Aozora Bunko:
aozora-corpus-generator:

## Text content

-   Two to six books per author, 12 authors.
-   All novels but Kawabata's are extracted from the HTML files of [Aozora Bunko](http://www.aozora.gr.jp/) using [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator). Kawabata works were created from ebooks.
-   List of authors (25 high-brow novels and 22 low-brow novels):
    -   High (6)
        -   Natsume Soseki (4)
        -   Dazai Osamu (2)
        -   Mori Ogai (3)
        -   Kobayashi Takiji (4)
        -   Tanizaki Jun'ichiro (6)
        -   Yasunari Kawabata (6) (*restricted; not from Aozora Bunko)
    -   Low (6)
        -   Yumeno Kyusaku (3)
        -   Edogawa Ranpo (4)
        -   Unno Juza (4)
        -   Okamoto Kido (5)
        -   Oguri Mushitaro (3)
        -   Sakaguchi Ango (3)

## Tokenized version

-   End of sentence marker is "<EOS>".
-   End of paragraph marker is "<PGB>".
-   One line per morpheme segmented using the morphological analyzer MeCab and [UniDic CWJ 2.2.0 dictionary](http://unidic.ninjal.ac.jp/download#unidic_bccwj). Special care is taken to:
    -   Identify so-called 'kanji-katakana-majiri-bun' sentences, in which katakana is used at the exclusion of katakana. This often results in tokenization errors.
-   By default, all symbols (punctuation) and numbers are removed.

## Plain version

-   One sentence per line with a linebreak in between paragraphs.

## Metadata

-   All metadata is included in the "groups.csv" file. Parts (brow and genre) are sourced from the manually specified 'author-title.csv' in the [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) repo, while the rest are extracted from the master list in the Aozora Bunko repo ('list_person_all_extended_utf8.zip'). The restricted corpus metadata is not in the repo.
-   Columns: textid, language, corpus, corpus_id, author_ja, title_ja, author, title, author_year, year, token_count, ndc, genre, comments, brow
    -   Note: the `year` column represents the publication date of the version of the work which the Aozora Bunko version is based off of and is not the first publishing date.

## Aozora Bunko issues/preprocessing in detail

See the provided [presentation](aozora-bunko-2018-01-22.pdf) and the readme from the [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) repo.

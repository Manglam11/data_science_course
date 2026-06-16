"""
NLP Basics with NLTK — Tokenization → N-grams → Stemming/Lemmatization
→ Stopwords → POS Tagging → Named Entity Recognition → Word Cloud

A clean, industry-standard walkthrough of the core NLTK toolkit.
Every step here uses the *correct* convention (e.g. POS-aware lemmatization,
full-sentence POS tagging) rather than the quick-demo shortcuts.

Author: Manglam  |  Mentor review: Claude Guruji
"""

# ----------------------------------------------------------------------
# 0. IMPORTS  (grouped: stdlib -> third party -> nltk submodules)
# ----------------------------------------------------------------------
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, wordpunct_tokenize
from nltk.util import ngrams
from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
from nltk import pos_tag, ne_chunk

from wordcloud import WordCloud
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# 1. ONE-TIME DATA DOWNLOAD
#    Run once, then comment out. These are the *data packs*, not the library.
# ----------------------------------------------------------------------
def download_nltk_data():
    for pkg in ["punkt", "punkt_tab", "wordnet", "omw-1.4", "stopwords",
                "averaged_perceptron_tagger_eng", "maxent_ne_chunker_tab", "words"]:
        nltk.download(pkg, quiet=True)


# ----------------------------------------------------------------------
# 2. SAMPLE TEXT
# ----------------------------------------------------------------------
AI = (
    "Artificial Intelligence refers to the intelligence of machines. "
    "This is in contrast to the natural intelligence of humans and animals. "
    "With Artificial Intelligence, machines perform functions such as "
    "learning, planning, reasoning and problem-solving."
)


# ----------------------------------------------------------------------
# 3. TOKENIZATION
# ----------------------------------------------------------------------
def tokenize_demo(text):
    words = word_tokenize(text)        # words + punctuation as separate tokens
    sentences = sent_tokenize(text)    # smart sentence split (punkt model)
    punct = wordpunct_tokenize(text)   # most aggressive: splits every punctuation
    print(f"word tokens     : {len(words)}")
    print(f"sentences       : {len(sentences)}")
    print(f"wordpunct tokens: {len(punct)}")
    return words


# ----------------------------------------------------------------------
# 4. N-GRAMS  (capture word order / context)
#    count of n-grams = N - n + 1
# ----------------------------------------------------------------------
def ngram_demo(tokens, n=2):
    grams = list(ngrams(tokens, n))
    print(f"{n}-grams ({len(grams)}): {grams[:3]} ...")
    return grams


# ----------------------------------------------------------------------
# 5. STEMMING vs LEMMATIZATION
#    Stemming = blind suffix chop (fast, may produce non-words)
#    Lemmatization = dictionary lookup (accurate, real words, needs POS)
# ----------------------------------------------------------------------
def _wordnet_pos(treebank_tag):
    """Map a Penn-Treebank POS tag to the tag WordNetLemmatizer expects."""
    if treebank_tag.startswith("J"):
        return wordnet.ADJ
    if treebank_tag.startswith("V"):
        return wordnet.VERB
    if treebank_tag.startswith("R"):
        return wordnet.ADV
    return wordnet.NOUN  # sensible default


def normalize_demo(words):
    stemmer = SnowballStemmer("english")   # preferred over Porter (improved + multilingual)
    lemmatizer = WordNetLemmatizer()

    # Best practice: lowercase, then lemmatize *with* the correct POS.
    tagged = pos_tag([w.lower() for w in words])
    stems = [stemmer.stem(w) for w, _ in tagged]
    lemmas = [lemmatizer.lemmatize(w, _wordnet_pos(t)) for w, t in tagged]

    print("sample stems :", stems[:8])
    print("sample lemmas:", lemmas[:8])
    return lemmas


# ----------------------------------------------------------------------
# 6. STOPWORD REMOVAL  (drop low-meaning filler words)
# ----------------------------------------------------------------------
def remove_stopwords(words, language="english"):
    sw = set(stopwords.words(language))           # set() -> fast lookups
    cleaned = [w for w in words if w.lower() not in sw and w.isalpha()]
    print("after stopword removal:", cleaned[:10], "...")
    return cleaned


# ----------------------------------------------------------------------
# 7. POS TAGGING  (tag the WHOLE sentence at once — context matters!)
# ----------------------------------------------------------------------
def pos_demo(sentence):
    tags = pos_tag(word_tokenize(sentence))       # NOT one token at a time
    print("POS tags:", tags)
    return tags


# ----------------------------------------------------------------------
# 8. NAMED ENTITY RECOGNITION  (tokenize -> pos_tag -> ne_chunk)
# ----------------------------------------------------------------------
def ner_demo(sentence):
    tree = ne_chunk(pos_tag(word_tokenize(sentence)))
    entities = [
        (" ".join(tok for tok, _ in subtree.leaves()), subtree.label())
        for subtree in tree
        if hasattr(subtree, "label")
    ]
    print("named entities:", entities)
    return entities


# ----------------------------------------------------------------------
# 9. WORD CLOUD  (font size = word frequency)
# ----------------------------------------------------------------------
def make_wordcloud(text, outfile="wordcloud.png"):
    wc = WordCloud(
        width=800, height=400, margin=2,
        background_color="black",
        colormap="viridis",     # smooth perceptual palette
        mode="RGBA",            # enables transparency support
    ).generate(text)

    plt.figure(figsize=(8, 4))
    plt.imshow(wc, interpolation="bilinear")  # smooths jagged edges
    plt.axis("off")                           # hide axis ticks/numbers
    plt.margins(x=0, y=0)                      # trim padding
    plt.tight_layout(pad=0)
    plt.savefig(outfile, dpi=150, bbox_inches="tight", facecolor="black")
    print(f"word cloud saved -> {outfile}")


# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
if __name__ == "__main__":
    download_nltk_data()

    print("\n--- TOKENIZATION ---")
    tokens = tokenize_demo(AI)

    print("\n--- N-GRAMS ---")
    ngram_demo(tokens, n=2)
    ngram_demo(tokens, n=3)

    print("\n--- NORMALIZATION (stem vs lemma) ---")
    normalize_demo(tokens)

    print("\n--- STOPWORD REMOVAL ---")
    remove_stopwords(tokens)

    print("\n--- POS TAGGING ---")
    pos_demo("My name is Manglam and I study data science")

    print("\n--- NAMED ENTITY RECOGNITION ---")
    ner_demo("The capital of India is New Delhi")

    print("\n--- WORD CLOUD ---")
    cloud_text = ("Python Python Python Matplotlib Matplotlib Seaborn Chart Chart "
                  "Chart Pandas Datascience Wordcloud Wordcloud Scatter Barplot")
    make_wordcloud(cloud_text)
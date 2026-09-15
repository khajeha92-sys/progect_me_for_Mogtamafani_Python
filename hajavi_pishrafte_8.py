#IN TEH NAME OF GOD
#MADE IN AMIRABAS KHAJEH FOR MR HAJAVI
#CLASS 8

import urllib.request
from collections import Counter
import re
import matplotlib.pyplot as plt


def get_text_from_url(url):
    """Fetches and returns text from a URL as a single string."""
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")


def clean_and_tokenize(text):
    """Processes a string of text and returns a generator of cleaned words."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    words = text.split()

    i = 0
    while i < len(words):
        yield words[i]
        i += 1


def count_words(word_iterable):
    """Takes an iterable of words and returns a Counter object."""
    word_counter = Counter()

    while True:
        try:
            word = next(word_iterable)
            word_counter[word] += 1
        except StopIteration:
            break

    return word_counter


def report_results(word_counter, top_n=5, word_to_check='the'):
    """Prints an analysis report and returns the top_n words."""

    print("Total unique words:", len(word_counter))
    print(f"Count of '{word_to_check}':", word_counter[word_to_check])

    top_commons = word_counter.most_common(top_n)

    print(f"\nTop {top_n} words:")
    i = 0
    while i < len(top_commons):
        print(top_commons[i][0], ":", top_commons[i][1])
        i += 1

    return top_commons


def visualize_top_words(top_commons, title_suffix=""):
    """Creates a bar chart from a List of (word, count) tuples."""

    words = []
    counts = []

    i = 0
    while i < len(top_commons):
        words.append(top_commons[i][0])
        counts.append(top_commons[i][1])
        i += 1

    colors = ["red", "green", "blue", "orange", "purple"]

    bars = plt.bar(words, counts, color=colors)

    i = 0
    while i < len(bars):
        plt.text(
            bars[i].get_x() + bars[i].get_width() / 2,
            bars[i].get_height(),
            str(counts[i]),
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold"
        )
        i += 1

    plt.title("Top Words " + title_suffix)
    plt.xlabel("Words")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()    
def main():
    url = "https://data.pr4e.org/romeo.txt"

    text = get_text_from_url(url)
    word_iterable = clean_and_tokenize(text)
    word_counter = count_words(word_iterable)
    top_commons = report_results(word_counter, top_n=5, word_to_check="the")
    visualize_top_words(top_commons)

###Driver Code ###
print('AMIRABAS KHAJEH')
main()

##MADE IN AMIRABAS KHAJEH

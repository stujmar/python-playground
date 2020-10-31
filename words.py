import sys
from urllib.request import urlopen


def fetch(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(items):
    for word in items:
        print(word)


def main():
    url = sys.argv[1]
    words = fetch(url)
    print_words(words)

if __name__ == '__main__':
    main()

# http://sixty-north.com/c/t.txt
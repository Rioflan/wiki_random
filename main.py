#!/usr/bin/python3

import requests, re, webbrowser

regex = r"^.*firstHeading.*?>(<.*?>)*(.*?)<.*$"

def get_page():
    r = requests.get('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard')
    matches = re.finditer(regex, r.text, re.MULTILINE)
    for match in matches:
        if not match.group(2):
            return (None, None)
        else:
            return (match.group(2), r.url)

result = []
for i in range(10):
    (a, b) = (None, None)
    while not a or not b:
        (a, b) = get_page()
    result.append((a, b))

for (i, value) in enumerate(result):
    print(i, value[0])

test_text = input ("Enter the page number: ")
test_number = int(test_text)

link = result[test_number][1]

webbrowser.open(link)

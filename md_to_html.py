import markdown
import os
import sys

print("--- Markdown to HTML ---")
fname = input("Enter  a file name: ")

if not os.path.exists(fname):
    print("Sorry, we couldn't find that file")
    sys.exit(1)

with open(fname, "r") as file:
    text = file.read()
    html = markdown.markdown(text)

html_fname = input("Where should we save the html? ")
with open(html_fname, "w") as file:
    file.write(html)

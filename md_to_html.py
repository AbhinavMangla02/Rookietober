import markdown

with open("README.md", "r") as file:
    text = file.read()
    html = markdown.markdown(text)

with open("README.html", "w") as file:
    file.write(html)

from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    doc = BeautifulSoup(file, "html.parser")

tags = doc.find_all("title")[0]

print(tags.string)
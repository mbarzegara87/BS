from bs4 import BeautifulSoup
import requests

search =str( input("search term: "))
params = {"q": search}
r = requests.get("https://www.bing.com/search?q=tango")
print(r.status_code)
#print(r.text)
f = open("./file.html", "w+")
#f.write(r.text)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})

if results is None:
    print("results was empty")
elif len(results) > 1:
    print("we have ", len(results), "results")
else:
    print(results)
links = results.findAll("li", {"class": "b_algo"})
# print(soup.prettify())
print(links)
for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attr["href"]
    if item_text and item_href:
        print(item_text)
        print(item_href)

print(len(links))

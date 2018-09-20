import requests
from bs4 import BeautifulSoup

my_list=[] #used to store the links

my_link="https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015"
# our link which we want to print
link=requests.get(my_link)
# requesting the link

obj=BeautifulSoup(link.content,"html.parser")
 #print the title of the webpage
print(obj.title)
my_list.append(obj.find_all('a'))
# collecting data/links on to list
#goes through each  'a' to get the reference
for i in obj.find_all('a'):
    print(i.get('href'))

#c=finds the table and prints the table data.
table = obj.find("table", { "class" : "wikitable sortable plainrowheaders" })
for row in table.findAll("tr"):
    cells = row.findAll("td")
    heading = row.findAll("th")
    # we are checking all contents in tables
    print(cells,heading)
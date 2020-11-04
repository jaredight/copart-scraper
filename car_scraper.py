import requests
import bs4
from bs4 import BeautifulSoup
import csv

page = requests.get("https://bids-history.com/search/")
pageContents = BeautifulSoup(page.content, 'html.parser')
listings = pageContents.select('.listing-item')

CarList = []

class Car:
    def __init__(self, price, condition, miles, title, location, estValue, model, damage):
        self.price = price
        self.condition = condition
        self.miles = miles
        self.title = title
        self.location = location
        self.estValue = estValue
        self.model = model
        self.damage = damage
    def  returnInfo(self):
        return [self.price, self.condition, self.miles, self.title, self.location, self.estValue, self.model, self.damage]

for listing in listings:
    price = listing.select_one('.g-rounded-3').get_text().replace('\n','')
    price = price.replace(' USD','').replace(',','').replace('$','')
    condition = listing.select_one('.g-rounded-50').get_text().replace('\n','')
    miles = listing.select_one('tr:nth-of-type(3) td:nth-of-type(2)').get_text().replace('\n','').replace(',','').replace(' MI','')
    title = listing.select_one('tr:nth-of-type(2) td:nth-of-type(2)').get_text()
    location = listing.select_one('tr:nth-of-type(1) td:nth-of-type(2)').get_text()
    estValue = listing.select_one('tr:nth-of-type(4) td:nth-of-type(2)').get_text()
    estValue = estValue.replace('\n','').replace('$','').replace(' USD','').replace(',','')
    model = listing.select_one('.vehicle-title a').get_text()
    damage = listing.select_one('.btn-sm-link:nth-of-type(1)').get_text()
    
    
    currCar = Car(price, condition, miles, title, location, estValue, model, damage)
    CarList.append(currCar)
    print(currCar.returnInfo())

    
# Function to output current results to CSV
def outputResults():
    writer = csv.writer('car-data')
    Headings = Car('price','condition','miles','title','location','estimated value','model','damage')
    writer.writerow(Headings.returninfo())
    for Car in CarList:
        writer.writerow(Car.returnInfo())
    return 0

outputResults()


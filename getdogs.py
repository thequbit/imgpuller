from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import csv
import sys

def getpage(url):
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)
    return soup

def getanimals(url):
    print "\tGetting page ..."
    soup = getpage(url)
    print "\tProcessing page ..."
    items = soup.findAll('td', attrs={'class': 'list-item'})
    print "\tFound {0} animals.".format(len(items))
    animals = []
    animals.append(("name","animalid","species","sex","bread","age","hidden","hasphto","photo"))
    for item in items:
        photo = item.find('div',attrs={'class': 'list-animal-photo-block'}).find('img')['src']
        info = item.find('div',attrs={'class': 'list-animal-info-block'})
        name = info.find('div',attrs={'class': 'list-animal-name'}).text
        animalid = info.find('div',attrs={'class': 'list-animal-id'}).text
        species = info.find('div',attrs={'class': 'list-anima-species'}).text
        sex = info.find('div',attrs={'class': 'list-animal-sexSN'}).text
        bread = info.find('div',attrs={'class': 'list-animal-breed'}).text
        age = info.find('div',attrs={'class': 'list-animal-age'}).text
        hidden = info.find('div',attrs={'class': 'hidden'}).text
        if "photo-not-available" in photo.lower():
            hasphoto = False
        else:
            hasphoto = True
        print "\tAdding '{0}' to the list.".format(name)
        animals.append((name,animalid,species,sex,bread,age,hidden,hasphoto,photo))
    return animals

def saveanimals(animals):
    success = True
    try:
        with open('dogs.csv','wb') as f:
            writer = csv.writer(f)
            writer.writerows(animals)
    except:
        success = False
    return success

def main(argv):
    if len(argv) != 2:
        print "Usage:\n\t> python getdogs.py <url>\n"
        return
    url = argv[1]
    print "Getting animals ..."
    animals = getanimals(url)
    print "Saving animals ..."
    saveanimals(animals)
    print "Done."

if __name__ == '__main__': sys.exit(main(sys.argv))

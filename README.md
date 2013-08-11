imgpuller
=========

Pulls image and animal data from petango.com to assist in photographing pets up for adoption


####Background####

Any time an action is performed more than a few times in the exact same way but on different data, it should be
scripted.  A friend asked me if this would be possible for some volenteer work that he does with taking photos
of animals up for adoption.  This is the result.

####Usage####

    > python getdogs.py "<url>"
    
    Where <url> will be something like:
    
    http://www.petango.com/webservices/adoptablesearch/wsAdoptableAnimals.aspx?species=Dog&sex=A&agegroup=All&shelter=NY343&onhold=A&orderby=ID&colnum=3&authkey=<authkey>
    
    Note: you should put the url in quotes since there are ampersands within the URL and the linux prompt will not
    interprete those they way you want it to .
    

####Dependencies####

The only dependency outside of the normal Python 2.7 package set is Beautiful Soup 4: http://www.crummy.com/software/BeautifulSoup/bs4/doc/

   > pip install BeautifulSoup4
   

####Outputs####

The tool will spit out a file called 'dogs.csv'.  This will contain a number of rows:

    name - The name of the animal (note: this is not a consistant field)
    
    animalid - The animal id number (I assume this is for internal use)
    
    species - The species of the animal
    
    sex - The gender of the animal
    
    bread - The bread of the animal
    
    age - The age of the animal (note: this is not a consistant field)
    
    hidden - A hidden field on the website, usually set to Foster or Adoption
    
    hasphoto - A True or False value to whether the animal has a photo or not
    
    photo - The URL of the animals photo (note: if there is no photo it will be set to a default one)
    

Enjoy!

from bs4 import BeautifulSoup
import urllib.request
import mysql.connector

#beginning of parsing data, will 
parser = 'html.parser' # or 'lxml' (preferred) or 'html5lib', if installed 
resp = urllib.request.urlopen("https://khn.org/news/lost-on-the-frontline-health-care-worker-death-toll-covid19-coronavirus/?fbclid=IwAR1cfrE9oo6U25yydH-t2A0egc_k05xkJfkW6S-5etLfdMAm8O86OXPleGA")
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

##isolateing the portion of the website that contians data that looks like
##<div class="col-xs-6 col-sm-6 col-md-6">
##<h3 style="font-size: 1.3em">Edwin Montanano</h3>
##<p><strong>Age:</strong> 73<br/>
##<strong>Occupation:</strong> Registered nurse<br/>
##<strong>Place of Work:</strong> Wellpath at Hudson County Correctional Center in Kearny, New Jersey<br/>
##<strong>Date of Death:</strong> April 5, 2020</p>
##</div>
##this is what bad divs contains ^^^^
##REMOVED ALL CASES WHERE THERE WAS NO PICTURE ##
baddivs = []
for divs in soup.find_all("div",class_="col-xs-6 col-sm-6 col-md-6"):
    #print(divs.find_previous("div"))
    if divs.find_previous("div"):
        baddivs.append(divs)

names = []
ages = []
occupation = []
workplace = []
deathdate = []

for what in baddivs:
    #this just gets the name
    names.append(what.find("h3").text.strip())
    #example of what yes looks like
    #['Age: 73', 'Occupation: Registered nurse', 'Place of Work: Wellpath at Hudson County Correctional Center in Kearny, New Jersey', 'Date of Death: April 5, 2020']
    yes = what.find("p").text.splitlines()
    div1 = yes[0] 
    div2 = yes[1]
    div3 = yes[2]
    div4 = yes[3]
    ages_ = div1[5:] 
    occupation_ = div2[12:]
    work_place = div3[15:]
    date_die = div4[15:]
    
    ages.append(ages_)
    occupation.append(occupation_)
    workplace.append(work_place)
    deathdate.append(date_die)
    
#print(names)
#print(ages)
#print(occupation)
#print(workplace)
#print(workplace[0])
#print(deathdate)
print(len(names))
print(len(ages))
print(len(workplace))
##getting images
image_source = []
for link in soup.find_all("img", recursive=True):
  if('400sq' in link['src']):
    image_source.append(link['src'])

#print(image_source)
print(len(image_source))


Smallwords = []


for lastshot in baddivs:
    #print(lastshot.find_previous("h3"))
    Smallwords.append(lastshot.find_previous("h3").text.strip())

print(len(Smallwords))
#print(Smallwords)

allofit = []



##for i in range(0,len(names)):
##    #cursor.execute("INSERT IGNORE INTO FRONTLINE (name, age, occupaton, workplace,deathdate,image,tribute) VALUES (%s, %s, %s, %s, %s, %s, %s) ",
##                   #(names[i],ages[i],occupation[i],work_place[i],deathdate[i],image_source[i],Smallwords[i]))
##    #mydb.commit()
##    #print("Record inserted successfully into Laptop table")
##    #insertVariblesIntoTable(names[i],ages[i],occupation[i],work_place[i],deathdate[i],image_source[i],Smallwords[i])
##    #print(names[i])
##    #print(ages[i])
##    #print(occupation[i])
##    #print(workplace[i])
##    #print(deathdate[i])
##    #print(image_source[i])
##    #print(Smallwords[i])
##    printstuff(occupation[i]) #,ages[i],occupation[i],work_place[i],deathdate[i],image_source[i],Smallwords[i])

mydb = mysql.connector.connect(host="localhost",
                            user="root",
                            password="435password",
                            database="python"
                            )
print(mydb)
cursor = mydb.cursor()
mySql_insert_query = """INSERT IGNORE INTO FRONTLINE (name, age, occupation, workplace,deathdate,image,tribute) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s) """
thecounter =0;
for i in range(0,len(names)):
    namez=names[i]
    agez=ages[i]
    occu=occupation[i]
    workin=workplace[i]
    dead =deathdate[i]
    image = image_source[i]
    wordz = Smallwords[i]
    #print(workin)
    #print(namez)
    #print(agez)
    #print(occu)
    #print(dead)
    #print(image)
    #print(wordz)
    cursor.execute(mySql_insert_query,(namez,agez,occu,workin,dead,image,wordz))
    mydb.commit()
    thecounter += cursor.rowcount
    #print(cursor.rowcount, "was inserted.")
    #print("\n")
print(thecounter, "was inserted.")

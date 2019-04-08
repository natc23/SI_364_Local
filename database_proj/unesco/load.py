import csv
import sqlite3

# python3 manage.py shell < many/load.py

from unesco.models import Site, Category, Region, Iso, States

fh = open('whc-sites-2018-small.csv')
rows = list(csv.reader(fh))



Site.objects.all().delete()
Category.objects.all().delete()
Region.objects.all().delete()
Iso.objects.all().delete()
States.objects.all().delete()


for row in rows[1:]:
    try:
        c = Category.objects.get(name=row[7])
    except:
        print("Inserting Category",row[7])
        c = Category(name=row[7])
        c.save()

    try:
        i = Iso.objects.get(name=row[10])
    except:
        print("Inserting iso",row[10])
        i = Iso(name=row[10])
        i.save()

    try:
        r = Region.objects.get(name=row[9])
    except:
        print("Inserting Region",row[9])
        r = Region(name=row[9])
        r.save()

    try:
        s = States.objects.get(name=row[8])
    except:
        print("Inserting States",row[8])
        s = States(name=row[8])
        s.save()

    try:
        y = int(row[3])
    except:
        y = None

    try:
        long = int(row[4])
    except:
        long = None

    try:
        lat = int(row[5])
    except:
        lat = None

    try:
        area = int(row[6])
    except:
        area = None

    # r = Membership.LEARNER
    # if row[1] == 'I' : r = Membership.INSTRUCTOR
    # m = Membership(role=r,person=p, course=c)
    # m.save()

    st = Site(name=row[0], category=c, iso=i, region=r, states=s, description=row[1], justification=row[2], year=y, longitude=long, latitude=lat, area_hectares=area)
    st.save()

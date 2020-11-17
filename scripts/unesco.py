import csv
from unesco.models import Category, State, Iso, Region, Site

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)
        name=row[0]#name
        des=row[1]#description
        jus=row[2]#justification
        year=row[3]#year
        lon=row[4]#longitude
        lat=row[5]#latitude
        area=row[6]#area_hectares
        a, created = Category.objects.get_or_create(name=row[7])#category
        a.save()
        b, created = State.objects.get_or_create(name=row[8])
        b.save()
        c, created = Region.objects.get_or_create(name=row[9])
        c.save()
        d, created = Iso.objects.get_or_create(name=row[10])
        d.save()

        #for year
        try:
            year = int(row[3])
        except:
            year = None

        #for longitude
        try:
            lon = float(row[4])
        except:
            lon = None

        #for latitude
        try:
            lat = float(row[5])
        except:
            lat = None

        #for area_hectares
        try:
            area = float(row[6])
        except:
            area = None

    #name,description,justification,year,longitude,latitude,area_hectares,category,states,region,iso

        site = Site(name = name ,description=des ,justification=jus, year=year, longitude=lon, latitude = lat,
        area_hectares=area ,category=a, states=b, region=c, iso=d)

        site.save()

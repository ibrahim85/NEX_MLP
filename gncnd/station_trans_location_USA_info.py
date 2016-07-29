# -*- coding: utf-8 -*-
from __future__ import print_function
"""
Created on Fri Jul 29 15:32:51 2016

@author: kitware
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 16:01:00 2016

@author: kitware
"""

import geocoder as geo
import geopy,sys
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import sys, json
import json, requests

geolocator = Nominatim()

import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def do_geocode(address):
    try:
        return geopy.geocode(address)
    except timeout:
        return do_geocode(address)

def LatLong_2_Location(lat_long):
    geolocator = Nominatim()
    location = geolocator.reverse(lat_long, timeout=30)

    print(location)

    ###City###
    print(location.raw)
    if isinstance(location.raw['address'], dict):
        if location.raw['address'].get('city')==None:
            city="UNKOWN"
        else:
            city=location.raw['address']['city']

        ###State###
        if location.raw['address'].get('state')==None:
            state="UNKOWN"
        else:
            state=location.raw['address']['state']

        if location.raw['address'].get('country')==None:
            country="UNKOWN"
        else:
            country=location.raw['address']['country']
    else:
        return ["UNKOWN","UNKOWN","UNKOWN"]

    return [city,state,country]

def main():
    glsT= open("USA_ghcnd-stations-loc_withInfo.txt","a+")

    with open("USA_ghcnd-stations-loc.txt","r") as gsT:
        for i,line in enumerate(gsT.readlines()):
            if i>1145:
                terms=line.split()

                geo_code=str(terms[1])+","+str(terms[2])
                url="http://localhost:8081/geocoder.html?ll="+geo_code
                url="http://demo.twofishes.net//geocoder.html?ll="+geo_code
                resp = requests.get(url)
                dataJson=resp.json()['interpretations'][0]
                featJson=dict(dict(dataJson)['feature'])
                if featJson.get('displayName')==None:
                    name1='Unkown'
                else:
                    name1=featJson.get('displayName').replace(" ","_")

                if featJson.get('name')==None:
                    name2='Unkown'
                else:
                    name2=featJson.get('name').replace(" ","_")

                city,state,country=LatLong_2_Location(geo_code)
                print(i,line)
                print(str(i)+">>"+terms[0]+" "+terms[1] +" "+terms[2]  +" "+name1 +" "+name2)
                glsT.write(terms[0]+" "+terms[1] +" "+terms[2]  +" "+name1 +" "+name2 +"\n")


                #glsT.write(terms[0]+" "+terms[1] +" "+terms[2]  +" "+city +" "+state +" "+country +"\n")
    glsT.close()

if __name__ == '__main__':
    main()




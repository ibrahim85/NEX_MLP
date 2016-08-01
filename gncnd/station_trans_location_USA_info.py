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

    #print(location)

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
    glsT= open("USA_ghcnd-stations-loc_city_states.txt","a+")

    with open("USA_ghcnd-stations-loc.txt","r") as gsT:
        for i,line in enumerate(gsT.readlines()):
            if i>=34734:
                terms=line.split()

                geo_code=str(terms[1])+","+str(terms[2])
                url="http://localhost:8081/geocoder.html?ll="+geo_code
                #url="http://demo.twofishes.net//geocoder.html?ll="+geo_code
                resp = requests.get(url)
                #print(json.dumps(resp.json(), indent=4))
                #print(len(resp.json()['interpretations'][0]))
                cityFeat=dict(dict(resp.json()['interpretations'][0])['feature'])
                stateFeat={}
                try:
                    stateFeat=dict(dict(resp.json()['interpretations'][1])['feature'])
                except IndexError:
                    stateFeat['name'] = None

                if cityFeat.get('displayName')==None:
                    city='Unkown'
                else:
                    city=cityFeat.get('displayName').replace(" ","_")

                if stateFeat.get('name')==None:
                    state='Unkown'
                else:
                    state=stateFeat.get('name').replace(" ","_")

                #city,state,country=LatLong_2_Location(geo_code)
                #print(i,line)
                print(str(i)+">>"+terms[0]+" "+terms[1] +" "+terms[2]  +" "+city +" "+state)
                linel=str(terms[0])+" "+str(terms[1]) +" "+str(terms[2])  +" "+city +" "+state +"\n"
                glsT.write((linel).encode('utf-8'))


                #glsT.write(terms[0]+" "+terms[1] +" "+terms[2]  +" "+city +" "+state +" "+country +"\n")
    glsT.close()

if __name__ == '__main__':
    main()




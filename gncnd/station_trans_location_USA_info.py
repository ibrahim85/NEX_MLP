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
    print(location.address)
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
def get_ID_list(fileName):
    id_list=[]
    with open(fileName,"r") as ft:
        for line in ft.readlines():
            id=str(line.split(",")[0])
            #print type(id),id
            id_list.append(id)
    return id_list
def main2():
    glsT= open("NewUSA_ghcnd-stations-loc_all.txt","a+")
    staID_list=get_ID_list("NewUSA_ghcnd-stations-loc_all.txt")
    with open("unknownStations.txt","r") as gsT:
        for i,line in enumerate(gsT.readlines()):
            if i>=0:
                terms=line.split(",")
                if terms[0] not in staID_list:
                    #term1 longitude  ;term2 latitude
                    geo_code=[]
                    geo_code.append(float(terms[1]))
                    geo_code.append(float(terms[2]))
                    g = geo.google(geo_code, method='reverse')
                    if g.city==None:
                        print(line)
                        continue
                    print(terms[0]+","+g.city+","+g.state+","+g.country)
                    linel=terms[0]+","+g.city+","+g.state+","+g.country+"\n"
                    glsT.write((linel).encode('utf-8'))
                    # print(str(i) + ">>" + terms[0] + " " + terms[1] + " " + terms[2] + " " + addr)
                    # linel = str(terms[0]) + " " + str(terms[1]) + " " + str(terms[2]) + " " + addr + "\n"
                    # glsT.write((linel).encode('utf-8'))



def main():
    glsT= open("USA_ghcnd-stations-loc_all.txt","a+")

    with open("USA_ghcnd-stations-loc.txt","r") as gsT:
        for i,line in enumerate(gsT.readlines()):
            if i>=0:
                terms=line.split()

                geo_code="\""+str(terms[1])+","+str(terms[2]+"\"")
                url="http://localhost:8081/geocoder.html?ll="+geo_code
                #url="http://demo.twofishes.net//geocoder.html?ll="+geo_code
                resp = requests.get(url)
                #print(json.dumps(resp.json(), indent=4))
                #print(len(resp.json()['interpretations'][0]))
                data=resp.json()['interpretations']
                levelNumber=len(data)
                addr=""
                if levelNumber >0:

                    for loc in data:
                        addr+=" "+loc['feature'].get('name').replace(" ","_")
                else:
                    print(i)
                    continue

                print(str(i)+">>"+terms[0]+" "+terms[1] +" "+terms[2]  +" "+addr)
                linel=str(terms[0])+" "+str(terms[1]) +" "+str(terms[2])  +" "+addr+"\n"
                glsT.write((linel).encode('utf-8'))


                #glsT.write(terms[0]+" "+terms[1] +" "+terms[2]  +" "+city +" "+state +" "+country +"\n")
    glsT.close()

if __name__ == '__main__':
    main2()




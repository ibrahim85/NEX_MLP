# -*- coding: utf-8 -*-
#import gmplot
#
##gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
#latitudes=[]
#longitudes=[]
#with open("USA_ghcnd-stations-loc_city_states.txt","r") as sF:
#    for line in sF.readlines():
#        terms=line.split()
#        latitudes.append(float(terms[1]))
#        longitudes.append(float(terms[2]))
#
#gmap.plot(latitudes, longitudes)
##gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
##gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
##gmap.heatmap(heat_lats, heat_lngs)
#
#gmap.draw("mymap.html")

from pygmaps_ng import *
import os


station={}
latitudes=[]
longitudes=[]
with open("USA_ghcnd-stations-loc_city_states.txt","r") as sF:
    for i,line in enumerate(sF.readlines()):
        terms=line.split()
        station[terms[0]]=i
        latitudes.append(float(terms[1]))
        longitudes.append(float(terms[2]))
print len(station)
for filename in os.listdir("/home/kitware/aalim/data/ncdc_data/2013ByDay_US_Temperature"):
    dlat=[]
    dlong=[]
    mymap = Map()
    app1 = App('test1',title="Station With Temp.")
    mymap.apps.append(app1)

    dataset1 = DataSet('data1', title="Show Stations" ,key_color='FF0088')
    app1.datasets.append(dataset1)
    with open("/home/kitware/aalim/data/ncdc_data/2013ByDay_US_Temperature/"+filename) as dayF:
        for line in dayF.readlines():
            sta=line.split()
            pt=[]
            pt.append(latitudes[station[sta[0]]])
            pt.append(longitudes[station[sta[0]]])
            #print filename
            if len(sta)==1:
                sta.append("--")
                sta.append("--")
            elif len(sta)==2:
                sta.append("--")


            #print "Station:"+sta[0]+"\nMin Temp:"+sta[1]+"\nMax Temp:"+sta[2]
            dataset1.add_marker(pt ,title="Show Stations",color="000000",text="Station:"+sta[0]+"\nMax Temp:"+sta[1]+"\nMin Temp:"+sta[2])
    mymap.build_page(center=pt,zoom=14,outfile="/home/kitware/aalim/data/ncdc_data/2013ByDayStationMap/"+filename.split("_")[0]+".html")
    print filename.split("_")[0]+".html"




#for i in range(len(latitudes)):
#    pt=[]
#    pt.append(latitudes[i])
#    pt.append(longitudes[i])
#    dataset1.add_marker(pt ,title="click me",color="000000",text="<a href='http://en.wikipedia.org/wiki/New_York'>New York!</a>")
#
#mymap.build_page(center=pt,zoom=14,outfile="NYC.html")
print "Hi"
import urllib2
import json

def addressInJson(locality = ""):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+locality
    response = urllib2.urlopen(url)
    data = json.load(response)   
    return data
    
def spacer():
    print 2 * '\n'            

def fetchLocalityDetails(locality = ""):
    dt = addressInJson(locality = locality) 
    frmtdata = dt.get('results')[0]
    print frmtdata.keys()
    spacer()
    ls = frmtdata.get("address_components")
    print ls
    
    spacer()
    dct = {}
    for dt in ls:
        dct.setdefault(locality, []).append(dt.get('long_name').encode("Ascii"))

    print dct

###############################################
locality = "New+York"
fetchLocalityDetails(locality = locality)
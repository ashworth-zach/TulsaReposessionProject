from django.shortcuts import render,redirect
import urllib.request, json
from openalpr import Alpr
from argparse import ArgumentParser
import base64
with urllib.request.urlopen("https://www.cityoftulsa.org/apps/opendata/OpenData_VehicleTowList.jsn") as url:
    data = json.loads(url.read().decode())
def index(request):
    context={
        'data':data['TowList']['TowNotice']
    }
    return render(request,'mainapp/index.html',context)

def find(request):
    newdata=[]
    for dict in data['TowList']['TowNotice']:
        if dict['TagNumber'].startswith(request.POST['tagstartswith']):
            newdata.append(dict)
    context={
        'data':newdata
    }
    return render(request,'mainapp/search.html',context)
def processimage(request):
    post=request.POST['canvasData']
    image =base64.b64decode(post)
    filename = 'image.png'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(image)
    parser = ArgumentParser(description='OpenALPR Python Test Program')

    parser.add_argument("-c", "--country", dest="country", action="store", default="us",
                    help="License plate Country" )

    parser.add_argument("--config", dest="config", action="store", default="/etc/openalpr/openalpr.conf",
                    help="Path to openalpr.conf config file" )

    parser.add_argument("--runtime_data", dest="runtime_data", action="store", default="/usr/share/openalpr/runtime_data",
                    help="Path to OpenALPR runtime_data directory" )

    parser.add_argument('plate_image', help='License plate image file')

    options = parser.parse_args()
    alpr = None
    try:
        alpr = Alpr('us', filename, options.runtime_data)

        if not alpr.is_loaded():
            print("Error loading OpenALPR")
        else:
            print("Using OpenALPR " + alpr.get_version())

            alpr.set_top_n(7)
            alpr.set_default_region("us")
            alpr.set_detect_region(False)
            jpeg_bytes = open(filename, "rb").read()
            results = alpr.recognize_array(jpeg_bytes)

            # Uncomment to see the full results structure
            # import pprint
            # pprint.pprint(results)

            print("Image size: %dx%d" %(results['img_width'], results['img_height']))
            print("Processing Time: %f" % results['processing_time_ms'])

            i = 0
            platenumber = results['results'][0]['candidates'][0]['plate']
            newdata=[]             
            for dict1 in data['TowList']['TowNotice']:
                if dict1['TagNumber'].startswith(str(platenumber)):
                    newdata.append(dict1)
            print(platenumber)
            context={
                'platenumber':platenumber,
                'data':newdata
            }
            for plate in results['results']:
                i += 1
                print("Plate #%d" % i)
                print("   %12s %12s" % ("Plate", "Confidence"))
                for candidate in plate['candidates']:
                    prefix = "-"
                    if candidate['matches_template']:
                        prefix = "*"

                    print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

    finally:
        if alpr:
            alpr.unload()
    return render(request, 'mainapp/recognition.html', context)
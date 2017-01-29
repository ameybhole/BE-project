import android

droid = android.Android()

droid.startLocating()
print "reading GPS ..."
event = droid.eventWaitFor('location',10000).result
if event['name'] == "location":
  try:
    lat = str(event['data']['gps']['latitude'])
    lng = str(event['data']['gps']['longitude'])
  except KeyError:
    lat = str(event['data']['network']['latitude'])
    lng = str(event['data']['network']['longitude'])    
  latlng = 'lat: ' + lat + ' lng: ' + lng
  print latlng

droid.stopLocating()


droid.startLocating()


event = droid.eventWaitFor('location',10000).result
Wait up to 10000ms for location event to occur.

  lat = str(event['data']['gps']['latitude'])
  lng = str(event['data']['gps']['longitude'])
Get the lat and lng information.

droid.stopLocating()

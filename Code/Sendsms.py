
# Import required libraries
import urllib      # URL functions
import urllib2     # URL functions

# Reading file from GPS server
file = open("/home/pi/Desktop/GPSC/file2","r")
file_data = file.read()
finaldata = file_data[118:138]+file_data[59:80]


# Define your message
message = "Accident happened at  " + finaldata +"   Put this in Google Map "
print "Your message is on way.."
# Set your username and sender name.
# Sender name must alphanumeric and 
# between 3 and 11 characters in length.
username = 'nagelparveen@gmail.com'
sender = 'parveen'

# Your unique hash is available from the docs page
# https://control.txtlocal.co.uk/docs/
hash = '2f802e3698b006cc2be9cedee58441499322a1f6'

# Set the phone number you wish to send
# message to.
# The first 2 digits are the country code.
# 44 is the country code for the UK
# Multiple numbers can be specified if required
# e.g. numbers = ('447xxx123456','447xxx654321')
numbers = ('00919920723683')

# Set flag to 1 to simulate sending
# This saves your credits while you are
# testing your code.
# To send real message set this flag to 0
test_flag = 0

#-----------------------------------
# No need to edit anything below this line
#-----------------------------------

values = {'test'    : test_flag,
          'uname'   : username,
          'hash'    : hash,
          'message' : message,
          'from'    : sender,
          'selectednums' : numbers }

url = 'http://www.txtlocal.com/sendsmspost.php'

postdata = urllib.urlencode(values)
req = urllib2.Request(url, postdata)

print 'Attempt to send SMS ...'

try:
  response = urllib2.urlopen(req)
  response_url = response.geturl()
  if response_url==url:
    print 'SMS sent!'
except urllib2.URLError, e:
  print 'Send failed!'
  print e.reason




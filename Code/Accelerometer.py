# ADXL345 Python 
import time
from adxl345 import ADXL345
  
adxl345 = ADXL345()
while True:
	axes = adxl345.getAxes(True)
	print "ADXL345 on address 0x%x:" % (adxl345.address)
	a = "   x = %.3fG" % ( axes['x'] )
	b = "   y = %.3fG" % ( axes['y'] )
	c = "   z = %.3fG" % ( axes['z'] )
        print a
	print b
	print c
 	x = a[7:12]
 	y = b[7:12]
	z = c[7:12]
        if(float(x) > 1 or float(y) > 1 or float(x) < -1 or float(y) < -1):
		import Sendsms
		break
	time.sleep(1)

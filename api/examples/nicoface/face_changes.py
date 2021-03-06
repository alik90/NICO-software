# Author: Erik
#
# Example for generating different face expression with wavelets
#
from nicoface.FaceExpression import faceExpression
import time
import timeit

#Change your interface here
fe = faceExpression()

# Chnange betwee two faces

for i in range(2,-1,-1):
    fe.setCommMode(i)
    #Generate the mouth form and eyebrowse
    # Using the standard values
    fe.mouth = fe.gen_mouth()
    fe.left = fe.gen_eyebrowse(type="l")
    fe.right = fe.gen_eyebrowse(type="r")
    fe.send()

    time.sleep(0.05)


    #Using both tuples for two mouth lines
    fe.mouth = fe.gen_mouth((1.0,-0.8,1.0,0),(None,None,None,None))
    fe.left = fe.gen_eyebrowse((-0.9,0,1,0),type="l")
    fe.right = fe.gen_eyebrowse((-0.9,0,1,0),type="r")

    fe.send()

    time.sleep(0.05)

for i in range (0,12,2):
    w1=1.0-0.24*i
    w2 = -0.8 + 0.15 * i
    #w2=0.2
    fe.mouth = fe.gen_mouth((w1, w2, 1.0, 0), (None, None, None, None))
    fe.send("m")
    time.sleep(0.001)

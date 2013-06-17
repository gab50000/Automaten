#!/usr/bin/python

#~ import numpypy
import numpy as np
import argparse
import pdb
import random
import Image
# looking at a site and its two neighboring sites: 
#there are 8 possible combinations: 0 0 0, 0 0 1, 0 1 0, ....
#for each combination the resulting site may be 0 or 1
#-> 2**8 possible rules 

#rule 0: every combination -> 0 (boring...)
#rule 1: 000 -> 1, everything else -> 0
#rule 2: 010 -> 1 , everything else -> 0
#rule 3: 010 -> 1 and 000 -> 1, everything else -> 0

def combitoint(array):
	return array[0]*4+array[1]*2+array[2]
	
def inttobin(number):
	if number>255:
		raise Exception
	else:
		binrepr=[]
		divisor=128
		while divisor>0:
			binrepr.append(number/divisor)
			if number/divisor:
				number-=divisor
			divisor/=2
	return binrepr

def create_rule(rulenumber):
	binrepr=inttobin(rulenumber)
	rules=dict()
	for state in range(8):
		rules[state]=(binrepr[-state-1]==1)
	return rules

def transition_periodic(nparray, rules):
	for i in xrange(1,len(nparray[0])-1):
		nparray[1][i]=rules[combitoint(nparray[0][i-1:i+2])]	
	nparray[1][0]=rules[4*nparray[0][-1]+2*nparray[0][0]+nparray[0][1]]
	nparray[1][-1]=rules[4*nparray[0][-2]+2*nparray[0][-1]+nparray[0][0]]
	
parser=argparse.ArgumentParser(description="1D lattice automaton, output as textfile")
parser.add_argument("-l", "--arraylength", default=50, type=int, help="array length")
parser.add_argument("-i", "--iterations", type=int, default=10000, help="number of iterations")
#~ parser.add_argument("rules", type=int, help="which rule(s) to apply?")
#parser.add_argument("--frames", "-f", type=int, default=0, help="number of parsed frames")
args = parser.parse_args()
#~ pdb.set_trace()
for rulenumber in xrange(256):
	nparray=np.zeros((args.iterations+1, args.arraylength), bool)
	for i in range(len(nparray[0])):
		nparray[0][i]=random.randint(0,1)==1
	rules=create_rule(rulenumber)

	for i in xrange(1,args.iterations+1):
		transition_periodic(nparray[i-1:i+1,:], rules)
	print "rule_"+str(rulenumber)
	nparray.dtype=np.uint8
	bild=Image.fromarray(nparray*255)
	bild.save("rule_"+str(rulenumber)+".png")

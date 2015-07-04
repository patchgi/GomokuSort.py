# coding: utf-8

# Python2.X encoding wrapper (Windows dedicated processing)
import codecs
import sys
import random
import time
sys.stdout = codecs.getwriter('cp932')(sys.stdout)

SCALE=5
turn =True

cells=[[0 for i in xrange(SCALE)]for j in xrange(SCALE)]

def put(_x,_y):
	putStone=0
	global turn
	if turn:
		print "yagi"
		putStone=1
	else:
		putStone=2
		cells[_x][_y]=putStone

def puttable(_x,_y):
	if 0>_x and _x<SCALE and 0>_y and _y>SCALE:
		return False
	if cells[_x][_y]!=0:
		return False
	return True

def drawBoard():
	raw=[" " for i in xrange(SCALE+1)]
	raw[SCALE]=" ====="
	for i in xrange(SCALE):
		for j in xrange(SCALE):
			if cells[j][i]==0:
				raw[i]+="_"
			if cells[j][i]==1:
				raw[i]+="o"
			if cells[j][i]==2:
				raw[i]+="*"

		print raw[i]
	print raw[SCALE]

if __name__=="__main__":
	drawBoard()
	while (True):
		if turn:
			while (True):
				input=raw_input()

				if input!=None:
					if len(input)==3:
						input=input.split(" ")
						if len(input)==2:
							if puttable(int(input[0]),int(input[1])):
								break
							else:
								print "Syntax Error"

						else:
							print "Syntax Error"

					else:
						print "Syntax Error"


			posX=int(input[0])
			posY=int(input[1])
			put(posX,posY)
			#turn =not turn
		else:
			while(True):
				eposX=random.randint(0,SCALE-1)
				eposY=random.randint(0,SCALE-1)
				if puttable(eposX,eposY):
					break

			print str(eposX)+" "+str(eposY) 
			put(eposX,eposY)
		
		drawBoard()
		time.sleep(1)
		turn =not turn

		



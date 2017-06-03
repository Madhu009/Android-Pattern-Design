import numpy as np 

data=np.linspace(1,10,9,endpoint=False)
data=np.reshape(data,(3,3))

imposmoves=[]
finalset=set()
l=[]
pos_patterns=[]
for r in range(0,3):
	for c in range(0,3):
		digit_impos_moves=set()
		for co in range(0,3):
			digit_impos_moves.add(data[r,co])
		for ro in range(0,3):
			digit_impos_moves.add(data[ro,c])
		imposmoves.append(digit_impos_moves)

def findpos_moves(imposmoves):
	s=set(np.arange(1,10))
	pos_moves=[]
	for d in imposmoves:
		pos_moves.append(list(s.difference(d)))
	return pos_moves

pos_moves=findpos_moves(imposmoves)

#Recursive depth first (Android Pattern Design)
def patterndesign(digit):
	if digit not in finalset:
		finalset.add(digit)
		l.append(digit)
		for d in pos_moves[digit-1]:
			patterndesign(d)
		if len(finalset) is not 9 and len(finalset) is not 1:
			finalset.remove(digit)
			l.remove(digit)
		elif len(finalset) is 9:
			l1=l.copy()	
			pos_patterns.append(l1)
			finalset.remove(digit)
			l.remove(digit)
		else:
			return
	else:
		return


patterndesign(5)
for i in pos_patterns:
	print(i)





		



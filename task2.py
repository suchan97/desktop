def load_txt(text):
	a=open(text+'.txt', 'r') #open txt file
	b=[] #make list 'b'. will be content of txt file
	b=a.readlines() #read txt file
	b = list(map(str.strip, b)) #remove last of each row '\n'
	b = list(map(list, b)) #split str
	num_len=len(b) #len(b)=len(b[0])
	a.close() #close txt file
	return b, num_len #load_txt(text)[0]=b, load_txt(text)[1]=num_len

def route(text, x, y): #x,y is coordinate
	if(text[x][y]=='1'):
		return 0
	if(x == y == len(text)-1):
		return 1
	if(x == len(text)-1):
		return route(text, x, y+1)
	if(y == len(text)-1):
		return route(text, x+1, y)
	return route(text, x, y+1) + route(text, x+1, y)

def main(text):	
	num_direction=0 #set possible num of route
	state=True #set inital state
	b=load_txt(text)[0]
	num_len=load_txt(text)[1]

	if (b[0][0]=='1') | (b[num_len-1][num_len-1]=='1'):
		num_direction=0
		state=False

	if state:
		print(route(b,0,0))
	else:
		print(num_direction)

main(str(input()))
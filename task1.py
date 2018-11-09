def load_txt(text):
	a=open(text+'.txt', 'r') #open txt file
	b=[] #make list 'b'
	b=a.readlines() #read txt file
	b = list(map(str.strip, b)) #remove last of each row '\n'
	b = list(map(list, b)) #split str
	a.close()
	return b

def find_right(b, x_var, y_var): #check right side '1'
	for i in range(len(b[x_var])-y_var-1):
		if b[x_var][y_var+i+1]=='1':
			x=i
			if find_down(b, x_var, y_var, x):
				return True
			else:
				continue
	return False

def find_down(b, x_var, y_var, x): #check down side '1' when right side have '1'
	for i in range(len(b)-x_var-1):
		if b[x_var+i+1][y_var+x+1]=='1':
			y=i
			if find_left(b, x_var, y_var, x, y):
				return True
			else:
				continue
	return False

def find_left(b, x_var, y_var, x, y): #check last point is '1' when find_down is True
	if b[x_var+y+1][y_var]=='1':
		return True
	else:
		return False

def main(text):
	b=load_txt(text)
	state=False #initial return value
	for i in range(len(b)-1):
		for j in range(len(b[0])-1): #check without last row and colum
			if b[i][j]=='1': #if loop reach '1' cehck right side '1'
				if find_right(b, i, j):
					state=True
					return state
	return state

print(main(str(input())))
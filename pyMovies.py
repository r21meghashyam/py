'''
	PY MOVIES program by Meghashyam
	Started on 27 AUG 2016
	Continued on 23 Sept 2016
'''
import os  
FILE_A='admins.txt'
FILE_U='users.txt'
FILE_M='movies.txt'

if os.path.exists(FILE_A)==0:
	open(FILE_A,'w').close()
if os.path.exists(FILE_U)==0:
	open(FILE_U,'w').close()
if os.path.exists(FILE_M)==0:
	open(FILE_M,'w').close()


print("::pyMovies::")
username=input("Enter username: ");#Accept username 
password=input("Enter password: ");#accept password

def Pass(stored,entered,count):
	if stored==entered:
		return 1
	else:
		count+=1
		if count>2:
			print("Failed to login")
			return 0
		password=input('Invalid Password!.\nEnter password:')
		return Pass(stored,password,count)

#check if user is an admin
def login(username,password,file):
	file=open(file,'r')
	while 1:
		line=file.readline()
		if line=='':
			file.close()
			return 0
		list=line.split(' ')
		if list[0]==username:
			file.close()
			return Pass(list[1],password,0)

def ts(text):
	l=len(text)
	if l>13:
		text=text[:-3]+'...'
	else:
		text=text+(' '*(15-l))
	return text


def shows():
	print('Shows:')
	print(ts('Screen')+ts('Movie')+ts('Total Seats')+ts('Seats Available'))
	file=open(FILE_M,'r')
	while 1:
		movie=file.readline()
		if movie=='':
			file.close()
			return 0
		list=movie.split(' ')
		print(ts(list[0])+ts(list[1].replace('_',' '))+ts(list[2])+ts(str(int(list[2])-int(list[3]))))
def edit():
	screen_no=int(input('Enter screen number: '))
	file=open(FILE_M,'r')
	doc=''
	change=found=0
	while 1:
		movie=file.readline()
		if movie=='':
			file.close()
			if found==0:
				print('You havent yet built that screen')
			break
		list=movie.split(' ')
		if int(list[0])==screen_no:
			found=1
			print('Screen Number: '+list[0])
			print('Movie Name: '+list[1].replace('_',' '))
			print('Total seats: '+list[2])
			print('Seats booked: '+list[3])
			print('Operations:')
			print('1. Change Movie')
			print('2. Change Total seats')
			ch=int(input('Enter option: '))
			if ch==1:
				list[1]=input('Enter movie name: ').replace(' ','_')
				change=1
			elif ch==2:
				seats=input('Enter new number of seats: ')
				if seats<int(list[3]):
					print('Too late! '+list[3]+' seats already booked!')
				else:
					list[2]=seats
					change=1
			else:
				print('Invalid option')
			doc+=list[0]+' '+list[1]+' '+list[2]+' '+list[3]
		else:
			doc+=movie
	if change==1:
		file=open(FILE_M,'w')
		file.write(doc)
		file.close()
		print('Changes Saved')
		
def Admin():
	print('1. View Shows')
	print('2. Edit')
	print('3. Exit')
	ch=int(input('Enter your choice:'))
	if ch==1:
		shows()
	elif ch==2:
		edit()
	elif ch==3:
		print('See you soon!')
		exit()
	else:
		print('Invalid Option!')
	Admin()

	
def addUser(username,password):
	file=open(FILE_U,'a')
	file.write('\n'+username+' '+password)
	file.close()
	print('Account Created :)')

def book():
	screen_no=int(input('Enter screen number: '))
	file=open(FILE_M,'r')
	doc=''
	change=found=0
	while 1:
		movie=file.readline()
		if movie=='':
			file.close()
			if found==0:
				print('Oops! Screen not found!')
			break
		list=movie.split(' ')
		if int(list[0])==screen_no:
			found=1
			available=int(list[2])-int(list[3])
			print('Screen Number: '+list[0])
			print('Movie Name: '+list[1].replace('_',' '))
			print('Total seats: '+list[2])
			print('Available seats: '+str(available))
			seats=int(input('Enter number of seats to be booked: '))
			if seats>available:
				print('Not enough seats available')
			else:
				list[3]=int(list[3])+seats
				change=1
			doc+=list[0]+' '+list[1]+' '+list[2]+' '+str(list[3])+'\n'
		else:
			doc+=movie
		
	if change==1:
		file=open(FILE_M,'w')
		file.write(doc)
		file.close()
		print('Changes Saved')
	
	
	
def User():
	print('1. View Shows')
	print('2. Book tickets')
	print('3. Logout')
	ch=int(input('Enter option: '))
	if ch==1:
		shows()
	elif ch==2:
		book()
	elif ch==3:
		print('See you soon!')
		exit()
	else:
		print('Invalid Option!')
	User()
	

if login(username,password,FILE_M):
	print('Hello Admin. Long time no seen :)')
	Admin()
elif login(username,password,FILE_U):
	print('Hello '+username)
	User()
else:
	ch=input('Seems like you are new here, Should we register you?(Y/N): ')
	if ch.upper()=='Y':
		print('Lets Roll')
		addUser(username,password)
		User()
	else:
		print('See you soon!')
		exit()
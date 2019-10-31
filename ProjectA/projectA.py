List_of_codes=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
List_of_Names=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
List_of_creditHours=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
List_of_sem=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def isValidCourseCode(i):
	Uppercase_Characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	Numeric_Characters=['0','1','2','3','4','5','6','7','8','9']
	if (i[0:1] in Uppercase_Characters) and (i[2:3:4] in Numeric_Characters):
		return True
	return(i)
def isValidName(i):
	Uppercase_Characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	if i[0] in Uppercase_Characters:
		return True
	return(i)
def isValidCreditHours(i):
	Num=['1','2','3']
	if (i in Num):
		return True
	return(i)
def isValidsemesters(i):
	available_sem=['0','1','2','3','4','5','6','7','8']
	if (i in available_sem):
		return True
	return(i)
def Add_Course():
	List_of_codes[y]=x
	List_of_Names[y]=z
	List_of_creditHours[y]=p
	List_of_sem[y]=k
	t=[x,z,p,k]
	print("your course details have been submitted as: ",t)
	return()
def Update_Course():
	u=0
	while u<y:
		print(u+1,List_of_codes[u],List_of_Names[u],List_of_creditHours[u],List_of_sem[u])
		u+=1
	d=int(input("course to be changed: "))
	if d<=y:
		x,z,p,k=input("enter your details(Course Code/Course Name/Credit Hours/Semesters ):  ").split()
		if ((isValidCourseCode(x) is True) and (isValidName(z) is True) and (isValidCreditHours(p) is True) and (isValidsemesters(k) is True)):
			List_of_codes[d-1]=x
			List_of_Names[d-1]=z
			List_of_creditHours[d-1]=p
			List_of_sem[d-1]=k
			print("your course has been updated")
		else:
			print("invalid course details")
			x,z,p,k=input("enter your details again(Course Code/Course Name/Credit Hours/Semesters ):  ").split()
			if ((isValidCourseCode(x) is True) and (isValidName(z) is True) and (isValidCreditHours(p) is True) and (isValidsemesters(k) is True)):
				List_of_codes[d-1]=x 
				List_of_Names[d-1]=z
				List_of_creditHours[d-1]=p
				List_of_sem[d-1]=k
				print("your course has been updated")
			else:
				print("still invalid, couldn't update course")
	else:
		print("course doesn't exxist")
def Delete_Course():
	u=0
	while u<=y:
		print(u+1,List_of_codes[u],List_of_Names[u],List_of_creditHours[u],List_of_sem[u])
		u+=1
	d=int(input("course to be deleted: "))
	if d<y:
		List_of_codes[d-1]=0
		List_of_Names[d-1]=0
		List_of_creditHours[d-1]=0
		List_of_sem[d-1]=0
		List_of_codes[d-1] = List_of_codes[u-1]
		List_of_Names[d-1]= List_of_Names[u-1]
		List_of_creditHours[d-1] = List_of_creditHours[u-1]
		List_of_sem[d-1] = List_of_sem[u-1]
		List_of_codes[u-1]=0
		List_of_Names[u-1]=0
		List_of_creditHours[u-1]=0
		List_of_sem[u-1]=0
	else:
		print("_course does not exist_")
def View_Courses():
	s=0
	print("COurse_CODE  ","Course_NAME  ","CREDIT_HOURS  ","SEMESTER")
	while s<y:
		print(str(List_of_codes[s])+"           "+str(List_of_Names[s])+"          ",str(List_of_creditHours[s])+"         ",str(List_of_sem[s]))
		s+=1
def View_Courses_of_a_semester():
		s=str(input("choose semester: "))
		print("COURSE_CODE ","COURSE_NAME ","CREDIT_HOURS ")
		e=0
		while e<y:
			if s==List_of_sem[e]:
				print((List_of_codes[e])+"        "+(List_of_Names[e])+"             "+str(List_of_creditHours[e]))
			e+=1
		if s not in List_of_sem:
			print("no course of semeter "+ s +" exists")
print("***Welcome to the University learning management system***")
y=0
while True: 
	print("1 ","add corse")
	print("2 ","update course")
	print("3 ","Delete course")
	print("4 ","View all courses")
	print("5 ","View courses of a semester")
	print("6 ","Exit program")	
	g=int(input("Choose the option: "))
	if g==1:
		x,z,p,k=input("enter details(Course Code/Course Name/Credit Hours/Semesters ):  ").split()
		if ((isValidCourseCode(x) is True) and (isValidName(z) is True) and (isValidCreditHours(p) is True) and (isValidsemesters(k) is True)):
			Add_Course()
		else:
			print("Invalid Details")
			x,z,p,k=input("enter course details again(Course Code/Course Name/Credit Hours/Semesters ):  ").split()
			if ((isValidCourseCode(x) is True) and (isValidName(z) is True) and (isValidCreditHours(p) is True) and (isValidsemesters(k) is True)):
				Add_Course()
			else:
				print("still invalid details, couldn't add course")
				y-=1
		y+=1
	if g==2:
		Update_Course()
	if g==3:
		Delete_Course()
		y-=1
	if g==4:
		View_Courses()
	if g==5:
		View_Courses_of_a_semester()
	if g==6:
		quit()
	print("_____________________________________________________________________________________________")
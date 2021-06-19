
class Newstudent:
    def __init__(self):
        self.Name = self.setName()
        self.Family =self.setFamily()
        self.Major =self.setMajor()
        self.stdid = self.setstdid()
        self.Age =self.setAge()
       
    def setName(self):
       
         return(input('enter Name:'))
    def setFamily(self):
       
         return(input('enter Family:'))
    def setMajor(self):
     
         return(input('enter Major:'))
    def setstdid(self):
       
         return(int(input('enter student ID :')))
    def setAge(self):
    
         return(int(input('enter age:')))
    

class main:

    def __init__(self,listlenght):
        self.listlen = listlenght
        self.stlist = []
    def savestudent(self) :
        for i in range(self.listlen):
            student = Newstudent()   
            self.stlist.append(student)
    def search(self,stdid) :
        flag = 0
        for student in self.stlist:
            if student.stdid == stdid:
                print('student with ID ='+str(stdid)+'is in the student list')
                flag = 1
                break
        if flag == 0:
            print('there is no student with ID ='+str(stdid)+'is in the student list')
    def deletestudent(self,stdid):
        for student in self.stlist:
            if student.stdid == stdid:
                self.stlist.remove(student)
                break
    def changestudent(self,stdid):
        for student in self.stlist:
          if student.stdid == stdid:
              student.Name = input('enter new Name :')
              student.Family = input('enter new Family :')
              student.Major = input('enter new Major :')
              student.Age= int(input('enter new age :'))
              break
    def showlist(self):
        print('students in list:')
        print()
        i = 1
        for student in self.stlist:
               print('student\t'+str(i)+'\tName:\t',student.Name)
               print('student\t'+str(i)+'\tFamily:\t',student.Family)
               print('student\t'+str(i)+'\tMajor:\t',student.Major)
               print('student\t'+str(i)+'\tAge:\t',student.Age)
               print('student\t'+str(i)+'\tstudent id:\t',student.stdid)
               i+=1
               print('--------------------------------------------------')
               print('--------------------------------------------------')
app = main(5)


print("\n============================================================\n")
print("\n============================================================\n")
print("\n======== ^ welcome to student management system ^ ==========\n")
print("\n============================================================\n")
print("\n============================================================\n")

print("\n1.Accept Student details\n2.Display Student Details\n" 
 "3.Search Details of a Student\n4.Delete Details of Student" 
  "\n5.Update Student Details\n6.Exit")

while(True): 
    ch = int(input("Enter choice:"))
    print(ch == 1)
    if(ch == 1):
        app.savestudent()
    elif(ch == 2):
        app.showlist()
    elif(ch == 3): 
        app.search(int(input('enter student ID :')))
    elif(ch == 4): 
        app.deletestudent(int(input('enter student ID :')))
    elif(ch == 5): 
        app.changestudent(int(input('enter student ID :')))
    elif(ch==6):
        print("\n=============================================================================\n")
        print("\n=============================================================================\n")
        print("\n======== * Thank you for choosing this student management system * ==========\n")
        print("\n=============================================================================\n")
        print("\n=============================================================================\n")

        break
    else:
        print('invalid input')
    


#Pat 7 ques1 python program 
#function will create a text file with current timestamp
# import datetime to get current time stamp
import datetime; 
# creating function 
def create_file(filepath): 
  #open function to create file at given location 
  f=open(filepath,"x") 
  #to calculate current time stamp
  currenttimestamp=str(datetime.datetime.now()) 
  #to write in file
  f.writelines(currenttimestamp)
  #to close the file
  f.close()
#user will enter file path
filepath=input("enter file path") 
#call of function
create_file(filepath) 


#Pat 7 ques 2 write python function to read from text file. function will take filename and display the text of file in console
# creating function to read and display content of file and file name as argument
def readfile(filename): 
    #variable to store file path and use of Fstring to contatnate strings
    path=f"C:\\Users\e3019715\\pythonfiles\\{filename}" 
    #to read content of file
    f=open(path,"r") 
    #return content of file
    return(f.read()) 


#file name entered through use
filename=input ("enter file name") 
#function call with argument of filename
readfile(filename) #function call with argument of filename

		
    
    
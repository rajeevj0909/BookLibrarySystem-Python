#Turns the database file into a list
def file_to_list():
    database_list=[]
    database_file=open("database.txt","r")
    #Reads every line
    for line in database_file:
        book_entry=[]
        start_pointer=0
        #In each line, it goes through every character looking for "~"  
        for index in range(len(line)):
            if line[index]=="~":
                #When found, it adds the string between the 2 "~" to a list
                end_pointer=index
                item=line[start_pointer:end_pointer]
                start_pointer=end_pointer+1
                #These 5 elements are added to the one list
                book_entry.append(item)
        #Each book is added to the database       
        database_list.append(book_entry)
    header=database_list[0]
    #Deletes the database header from the list (ID:Title:Author:PurchaseDate:MemberID:)
    del database_list[0]
    database_file.close()
    #Returns the header and all the data
    return (header,database_list)

#Used by the checkout file
def withdraw(search_book_id,search_member_id):
    database_all=file_to_list()
    header=database_all[0]
    database_list=database_all[1]
    #Writes the header to the file
    database_file=open("database.txt","w")
    for element in header:
        database_file.write(element+":")
    database_file.write("\n")
    #Writes the data back to the file
    for book in database_list:
        #For the book that needs changing
        if int(book[0])==int(search_book_id):
            database_file.write(book[0]+"~")
            database_file.write(book[1]+"~")
            database_file.write(book[2]+"~")
            database_file.write(book[3]+"~")
            #The ID is updated
            database_file.write(search_member_id+"~\n")
        #For all other books, it is added back normally
        else:
            for element in book:
                database_file.write(element+"~")
            database_file.write("\n")
    database_file.close()
    #It is important that the log_file gets updated too, popularity increments
    add_to_log(int(search_book_id))

#Used by the returns file
def return_to_file(book_id,header,database_list):
    #Writes the header to the file
    database_file=open("database.txt","w")
    for element in header:
        database_file.write(element+"~")
    database_file.write("\n")
    #Writes the data back to the file
    for book in database_list:
        #For the book that needs changing
        if int(book[0])==int(book_id):
            database_file.write(book[0]+"~")
            database_file.write(book[1]+"~")
            database_file.write(book[2]+"~")
            database_file.write(book[3]+"~")
            #The ID is updated to 0 (Available)
            database_file.write("0~\n")
        #For all other books, it is added back normally
        else:
            for element in book:
                database_file.write(element+"~")
            database_file.write("\n")
    database_file.close()

#Turns the loglist file into a list
def log_to_list():
    log_list=[]
    logfile=open("logfile.txt","r")
    #Reads every line
    for line in logfile:
        log_entry=[]
        start_pointer=0
        #In each line, it goes through every character looking for "~"  
        for index in range(len(line)):
            if line[index]=="~":
                #When found, it adds the string between the 2 "~" to a list
                end_pointer=index
                item=line[start_pointer:end_pointer]
                start_pointer=end_pointer+1
                #These 5 elements are added to the one list
                log_entry.append(item)
        #Each entry is added to the list       
        log_list.append(log_entry)
    logfile.close()
    #Returns all the data
    return log_list

#This function is ran by the withdraw function
def add_to_log(book_id):
    #It creates a list of all the data in the logfile
    log_list=log_to_list()
    #For each entry
    for entry in log_list:
        #For the entry that needs changing
        if int(entry[0])==book_id:
            #It increments the popularity points
            value=int(entry[1])
            value=value+1
            value=str(value)
            entry[1]=value
    #Once the list is updated, it's written back to the file
    logfile=open("logfile.txt","w")
    for entry in log_list:
        for element in entry:
            logfile.write(element+"~")
        logfile.write("\n")
    logfile.close()

#This function is to initialise the logfile
#Can be used if the software was to be used in libraries across the world
def setup_logfile():
    database_all=file_to_list()
    logfile=open("logfile.txt","w")
    database_list=database_all[1]
    for book in database_list:
        logfile.write(book[0]+"~1~\n")
    logfile.close()

if __name__=="__main__":
    '''This displays incorrectly in the shell but
    shows fine in the tkinter window.'''
    print(file_to_list())
    withdraw("1","9999")
    return_to_file("1",(file_to_list())[0],(file_to_list())[1])
    print(log_to_list())
    add_to_log("1")

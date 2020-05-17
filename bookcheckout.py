from database import *
#Ran when the book checkout submit button is clicked.
def availability(search_book_id,search_member_id):
    #This list just contains all the data, not the database heading
    database_list=(file_to_list())[1]
    answer=("Please try again.")
    try:
        #Validation checks
        if (int(search_book_id)>0) and (int(search_member_id)>999 and int(search_member_id)<10000):
            for book in database_list:
                book_id=int(book[0])
                #If the books is found
                if int(book_id)==int(search_book_id):
                    found=True
                    answer=""
                    member_id=str(book[4])
                    #Either the book is unavailable
                    if int(member_id)!=0:
                        answer=("\nBook is unavailable.\nCurrently on loan by Member: "+member_id+" \n")
                    #Or the book is available and it is withdrawn
                    elif int(member_id)==0:
                        answer=("\nBook is available!\nBook has been checked out!\n")
                        #The book ID and member ID are passed to the withdraw function in database.py
                        withdraw(search_book_id,search_member_id)
            if found ==False:
                answer=("Please try again.")
        else:
            answer=("Please try again.")
    except:
        answer=("Please try again.")

    return(answer)
        
if __name__=="__main__":
    '''This displays incorrectly in the shell but
    shows fine in the tkinter window.'''
    print(availability("1","4321"))#Normal case
    print(availability("5","4321"))#Normal case
    print(availability("1","53425432"))#The following are stress tests
    print(availability("1","gfdsgfds"))
    print(availability("54325423","4321"))





 

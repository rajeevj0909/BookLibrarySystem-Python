from database import *
#Ran when the book return submit button is clicked.
def return_book(book_id):
    database_all=file_to_list()
    header=database_all[0]
    database_list=database_all[1]
    answer=""
    try:
        #Validation
        if (int(book_id)>0):
            for book in database_list:
                if int(book_id)==int(book[0]):
                    found=True
                    #If the books is already available do nothing
                    if int(book[4])==0:
                           answer=("Already available")
                    else:
                        #Returns the book, function found in database.py
                        return_to_file(book_id,header,database_list)
                        answer=("Returned")
                
        if found==False:
            answer=("Please try again")
    except:
        answer=("Please try again")

    return (answer)

if __name__=="__main__":
    '''This displays incorrectly in the shell but
    shows fine in the tkinter window.'''
    print(return_book("5"))#Normal case
    print(return_book("4"))#Normal case
    print(return_book("100"))#The following are stress tests
    print(return_book("-1"))
    print(return_book("0.5"))

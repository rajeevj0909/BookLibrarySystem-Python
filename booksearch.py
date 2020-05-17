from database import *
#Ran when the booksearch submit button is clicked.
def submit_button(search_item,user_choice):
        try:
            #This list just contains all the data, not the database heading
            database_list=(file_to_list())[1]
            search_item=search_item.lower()
            found=0
            answer=""
            answer_list=[]
            #Decides what the user wants to search by
            if user_choice=="Book ID":
                choice=0
            elif user_choice=="Title":
                choice=1    
            elif user_choice=="Author":
                choice=2
            elif user_choice=="Purchase Date":
                choice=3
            elif user_choice=="Member ID":
                choice=4
            for book in database_list:
                attribute=book[choice]
                attribute=attribute.lower()
                #Looks for search item and assembles a string
                if attribute==search_item:
                    found=found+1
                    answer="\nWe found your book!\nHere are the details:\nBook ID:\
                        "+book[0]+"\nBook Title:         "+book[1]+"\nBook Author: \
                        "+book[2]+ "\nBook Purchase Date:   "+book[3]+"\n"
                    #Checks book availability
                    if book[4]=="0":
                        answer=  answer+"  Book is currently available.\n \n "
                    else:
                        answer=  answer+"Currently being loaned by Member:  "+book[4]+"\n"
                    answer_list.append(answer)
            if found==0:
                    answer_list=["Nothing could be found"]
        except:
          answer_list=["Please try again"]
                    
        return(answer_list)

if __name__=="__main__":
    '''This displays incorrectly in the shell but
    shows fine in the tkinter window.'''
    print(submit_button("The Hobbit","Title"))#Normal case
    print(submit_button("The Hobbit","Book ID"))#Title can't be found in ID
    print(submit_button("1984","Title"))#1 Title with 2 different authors
    print(submit_button("Harper Lee","Author"))#Test for another attribute
    print(submit_button("0","Member ID"))# All Available books

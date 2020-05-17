from database import *
#Ran when the 4th button on the homepage is clicked.
def list_books():
    log_list=log_to_list()
    for book in log_list:
        book[1]=int(book[1])
    database_list=(file_to_list())[1]
    titles_list=[]
    popularity_list=[]
    #Adds the log_list into 2 separate lists
    for book in log_list:
        id_num=int(book[0])-1
        if (database_list[id_num])[1] not in titles_list:
            titles_list.append((database_list[id_num])[1])
            popularity_list.append(book[1])
        #It also totals up the popularity of any books with the same titles
        else:
            for i in range(len(titles_list)):
                if titles_list[i]==database_list[id_num][1]:
                    popularity_list[i]=popularity_list[i]+log_list[id_num][1]
    #Adds these 2 lists back to a loglist so it can be sorted correctly
    log_list=[]
    for i in range(len(titles_list)):
        log_list.append([titles_list[i],int(popularity_list[i])])
    #Orders it by 2nd item- Order of popularity
    log_list.sort(key = lambda x: x[1],reverse=True)
    titles_list=[]
    popularity_list=[]
    #Then changes it back to 2 lists so that it can be used as the x and y axis
    for book in log_list:
        titles_list.append(book[0])
        popularity_list.append(book[1])
    return (titles_list,popularity_list)


#Used when the mouse is hovering over a title
def title_search(search_item):
    database_list=(file_to_list())[1]
    search_item=search_item.lower()
    found=0
    answer=""
    '''Searches the database for the book with the same title.
    If more than 1 book with same title exists, information
    for all books are displayed'''
    for book in database_list:
        attribute=book[1]
        attribute=attribute.lower()
        if attribute==search_item:
            found=found+1
            answer=answer+"\nBook ID:\
                "+book[0]+"\nBook Title:         "+book[1]+"\nBook Author: \
     "+book[2]+ "\nBook Purchase Date:   "+book[3]+"\n"
            if book[4]=="0":
                answer=  answer+"  Book is currently available.\n \n "
            else:
                answer=  answer+"Currently being loaned by Member:  "+book[4]+"\n"
        
                
    if found==0:
        answer="Invalid Input"
    
    return(answer)

if __name__=="__main__":
    '''This displays incorrectly in the shell but
    shows fine in the tkinter window.'''
    print(list_books())#Normal case
    print(title_search("The Hobbit"))#Title with 1 author
    print(title_search("1984"))#1 Title with 2 different authors


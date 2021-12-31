import sys 
book_list = []
book_lend= dict()
no = 0 
a = 0
while True:
    class Library :
        def intro(self):
            print("\n\nGood morning, welcome to My Library ")
            print('If you want to access the books available press "1"')
            print('If you want to lend a book press "2"')
            print('If you want to return a book press "3"')
            global a 
            print('if you want to exit press "enter" in all circumstances ')
            a = int(input('please choose one from the above option - '))
        def books_available (self):
            global book_list
            book_list = ["Python","JavaScript","Java","Kotlin","PhP"]
            return ("These are the books that are available -->",book_list)
        def book_lend(self):
            global book_list,book_lend
            print(f'these are the available book *case sensitive -->{book_list}')
            book_name = input('enter which book you want to lend - ')
            lender_name = input('enter you name - ')
            a = {lender_name:book_name}
            if book_name in book_list :
                book_list.remove(book_name)
                print(f'You can take the book in take out section *please maintain the book  {book_name}')
                book_lend.update (a)
            else :
                self.intro()
        def book_return(self):
            global no
            no += 1
            name = input('Please enter you name - ')
            if name in book_lend:
                checknam= input('Please enter you name for verification purpose - ')
                if checknam != name :
                    if no > 3 :
                        print('you have been blocked for not passsing the verification test ')
                        sys.exit()
                    else :
                        self.book_return()
                bkn = input('Enter the book name please - ')
                if  bkn in book_lend.values() :
                    print(f'You have successfully returned the book {bkn} THANK YOU ,Please visit again ')
                else :
                    self.book_return()
            else :
                print('it looks like you have been not registered ')
    l = Library()
    l.intro()
    l.books_available()
    if a == 1:
        print(l.books_available())
    elif a == 2 :
        l.book_lend()
    elif a == 3 :
        l.book_return()
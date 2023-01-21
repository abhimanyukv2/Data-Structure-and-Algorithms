'''Suppose you are on the design team for a new e-book reader. What are the primary classes and methods that the Python software for your reader will need? You should include an inheritance diagram for this code, but you do not need to write any actual code. Your software architecture should at least include ways for customers to buy new books, view their list of purchased books, and read their purchased books.'''

'''
    |-----------------------------------------------------------------------------|
    | Class: Book                                                                 |
    |-----------------------------------------------------------------------------|
    | Method                                                                      |
    | view_eBook()                                                                |
    | view_hardcopy()                                                             |
    | purchase_book()                                                             |
    |-----------------------------------------------------------------------------|
    | Instance Variable                                                           |
    | available_book_list                                                         |
    | purchased_ebook(list)                                                       |
    | purchased_hardcopy(list)                                                    |
    |-----------------------------------------------------------------------------|
    | Class: E-Book(Book)                 | Class: HardCopy(Book)                 |
    |-------------------------------------|---------------------------------------|
    | Method                              | Method                                |
    | view_purchased_ebook()              | View_purchased_hardcopy()             |
    | read_purchased_ebook()              | read_purchased_hardcopy()             |
    |-----------------------------------------------------------------------------|
'''
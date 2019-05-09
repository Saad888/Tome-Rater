"""
TomeRater.py

Summary:
----
This application allows users to read and rate books. 
It was created as part of the Capstone project for Codecademy's  course titled 
"Programming with Python". The core of the program is through TomeRater which 
is used to create a library of Users and Books and contains various methods 
for analysis. Please see the docstring for TomeRater for more details

Classes:
----
User 
Book 
Fiction (child of Book)
NonFiction (child of Book)
TomeRater (analysis class)
"""


def email_format(email):
    """Returns true if email is correct format, false otherwise"""

    if type(email) is str:
        confirm_at = (email.find("@") > -1)
        domain = max(email.find(".com"), 
                     email.find(".edu"), 
                     email.find(".org"))
        confirm_domain = (domain > -1) and (len(email) - domain == 4)
        if confirm_at and confirm_domain:
            return True
    print("Invalid Email Format (must have @ and end in .com, .edu, or .org)")
    return False
        

class User:

    """This class stores informations regarding individual users 

    Attributes:
        name (str): User's name
        email (str): User's email
        books (dict): Dictionary with Books as keywords and rating as values

    Methods:
        get_email(): Returns user's email
        change_email(str): Changes email if str is correct format
        read_book(Book, rating): Adds a book to self.books() dictionary with 
                                 its rating as the value {Book: rating}
        get_average_rating(): Returns average user ratings for books
        help(): Prints docstring for assistance
    """

    def __init__(self, name, email):
        """Confirms email format, sets name and email, initates book dict"""

        # Confirm email is of correct form, otherwise request another email
        while email_format(email) is False:
            print("Please enter correct email: ")
            email = input()

        # Initiates user instance variables
        self.name = str(name)
        self.email = email
        self.books = {}

    def get_email(self):
        """Returns user's email"""
        return self.email

    def change_email(self, address):
        """Changes user's email based on input"""
        if email_format(address):
            prev_email = self.email
            self.email = address
            print("User's email has been changed.\nPrevious Email: {}\n\
                New Email: {}".format(prev_email, self.email))

    def read_book(self, book, rating=None):
        """Adds a book w/ its rating to the books dictionary (default: None)"""

        if isinstance(book, (Book, Fiction, NonFiction)):     
            # Confirms if rating is correct before adding  
            try:
                rating = float(rating)
                if (rating >= 0) and (rating < 5):
                    self.books[book] = rating
                else:
                    raise ValueError
            except (TypeError, ValueError):
                self.books[book] = None
        else:
            print("Incorrect input for Book")

    def get_average_rating(self):
        """Returns average rating, ignored books with no rating"""

        rating_sum = 0
        rating_count = 0
        rating_list = list(self.books.values())

        # Cycles through ratings and returns average
        for rating in list(rating_list):
            if rating is not None:
                rating_sum += rating
                rating_count += 1
        return rating_sum / (max(rating_count, 1))

    def __repr__(self):
        """Prints information about the user (Name, Email, # of books)"""

        return "User: {} | Email: {} | Books Read: {}"\
            .format(self.name, self.email, len(self.books))

    def __eq__(self, other):
        """Returns True is user names and email match"""

        if type(self) == User and type(other) == User:
            return (self.name == other.name) and (self.email == other.email)
        else: 
            return False

    def help(self):
        """Prints docstring in console"""
        print(self.__doc__)


class Book:

    """Stores information regarding a Book
    
    Attributes:
    title (str): Title of the book
    isbn (str): ISBN of the book
    ratings [(int)]: List of user ratings for the book

    Methods:
    get_title(): Returns title
    get_isbn(): Returns ISBN
    set_isbn(isbn): Sets the ISBN of the Book
    add_rating(rating): Adds user rating if it is within 0 and 4, inclusive
    get_average_rating(): Returns average of user ratings
    help(): Returns docstring

    """

    def __init__(self, title, isbn):
        """Sets object title and isbn, creates empty list for user ratings"""
        self.title = str(title)
        self.isbn = str(isbn)
        self.ratings = []

    def get_title(self):
        """Returns title of book"""
        return self.title

    def get_isbn(self):
        """Returns ISBN"""
        return self.isbn

    def set_isbn(self, isbn):
        """"Sets isbn to a new values"""
        old_isbn = self.isbn
        self.isbn = str(isbn)
        print("ISBN changed.\nPrevious ISBN = {}\nNew ISBN = {}".
              format(old_isbn, self.isbn))

    def add_rating(self, rating):
        """Adds user ratings to rating list"""
        try:
            rating = float(rating)
            if (rating >= 0) and (rating <= 4):
                self.ratings += [rating]
                return None
            else:
                print("Invalid Rating")
        except TypeError:
            return None

    def get_average_rating(self):
        """Returns average of all ratings for this book"""

        rating_sum = 0
        for i in self.ratings:
            rating_sum += i
        return rating_sum / max(len(self.ratings), 1)

    def __eq__(self, other):
        """Returns True if title and ISBN are the same"""

        if (type(self) == type(other)):
            return (self.title == other.title) and (self.isbn == other.isbn)
        else: 
            return False

    def __hash__(self):
        """Sets hash so that the class can be used as keys for dictionaries"""
        return hash((self.title, self.isbn))

    def __repr__(self):
        """Returns book title"""
        return self.title

    def help(self):
        """Prints docstring in console"""
        print(self.__doc__)


class Fiction(Book):

    """Stores information regarding a Fiction book (child of Class Book)
    
    Attributes:
    title (str): Title of the book
    isbn (str): ISBN of the book
    ratings [(int)]: List of user ratings for the book
    author (str): Author of book

    Methods:
    get_author(): Returns Author
    get_title(): Returns title
    get_isbn(): Returns ISBN
    set_isbn(isbn): Sets the ISBN of the Book
    add_rating(rating): Adds user rating if it is within 0 and 4, inclusive
    get_average_rating(): Returns average of user ratings
    help(): Returns docstring

    """

    def __init__(self, title, author, isbn):
        """Repeats book initialization and sets child variable author"""
        super().__init__(title, isbn)
        self.author = str(author)

    def get_author(self):
        """Returns author"""
        return self.author

    def __repr__(self):
        """Returns Title, by Author"""
        return "{}, by {}".format(self.title, self.author)

    def help(self):
        """Prints docstring in console"""
        print(self.__doc__)


class NonFiction(Book):

    """Stores information regarding a Non Fiction book (child of Class Book)
    
    Attributes:
    title (str): Title of the book
    isbn (str): ISBN of the book
    ratings [(int)]: List of user ratings for the book
    subject (str): Subject of book
    level (str): Level of book (e.g. Beginner, Advanced, etc.)

    Methods:
    get_title(): Returns title
    get_isbn(): Returns ISBN
    set_isbn(isbn): Sets the ISBN of the Book
    get_subject(): Returns the subject of the book
    get_level(): Returns the level of the book
    add_rating(rating): Adds user rating if it is within 0 and 4, inclusive
    get_average_rating(): Returns average of user ratings
    help(): Returns docstring

    """

    def __init__(self, title, subject, level, isbn):
        """Repeats book initialization and sets child variables subject & title"""
        super().__init__(title, isbn)
        self.subject = str(subject)
        self.level = str(level)

    def get_subject(self):
        """Returns the subject"""
        return self.subject

    def get_level(self):
        """Returns the level"""
        return self.level

    def __repr__(self):
        """Returns the title, level, and subject in string form"""
        return "{title}, {level} manual on {subject}".format(
            title=self.title, level=self.level, 
            subject=self.subject)

    def help(self):
        """Prints docstring in console"""
        print(self.__doc__)


class TomeRater:

    """Main class used to create books/users & manipulate/analyze their data

    Attributes:
    -----------
    users{}: dictionary of {user emails: user objects}
    books{}: dictionary of {books objects: # of users who've read the book}

    Methods:
    --------
    create_book(title, isbn): creates book object from inputs
    create_novel(title, author, isbn): creates fiction book object from inputs
    create_non_fiction(title, subject, level, isbn): creates manual from inputs
    add_book_to_user(book, email, rating): adds a book to user with rating
                                           default rating is None
    add_user(name, email, books): creates user and adds books to user
    print_catalog: prints all books in TomeRater
    print_users: prints all users in TomeRater
    most_read_book(): returns most read book
    get_n_most_read_books(): returns list of n most read books
    highest_rated_book(): returns book with highest average rating
    most_positive_user(): returns user with highest average rating
    get_n_most_prolific_readers(): returns n users with highest book count

    Private Methods:
    ----------------
    _confirm_isbn(): confirms if isbn is duplicate of existing TomeRater book
    _sort_dictionary(dic, n): returns n keys with highest values 

    """

    def __init__(self):
        self.users = {}
        self.books = {}
        print("TomeRater successfully created! Use .help() for assistance.")

    def _confirm_isbn(self, isbn):
        """Confirms if ISBN is a duplicate of ISBN of an existing book"""
        for book in self.books:
            if book.get_isbn() == str(isbn):
                print("ISBN is duplicate of", book)
                print("Book has not been created.")
                return False
        return True

    def create_book(self, title, isbn):
        """Creates and returns a book"""
        if self._confirm_isbn(isbn):
            new_book = Book(title, isbn)
            return new_book

    def create_novel(self, title, author, isbn):
        """Creates and Returns a novel"""
        if self._confirm_isbn:
            new_book = Fiction(title, author, isbn)
            return new_book

    def create_non_fiction(self, title, subject, level, isbn):
        """Creates and Returns a non-fiction book"""
        if self._confirm_isbn:
            new_book = NonFiction(title, subject, level, isbn)
            return new_book

    def add_book_to_user(self, book, email, rating=None):
        """Adds a book to an exiting user in TomeRater by email"""

        # Confirms email format and adds the book to a user
        if isinstance(book, (Book, Fiction, NonFiction)):
            email = str(email)
            if email in self.users:
                this_user = self.users[email]
                this_user.read_book(book, rating)
                book.add_rating(rating)
                if book in self.books:
                    self.books[book] += 1
                else:
                    self.books[book] = 1
            else:
                print("No user with", email)
        else:
            print("Incorrect input for book, no actions taken")

    def add_user(self, name, email, user_books=None):
        """Adds a user, if list of books is given, adds those to the user"""
        
        # Confirms email format and ensure no duplicate emails         
        while (email in self.users) or (email_format(email) is False):
            if email in self.users:
                print("User with this email already exists!")
            print("Please enter a different email: ")
            email = input()

        # Create User
        new_user = User(name, email)

        # Adds user to list
        self.users[email] = new_user

        # Adds books list to user (if provided and valid)
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

        # Returns user for debugging
        return new_user

    def print_catalog(self):
        """Prints all the books in this Tomerater instance"""
        for book in self.books:
            print(book)

    def print_users(self):
        """Prints all users in this TomeRater instance"""
        for user_email in self.users:
            print(self.users[user_email])

    def _sort_dictionary(self, dic, n):

        """Returns a sorted list from dictionary dic with in ASCENDING order

        Parameters:
        -----------
        dic: dictionary to be sorted (must be larger than 0)
        n: number of items to return (greater than 1)

        Returns:
        --------
        list of size n or len(dic) (whichever is smaller)
        """

        # Confirms if inputs were of valid type
        if (type(dic) is not dict) or (type(n) is not int) or (n < 1):
            print("Incorrect arguments were used for the function")
        else:
            # Creates sorted list of dictionary with descending values
            sorted_list = sorted(
                dic.items(), 
                key=lambda i: i[1], 
                reverse=True
            )

            # returns list of keys from 0 to n (highest to lowest value)
            return [sorted_list[i][0] for i in range(min(n, len(dic)))]
            
    def most_read_book(self):
        """Returns the most read book in this TomeRater instance, else None"""
        best_book = self.get_n_most_read_books(1)
        return best_book[0] if best_book is not None else None

    def get_n_most_read_books(self, n):
        """Returns n most read books in descending order"""
        if len(self.books) > 0:
            try:
                sorted_books = self._sort_dictionary(self.books, int(n))
                return sorted_books
            except (TypeError, ValueError):
                print("Incorrect value for n")
        else:
            print("No books in TomeRater")

    def highest_rated_book(self):
        """Returns the highest rated book in this TomeRater instance"""
        if len(self.books) != 0:
            book_rating = {}
            for book in self.books:
                book_rating[book] = book.get_average_rating()
            sorted_rating = self._sort_dictionary(book_rating, 1)
            return sorted_rating[0]
        else:
            print("No books in TomeRater")

    def most_positive_user(self):
        """Returns user with highest rating"""
        if len(self.users) != 0:
            user_ratings = {}
            for email in self.users:
                user_ratings[email] = self.users[email].get_average_rating()
            highest_user_email = self._sort_dictionary(user_ratings, 1)
            return self.users[highest_user_email[0]]
        else:
            print("No users in TomeRater")

    def get_n_most_prolific_readers(self, n):
        """returns n users who've read the most book in descending order"""
        if len(self.users) != 0:
            try:
                user_book_count = {}
                for email in self.users:
                    user_book_count[email] = len(self.users[email].books)
                sorted_user_list = self._sort_dictionary(user_book_count, int(n))
                return sorted_user_list
            except (TypeError, ValueError):
                print("Incorrect value for 'n'")
        else:
            print("No users in TomeRater")

    def help(self):
        """Prints docstring in console"""
        print(self.__doc__)

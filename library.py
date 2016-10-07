import json

from pymongo import MongoClient


class Library:

    # Connecting to mongobd Database.
    client = MongoClient("mongodb://localhost:27017/")
    db = client.library
    coll = db.books

    def convert_to_json(self, string):
        """Converts str to json.

        :param string: str, string
        :return: json format
        """
        return json.loads(string)

    def add_book(self):
        """Add's books with ISBN, namee, category and qty."""
        # Checking for book data
        book_isbn = self.find_book()
        if book_isbn is False:
            book_isbn = raw_input("ISBN :")
            book_name = raw_input("Name :")
            book_category = raw_input("Category :")
            book_qty = raw_input("Qty :")

            book_document = "{\"book_isbn\":\"" + str(book_isbn) + \
                            "\", \"book_name\":\"" + str(book_name) + \
                            "\", \"book_category\":\"" + str(book_category) +\
                            "\", \"book_qty\":\"" + str(book_qty) + "\"} "

            book_document_json = self.convert_to_json(book_document)

            self.coll.insert (book_document_json)
            print "Info : Added Book Record"
        else:
            print "Error : Book already Exists  !"

    def find_book(self):
        """Finds book by ISBN."""

        book_isbn = raw_input("ISBN :")

        book_document = "{\"book_isbn\":\"" + str(book_isbn) + "\"}"
        book_document_json = self.convert_to_json(book_document)
        result = self.coll.find(book_document_json)
        for row in result:
            print "Book Name     :" + str(row.get('book_name'))
            print "Book Category :" + str(row.get('book_category'))
            print "Book Quantity :" + str(row.get('book_qty'))
            return book_isbn

        print "Book Not Found"
        return False

    def update_book_details(self):
        """Finds and Update the book by ISBN."""

        # Checking for book data
        book_isbn = self.find_book()
        if book_isbn is not False:
            book_name = raw_input("Name :")
            book_category = raw_input("Category :")
            book_qty = raw_input("Qty :")

            where_document = "{\"book_isbn\":\"" + str(book_isbn) + "\"} "
            where_document_json = self.convert_to_json(where_document)

            book_document = "{\"book_isbn\":\"" + str(book_isbn) + \
                            "\", \"book_name\":\"" + str(book_name) + \
                            "\", \"book_category\":\"" + str(book_category) +\
                            "\", \"book_qty\":\"" + str(book_qty) + "\"} "
            book_document_json = self.convert_to_json(book_document)

            self.coll.update(where_document_json, book_document_json)
            print "Updated Success....."

    def delete_book(self):
        """Delete a Book by ISBN."""

        book_isbn = raw_input("ISBN :")
        book_document = "{\"book_isbn\":\"" + str(book_isbn) + "\"}"
        book_document_json = json.loads(book_document)

        result = self.coll.find(book_document_json)
        for row in result:
            self.coll.remove(book_document_json)
            print "Deleted Book"
            return

        print "Book Not Found"

    def get_quantity_of_book(self):
        """Get Quantity of a book by its ISBN."""
        book_isbn = raw_input("ISBN :")

        book_document = "{\"book_isbn\":\"" + str(book_isbn) + "\"}"
        book_document_json = json.loads(book_document)
        result = self.coll.find(book_document_json)
        for row in result:
            print "Book Quantity :" + str(row.get('book_qty'))
            return

        print "Book Not Found"

    def get_quantity(self):
        """Get Quantity of all Books."""
        result = self.coll.find()
        print "ISBN\tQTY"
        for row in result:
            print str(row.get('book_isbn')) + "\t" + str(row.get('book_qty'))
# Creating object for library
l = Library()

# Implementing switch case
option = {1: l.add_book,
          2: l.find_book,
          3: l.update_book_details,
          4: l.delete_book,
          5: l.get_quantity_of_book,
          6: l.get_quantity,
          7: False}

print "Welcome to Nineleaps Library"
print "1. Add Books\n2. Find a Book\n3. Update a Book\n4. Delete a Book\n5.Get Quantity of a Book\n6.Get Quantity"
print "--------------------------------------"
selected = option[int(raw_input("Input :"))]
while selected:
    selected()
    print "--------------------------------------"
    selected = option[int(raw_input("Input :"))]
print "Bye....."

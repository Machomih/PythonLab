class LibraryItem:
    def __init__(self, title, item_id, is_checked_out=False):
        self.title = title
        self.item_id = item_id
        self.is_checked_out = is_checked_out

    def display_info(self):
        return f"Title: {self.title}, Item ID: {self.item_id}, Checked Out: {self.is_checked_out}"

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already in the library.")


class Book(LibraryItem):
    def __init__(self, title, item_id, author, is_checked_out=False):
        super().__init__(title, item_id, is_checked_out)
        self.author = author

    def display_info(self):
        return (f"Title: {self.title}, "
                f"Item ID: {self.item_id}, "
                f"Author: {self.author}, "
                f"Checked Out: {self.is_checked_out}")


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, is_checked_out=False):
        super().__init__(title, item_id, is_checked_out)
        self.director = director

    def display_info(self):
        return (f"Title: {self.title}, "
                f"Item ID: {self.item_id}, "
                f"Director: {self.director}, "
                f"Checked Out: {self.is_checked_out}")


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue, is_checked_out=False):
        super().__init__(title, item_id, is_checked_out)
        self.issue = issue

    def display_info(self):
        return f"Title: {self.title}, Item ID: {self.item_id}, Issue: {self.issue}, Checked Out: {self.is_checked_out}"


book = Book("20.000 feet under the Sea", 1001, "Jules Verne")
print(book.display_info())
book.check_out()
book.return_item()
print()

dvd = DVD("The Dark Knight", 2002, "Christopher Nolan")
print(dvd.display_info())
dvd.check_out()
print()

magazine = Magazine("Cars", 3003, "June 2023")
print(magazine.display_info())
magazine.check_out()

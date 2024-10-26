class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []  # Store contracts as a private attribute
        self._books = []      # Store unique books associated with the author

    def add_contract(self, contract):
        self._contracts.append(contract)
        if contract.book not in self._books:  # Avoid duplicates
            self._books.append(contract.book)

    def contracts(self):
        return self._contracts

    def books(self):
        return self._books

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []  # Store contracts as a private attribute
        self._authors = []    # Store unique authors associated with the book

    def add_contract(self, contract):
        self._contracts.append(contract)
        if contract.author not in self._authors:  # Avoid duplicates
            self._authors.append(contract.author)

    def contracts(self):
        return self._contracts

    def authors(self):
        return self._authors


class Contract:
    all = []  # Store all contracts

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        if not isinstance(book, Book):
            raise Exception("Book must be of type Book")
        if not isinstance(date, str):
            raise Exception("Date must be of type str")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be of type int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add the contract to the author's and book's contracts
        author.add_contract(self)
        book.add_contract(self)

        # Add the contract to the global list of contracts
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]


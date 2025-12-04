### Portfolio
I'm curating a portfolio of data science projects I've worked on or am currently working on. Some are for fun and curiosity; others came from a data science bootcamp.

# SQL
Before my bootcamp, SQL was on my radar as important for databases and as a coding skill. What I didn't expect was its elegance, which really appealed to my mathematical sensibilities over 20 years after graduation... I really enjoyed the logic, designing database structures, and putting together the puzzle of an efficient query.

![Ornate, multi-level bookstore with carved wooden railings, tall bookshelves filled with books, warm lighting from hanging lanterns, and a grand central staircase leading between floors. The tonal palette is warm and autumnal.](https://github.com/SarennahL-C/pf-ebookstore/blob/a24197d74648de19b3aa32d273e0fa84aad1bd6e/bookstore.jpg?raw=true)

# ebookstore
This SQLite project was a bootcamp task to:

> ... create a program for a bookstore. The program should allow the clerk to enter data about new books into the database, update book information, delete books from the database, and search to check the availability of books.

In my solution, I've extended the brief to allow for authors writing multiple books and to save the inventory for a permanent record. I've also allowed the user to load sample data or data from a correctly formatted text file.

If the clerk enters a book by an author already in the system, this is recognised, and the steps to enter author information are skipped. If the clerk amends the details of an author, the changes propagate to all the relevant records. While there is defensive coding elsewhere to ensure proper inputs, there isn't an enforced structure for author names, meaning that Iain Banks and Iain M. Banks are both possible and are treated as separate authors. This is intentional to allow for author choices such as Iain (M.) Banks using the M. to signify his science fiction work, distinct from his literary fiction.

This project showcases SQL coding using SQLite within Python. At this point, it was the most complex piece of Python I'd written, and it remains my longest .py file. The program runs directly from the terminal from a menu:

![Screenshot of a text menu presented in white console font on black background. The user is expected to select from the menu by keying in a single digit and pressing enter.](https://github.com/SarennahL-C/pf-ebookstore/blob/cde3e2ad9f8244c37d1491918b38edbfbd31164f/book%20shelf%20menu.jpg?raw=true). 

View a sample of the book records [here](https://github.com/SarennahL-C/pf-ebookstore/blob/72d19e3e7f21e920b61fc10d91854ec76de7e578/book%20shelf%20option%205%20book%20details.jpg).

The reviewer's feedback on my project noted that my solution is an extensive and seamless interpretation of the brief. I also had a gentle nudge to up my PEP8 game, which I took to heart and now follow closely. View a screenshot of the feedback [here](https://github.com/SarennahL-C/pf-ebookstore/blob/ba994ab4e9e3d4d90c4cce62441b1a3f137782af/SQL%20feedback.jpg).

#### Requirements
Install the requirements for Python 3 using `pip install -r requirements.txt`.

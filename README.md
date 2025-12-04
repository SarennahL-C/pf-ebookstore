### Portfolio
I'm curating a portfolio of data science projects I've worked on or am currently working on. Some are for fun and curiosity; others came from a data science bootcamp.

# SQL
Before my bootcamp, SQL was on my radar as important for databases and as a coding skill. What I didn't expect was its elegance, which really appealed to my mathematical sensibilities over 20 years after graduation... I really enjoyed the logic, designing database structures, and putting together the puzzle of an efficient query.

![Ornate, multi-level bookstore with carved wooden railings, tall bookshelves filled with books, warm lighting from hanging lanterns, and a grand central staircase leading between floors. The tonal palette is warm and autumnal.]

# ebookstore
This SQLite project was a bootcamp task to:

> ... create a program for a bookstore. The program should allow the clerk to enter data about new books into the database, update book information, delete books from the database, and search to check the availability of books.

In my solution, I've extended the brief to allow for authors writing multiple books and to save the inventory for a permanent record. 

If the clerk enters a book by an author already in the system, this is recognised, and the steps to enter author information are skipped. If the clerk amends the details of an author, the changes propagate to all the relevant records. While there is defensive coding elsewhere to ensure proper inputs, there isn't an enforced structure for author names, meaning that Iain Banks and Iain M. Banks are both possible and are treated as separate authors. This is intentional to allow for author choices such as Iain (M.) Banks using the M. to signify his science fiction work, distinct from his literary fiction.

This project showcases SQL coding using SQLite within Python. At this point, it was the most complex piece of Python I'd written, and it remains my longest .py file.

The reviewer's feedback on my project noted that my solution is an extensive and seamless interpretation of the brief. I also had a gentle nudge to up my PEP8 game, which I took to heart and now follow closely. View a screenshot of the feedback [here](https://github.com/SarennahL-C/pf-ebookstore/blob/ba994ab4e9e3d4d90c4cce62441b1a3f137782af/SQL%20feedback.jpg).

#### Requirements
Install the requirements for Python 3 using `pip install -r requirements.txt`.

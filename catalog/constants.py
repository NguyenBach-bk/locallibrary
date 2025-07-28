# locallibrary/catalog/constants.py
import datetime

MAX_LENGTH_GENRE_NAME = 200
MAX_LENGTH_AUTHOR_NAME = 100
MAX_LENGTH_BOOK_TITLE = 200
MAX_LENGTH_BOOK_SUMMARY = 1000
MAX_LENGTH_BOOK_ISBN = 13
MAX_LENGTH_BOOK_IMPRINT = 200
MAX_GENRES_DISPLAY = 3

LOAN_STATUS = (
    ('m', 'Maintenance'),
    ('o', 'On loan'),
    ('a', 'Available'),
    ('r', 'Reserved'),
)

LOAN_STATUS_LOOKUP = { label.lower().replace(' ', '_'): code for code, label in LOAN_STATUS }

STATUS_MAINTENANCE = LOAN_STATUS_LOOKUP['maintenance']
STATUS_ON_LOAN     = LOAN_STATUS_LOOKUP['on_loan']
STATUS_AVAILABLE   = LOAN_STATUS_LOOKUP['available']
STATUS_RESERVED    = LOAN_STATUS_LOOKUP['reserved']

# Số mục mỗi trang cho BookListView.paginate_by
BOOK_LIST_VIEW_PAGINATE = 10
AUTHOR_LIST_VIEW_PAGINATE = 10
# Số mục mỗi trang cho LoanedBooksByUserListView
MY_BORROWED_PAGINATE_BY = 10
DEFAULT_DATE_OF_DEATH = datetime.date(2000, 1, 1)

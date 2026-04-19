from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS


class BookRequest(BaseModel):
    title: str
    author: str
    category: str

@app.post("/books")
async def create_book(book_request: BookRequest):
    BOOKS.append(book_request.model_dump())
    return book_request

@app.put("/books/update_book")
async def update_book(update_book: BookRequest):
    for x in range (len(BOOKS)):
        if BOOKS[x]['title'] == update_book.title:
            BOOKS[x] = update_book
            return BOOKS[x]
    return {'error': 'Title not found'}


@app.delete("/books/{delete_title}")
async def delete_book(delete_title: str):
    for x in range (len(BOOKS)):
        if BOOKS[x].get('title') == delete_title:
            BOOKS.pop(x)
            return {'message': f"Book {delete_title} deleted"}
    return {'error': 'Title not found'}


@app.get("/books/{book_author}/")
async def read_author_category(book_author:str, category:str):
    books_auth = []
    for x in range (len(BOOKS)):
        if BOOKS[x]['author'] == book_author and BOOKS[x]['category'] == category:
            books_auth.append(BOOKS[x])
            return books_auth
    return {'error': 'Author or category not found'}

@app.get("/books/")
async def read_category_by_query(category:str):
    books_root= []
    for x in range (len(BOOKS)):
        if BOOKS[x]['category'] == category:
            books_root.append(BOOKS[x])
            return books_root
    return {'error': 'Category not found'}



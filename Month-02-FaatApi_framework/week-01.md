# 📚 FastAPI Books CRUD API

## 🚀 Overview

This project is a simple **REST API** built using FastAPI.  
It demonstrates **CRUD operations (Create, Read, Update, Delete)** on a collection of books.

This project focuses on **backend fundamentals**, including request handling, routing, and API design.

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn

---

## 📌 Features

### 🔍 Read Operations (GET)

- Get all books  
- Get a book by title (path parameter)  
- Filter books by category (query parameter)  

### ➕ Create Operation (POST)

- Add a new book using request body  

### 🔄 Update Operation (PUT)

- Update existing book details  

### ❌ Delete Operation (DELETE)

- Delete a book by title  

---

## 📂 API Endpoints

| Method | Endpoint                     | Description              |
|--------|------------------------------|--------------------------|
| GET    | `/books`                     | Get all books            |
| GET    | `/books/{title}`             | Get book by title        |
| GET    | `/books?category=`           | Filter books by category |
| POST   | `/books/create-book`         | Create a new book        |
| PUT    | `/books/update-book`         | Update book details      |
| DELETE | `/books/delete-book/{title}` | Delete book by title     |

---

## ▶️ Run the Project

```bash
uvicorn main:app --reload
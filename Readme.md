# Library Management System

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installations](#installations)
- [Usage](#usage)

## Introduction

Libraries play a crucial role in organizing and providing access to an extensive collection of books, journals, and other resources. Effective management of library operations, including cataloging, circulation, and patron management, is vital to ensure a smooth and organized experience for library users. The Library Management System project was created to address these challenges and gain insights into the following key areas:

- **Object-Oriented Programming (OOP) Concepts:** The project implements OOP principles such as encapsulation, inheritance, and polymorphism to model real-world library entities, making the code modular, maintainable, and extensible.

  [Learn more about OOPS](https://www.notion.so/Object-Oriented-Programming-3ef6aeb57267466d83d5a4f6f5b07432?pvs=21)

- **Python Programming:** This project offers hands-on experience in Python, one of the most popular programming languages. It demonstrates how Python's readability and versatility make it an excellent choice for software development.

- **MySQL Database:** The use of a MySQL database allows the system to store and manage vast amounts of library-related data efficiently. It explores concepts like database design, querying, and data manipulation.

  [Learn more about MySQL](https://www.notion.so/MySQL-ac550b91409944729a43faa7bfbd5a00?pvs=21)

- **Learning by Doing:** By working on this project, you can deepen your understanding of minor yet essential concepts in OOP, Python programming, and database management. It provides an opportunity to apply these concepts to a real-world scenario.

The Library Management System project is an excellent learning tool for both beginners looking to grasp OOP and Python fundamentals and more experienced developers seeking to reinforce their knowledge. Whether you are a student, educator, or library enthusiast, this project can be a valuable asset in your journey toward mastering programming and database management.

## Features

1. **Custom Exceptions:**
   - Custom exceptions are a crucial part of robust error handling in any project. They allow you to define and raise specific exceptions when certain conditions or errors occur.
   - Custom exceptions can provide clear and meaningful error messages to users or developers, making it easier to diagnose and address issues.

2. **Library Module:**
   - The library module appears to be the core of your project, responsible for displaying detailed information about various aspects of the library.
   - It likely includes functions or classes to fetch and present data from tables such as books, patrons, authors, and book genres.
   - This module enhances the user experience by providing access to valuable library-related information.

3. **Library Management Module:**
   - The library management module is a critical component for library administrators or staff members.
   - It enables the insertion, updating, and deletion of records in tables like books, patrons, authors, and genres.
   - This functionality ensures that the library's database remains up-to-date and organized.

4. **Transaction Management Module:**
   - Transaction management is a vital aspect of library operations, especially for tracking book checkouts and returns.
   - The use of ACID transactions enhances the reliability and consistency of these operations.
   - ACID transactions guarantee that library patrons can smoothly check out and return books, even in the presence of failures or errors.

In summary, your Library Management System project combines essential features such as custom exceptions, data presentation, database management, and ACID transaction handling. These features collectively contribute to the efficiency and reliability of library operations.

## Getting Started

### Prerequisites & Installations

Before you begin working with the Library Management System project, ensure that you have the following prerequisites set up:

1. **Python Environment:**
   - Create a virtual environment to isolate project dependencies and ensure compatibility.
   
     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```

     - On macOS and Linux:
       ```bash
       source venv/bin/activate
       ```

2. **Dependencies Installation:**
   - Install the required libraries and dependencies from the **`requirements.txt`** file using pip:

     ```bash
     pip install -r requirements.txt
     ```

3. **MySQL Database:**
   - Set up a MySQL database server. You can install MySQL Server locally or use a remote MySQL server depending on your project's requirements.

4. **Database Configuration:**
   - In the **`database.py`** module, provide the necessary database connection details:
     - Database host (e.g., localhost or remote host)
     - Database username and password
     - Database name

   - Example **`database.py`** content:

     ```python
     DATABASE_CONFIG = {
         'host': 'localhost',
         'user': 'your_username',
         'password': 'your_password',
         'database': 'your_database_name'
     }
     ```

Once you have these prerequisites in place, you can proceed with running and developing your Library Management System project.

[Database Schema](https://www.notion.so/Relational-Model-Description-for-Library-management-system-7d42ad23760d4e358b820b7cb01541d1?pvs=21)

## Usage

### 1. Starting the Application

- Ensure that you have completed the prerequisites outlined in the [Prerequisites](#prerequisites) section of this documentation.
- Activate the virtual environment if you haven't already:
  - On Windows:
    ```bash
    venv\Scripts\activate
    ```
  - On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```

### 2. Running the Application

- To start the Library Management System, run the main application file:
  ```bash
  python main.py

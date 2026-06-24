# python-cf9

A collection of educational Python exercises and examples developed while learning core programming concepts and Python fundamentals.

This repository is organized into chapter-based modules and includes independent examples covering topics from basic syntax to functional programming and object-oriented programming.

The material follows a progressive learning approach, where each chapter introduces new concepts through small standalone scripts and exercises.

---

## Tech Stack

* Python 3.14.5
* NumPy
* pandas

---

## Repository Organization

The repository is structured as educational material.

Each `chapterXX` folder contains independent Python modules focused on a specific topic.

Additional standalone scripts located in the project root are used for demonstrations and experimentation outside the chapter structure.

---

## Topics Covered

### Chapter 01 — Python Fundamentals

* Variables and literals
* Input and output
* Numeric operations
* Booleans and logic
* String manipulation
* Indexing and slicing
* Basic programming exercises

### Chapter 02 — Data Structures & OOP

* Lists and nested lists
* Tuples
* Sets
* Dictionaries
* Functions
* Variable arguments
* Classes and inheritance
* Small application examples

### Chapter 03 — Intermediate Python Concepts

* Mutability and immutability
* Object behavior
* Comparisons
* Ternary expressions
* Fibonacci algorithms
* Password generation
* HTTP error demonstrations

### Chapter 04 — Functions & Advanced Syntax

* Type annotations
* Generics
* Scope
* Recursion
* Lambda expressions
* map / filter / reduce
* Copying and unpacking

### Chapter 05 — Functional Programming Concepts

* List comprehensions
* Closures
* Inner functions
* Function arguments
* Event logging
* Calculator examples
* Functional programming patterns

---

## Repository Structure

```text
python-cf9
│
├── chapter01/
├── chapter02/
├── chapter03/
├── chapter04/
├── chapter05/
│
├── extra_demo.py
├── hello.py
├── out_of_box_01.py
├── pandas-demo.py
├── tuple_demo.py
│
└── requirements.txt
```

Folder responsibilities:

* **chapter01–chapter05/** → Educational modules organized by topic
* **extra_demo.py** → Additional Python demonstrations
* **pandas-demo.py** → Data analysis examples using pandas
* **tuple_demo.py** → Tuple examples and experiments
* **requirements.txt** → Repository dependencies

---

## Features

* Independent educational Python examples
* Progressive chapter-based learning
* Practical programming exercises
* Object-oriented programming examples
* Functional programming concepts
* Interactive input and output examples
* NumPy and pandas demonstrations

---

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Examples

Run individual modules directly:

```bash
python chapter01/01_primitives.py
```

Examples:

```bash
python hello.py
python pandas-demo.py
python tuple_demo.py
```

---

## Dependencies

Main dependencies:

```text
numpy
pandas
```

Install all project dependencies using:

```bash
pip install -r requirements.txt
```

---

## Educational Purpose

This repository was created for practice and learning in:

* Python fundamentals
* Data structures
* Object-oriented programming
* Functional programming
* Recursion and algorithms
* Type annotations
* NumPy
* pandas

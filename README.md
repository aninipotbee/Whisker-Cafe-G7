# 🐱 Whisker Café
### Cat Café Reservation and Visitor Management System

Whisker Café is a web-based management system designed for a cat café business. It helps café owners and staff manage customer reservations, organize visitors waiting for their sessions, and monitor the different stages of a customer's visit.

The system combines a cat café-inspired interface with Python and Django functionality, incorporating two fundamental data structures: **First In, First Out (FIFO) Queue** and **Singly Linked List**.

---

## 📌 Project Overview

Managing reservations and customer visits manually can become confusing, especially when several customers arrive and require assistance.

Whisker Café provides a centralized platform where café staff can organize reservations, manage visitor queues, view resident cats, and track customer visit workflows.

### 🎯 Target Users

- **Café Owners** – Manage café operations and monitor reservations.
- **Managers** – Organize staff assignments and oversee customer activities.
- **Café Staff** – Handle reservations, assist visitors, and manage waiting queues.

---

## ✨ Features

### 1. Reservation Management
- Record customer information.
- Manage guest counts and session schedules.
- Select preferred resident cats.
- Assign staff hosts to reservations.

### 2. Resident Cat Directory
- Display the café's resident cats.
- Show cat information and personalities.
- Provide customers with an overview of the available cats.

### 3. Visitor Queue Management
- Organize visitors according to their arrival order.
- Display the next visitor to be served.
- Add and remove visitors from the waiting line.
- Follow the First In, First Out (FIFO) principle.

### 4. Visit Workflow Management
- Organize the different stages of a customer's café visit.
- Add, insert, and remove workflow steps.
- Track the order of the process using a Singly Linked List.
- Inspect the actual nodes, including head, tail, and next references.

### 5. Additional Management Features
- Staff host assignments.
- Reservation reports.
- CSV export.
- Team accounts and role-based permissions.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Web framework and backend |
| SQLite | Database management |
| HTML | Website structure |
| CSS | Website styling and layout |
| JavaScript | Interactive website elements |

---

## 🧠 Data Structures Implemented

### Part A: FIFO Queue

The application uses a First In, First Out (FIFO) Queue to manage visitors waiting for their café sessions.

The first visitor who enters the queue will be the first one served.

**Implementation:** `backend/dsa/queue.py`

| Method | Description | Complexity |
|---|---|---|
| enqueue() | Adds a visitor to the rear | O(1) |
| dequeue() | Removes the first visitor | O(1) |
| peek() | Views the next visitor | O(1) |
| is_empty() | Checks if the queue is empty | O(1) |
| size() | Returns the number of visitors | O(1) |

The implementation uses Python's `collections.deque` to support efficient queue operations.

### Part B: Singly Linked List

The application uses a Singly Linked List to represent and organize the ordered stages of a café visit.

Each node contains data and a reference to the next node.

**Implementation:** `backend/dsa/singly_linked_list.py`

The linked list maintains:
- **Head** – Points to the first node.
- **Tail** – Points to the last node.
- **Next** – Connects a node to the following node.
- **Size** – Tracks the total number of nodes.

| Method | Description | Complexity |
|---|---|---|
| prepend() | Adds a node at the beginning | O(1) |
| append() | Adds a node at the end | O(1) |
| insert_at() | Inserts a node at a given index | O(n) |
| remove_at() | Removes a node at a given index | O(n) |
| remove() | Removes the first matching value | O(n) |
| get() | Retrieves a value by index | O(n) |
| index_of() | Finds the first matching value | O(n) |
| size() | Returns the number of nodes | O(1) |

Appending takes O(1) because the list maintains a tail reference. Retrieving a value takes O(n) because the nodes must be traversed starting from the head.

---

## 💻 Installation and Setup

### Requirements

- Python 3.12 or 3.13
- Windows operating system
- Internet connection for the initial setup
- A web browser

### Step 1: Download the Repository

1. Open the project repository on GitHub.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the downloaded ZIP file.
5. Open the extracted project folder.

Make sure you are inside the folder containing:
- `SETUP.bat`
- `START.bat`
- `manage.py`

### Step 2: Open PowerShell

1. Open the extracted project folder.
2. Click the File Explorer address bar.
3. Type `powershell`.
4. Press Enter.

### Step 3: Install Dependencies

Run the following command:

```powershell
.\SETUP.bat
```

Wait until the setup process finishes.

This will create the virtual environment, install the required dependencies, and prepare the database.

### Step 4: Start the Application

After setup is complete, run:

```powershell
.\START.bat --port 8001
```

### Step 5: Open the Website

Open your browser and visit:

```text
http://127.0.0.1:8001/
```

Create your own account and team name when accessing the application for the first time.

**Note:** Keep the PowerShell window open while using the website. To stop the server, press `Ctrl + C`.

---

## 🧪 Testing and Verification

The project includes test scripts for verifying the application and the implemented data structures.

Run the following commands in PowerShell:

| Command | Purpose |
|---|---|
| `.\RUN_TESTS.bat` | Runs the application tests |
| `.\CHECK_QUEUE.bat` | Checks the FIFO Queue implementation |
| `.\CHECK_LINKED_LIST.bat` | Checks the Singly Linked List implementation |
| `.\CHECK_ACTIVITY.bat` | Checks the application activity requirements |
| `.\RUN_ALL_CHECKS.bat` | Runs the combined goal checks |

The expected results are:

- 57 application tests passing.
- FIFO Queue goal checks passing.
- Singly Linked List goal checks passing.
- Combined checks reporting success.

---

## 📂 Project Structure

```text
Whisker-Cafe/
│
├── backend/
│   └── dsa/
│       ├── queue.py
│       └── singly_linked_list.py
│
├── challenge/
├── tests/
├── frontend/
│   ├── templates/
│   └── static/
│
├── database/
├── docs/
│
├── SETUP.bat
├── START.bat
├── RUN_TESTS.bat
├── CHECK_QUEUE.bat
├── CHECK_LINKED_LIST.bat
├── CHECK_ACTIVITY.bat
├── RUN_ALL_CHECKS.bat
│
├── manage.py
└── README.md
```

---

## 🎓 Project Purpose

Whisker Café demonstrates the practical application of data structures in a web-based business management system.

Through the integration of a FIFO Queue and a Singly Linked List, the project shows how programming concepts can help organize customer waiting lines and manage ordered processes.

The project also demonstrates the use of Python, Django, database management, and frontend development in building a functional web application.

---

**Developed as a Programming Implementation Task (PIT)**

**Course:** Python and Django / Data Structures and Algorithms  
**Section:** CS2C  
**Project:** Whisker Café

*Thank you for visiting Whisker Café! 🐾*

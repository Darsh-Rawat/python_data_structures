# 🧠 DSA Package — Learn Data Structures the Pythonic Way

A modular, beginner-friendly **Data Structures & Algorithms (DSA)** package built in **Python**, designed for both **learning** and **experimentation**.

This package provides clean, well-documented implementations of core data structures such as **Linked List**, **Stack**, and **Queue**, with plans to extend toward **Trees**, **Graphs**, and **Sorting/Searching algorithms** — all written from scratch, focusing on **clarity and understanding over abstraction**.

---

## 🚀 Features

✅ **Beginner-friendly design** — simple, readable Python code with clear docstrings
✅ **Dynamic structure support** — linked and dynamic versions for hands-on understanding
✅ **Object-oriented approach** — every data structure built using classes and nodes
✅ **Interactive learning focus** — easy to integrate with real-time “Code + Chat” app
✅ **Extensible** — ready to expand with more DSA modules

---

## 📦 Current Data Structures

| Data Structure     | Description                                                                                                | Status         |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | -------------- |
| **Linked List**    | Implementation of singly linked list with operations like `insert`, `delete`, `reverse`, `find`, `display` | ✅ Completed    |
| **Stack**          | Stack using both Python list and Linked List implementation                                                | ✅ Completed    |
| **Queue**          | Dynamic queue implementation built on top of Linked List                                                   | ⚙️ In progress |
| **Trees & Graphs** | Coming soon                                                                                                | ⏳ Planned      |

---

## 🧩 Example Usage

Here’s a quick peek into how you can use the package:

```python
from dsa.linked_list import LinkedList
from dsa.stack import Stack
from dsa.queue import Queue

# Linked List
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()
ll.reverse()

# Stack
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20

# Queue
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.dequeue()
```

---

## 🧠 Project Structure

```
dsa-package/
│
├── core/
│   └── node.py             # Node class used across multiple structures
│
├── data_structures/
│   ├── linked_list.py      # LinkedList implementation
│   ├── stack.py            # Stack implementation
│   └── queue.py            # Queue implementation (dynamic)
│
├── tests/
│   ├── test_linked_list.py
│   ├── test_stack.py
│   └── test_queue.py
│
├── __init__.py
├── setup.py
├── README.md
└── .gitignore
```

---

## 🧩 Core Concepts Covered

* **Pointers & Nodes**
* **Time and Space Complexity Analysis**
* **Dynamic Memory Representation**
* **OOP in DSA Implementation**
* **Algorithm Design Thinking**

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/dsa-package.git
cd dsa-package
pip install -e .
```

---

## 🧭 Roadmap

* [x] Linked List (Insertion, Deletion, Reverse)
* [x] Stack (List + LinkedList-based)
* [ ] Queue (Dynamic Implementation)
* [ ] Tree Structures (BST, AVL)
* [ ] Graphs (Adjacency List, BFS, DFS)
* [ ] Sorting Algorithms
* [ ] Integration with Real-time **Code + Chat** app (FastAPI + Next.js)

---


## 🤝 Contributing

Contributions are welcome!
Feel free to fork, improve, and submit PRs. You can also open issues for any bugs or feature requests.

---

Would you like me to **add badges** (like Python version, License, PRs welcome, etc.) and a **project banner** section at the top (for GitHub aesthetics)?
That would make your README look even more professional.

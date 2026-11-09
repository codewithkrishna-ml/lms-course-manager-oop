# Online Course & LMS Manager System 🎓💻

A comprehensive, object-oriented Learning Management System (LMS) console simulator built entirely in Python. This backend engine manages academic course creation tracks, enforces data integrity metrics for student enrollments, maps class schedules, and provides native CSV logging handlers for system administrators.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML) -> **Aspiring ML Engineer at Google / Microsoft** 🤖⚡
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Refining problem-solving workflows via Data Structures & Algorithms (DSA) and data manipulation frameworks like **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Dynamic Course Provisions:** Easily launch new educational curriculums mapped to custom auto-incrementing serial IDs starting from a structural index (`ID: 101`).
*   **Data Integrity Checkpoints:** Implements strict validation layers that block blank strings and automatically flag duplicate user entries to prevent a student from double-enrolling in the same track.
*   **Live Class Roster Viewports:** Instantly look up course nodes to see active registration queues, showing exact student arrays side by side.
*   **Scratch-Built Data Serialization:** Writes operational database snapshots directly into structured sheets (`lms_course_ledger.csv`) manually using pure string operations without external bulk extensions.

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This enterprise learning system emphasizes strong isolation boundaries, clean component relationships, and defensive input guards:
*   **Classes & System Modularity:** Structured modularly around independent logical objects: `CourseDetails` (individual module data model) and `LMSManager` (the tracking engine and system repository controller).
*   **Composition / Aggregation Design:** The main manager system coordinates operational lookups by aggregates—storing dynamic collections of `CourseDetails` objects inside dictionary trees mapped smoothly at runtime.
*   **Robust Terminal Safeguards:** Uses defensive parsing parameters (`try-except ValueError`) that intercept type errors during numeric conversions to keep execution scopes stable.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd lms-course-manager-oop
    ```
3.  **Run the interactive framework menu loop:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   **Python 3.x** installed on your machine.
*   Runs entirely on pure Python architecture without needing external third-party library installations.

# College Enterprise Resource Planner

A comprehensive web-based management system for colleges, developed using Python and the Django framework. This project streamlines administrative, academic, and communication processes for students, staff, and administrators.

## 🚀 Deployed At

[https://syncx.pythonanywhere.com](https://syncx.pythonanywhere.com) &nbsp; **v1.1.0**

---

## 🧑‍💻 Demo Student Login

- **E-Mail:** guna@gmail.com  
- **Password:** gunasekaran

---

## ✨ Features

### A. Admin Users Can
1. See overall summary charts of student and staff performance, courses, subjects, leave, etc.
2. Manage staff (add, update, delete)
3. Manage students (add, update, delete)
4. Manage courses (add, update, delete)
5. Manage subjects (add, update, delete)
6. Manage sessions (add, update, delete)
7. View student attendance
8. Review and reply to student/staff feedback
9. Review (approve/reject) student/staff leave

### B. Staff/Teachers Can
1. See summary charts related to their students, subjects, and leave status
2. Take/update student attendance
3. Add/update results
4. Apply for leave
5. Send feedback to HOD

### C. Students Can
1. See summary charts related to their attendance, subjects, and leave status
2. View attendance
3. View results
4. Apply for leave
5. Send feedback to HOD

---

## 💡 Support the Developer

1. Add a Star 🌟 to this repository
2. Follow on [GitHub](https://github.com/Ansarimajid) & [LinkedIn](https://www.linkedin.com/)

---

## 🛠️ How to Install and Run This Project

### Pre-Requisites

1. **Install Git Version Control**  
   [https://git-scm.com/](https://git-scm.com/)

2. **Install Python (Recommended: Python 3.11 or higher)**  
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

3. **Install Pip (Package Manager)**  
   [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/)

   *Alternative to Pip is Homebrew (for Mac/Linux users)*

---

### Installation Steps

**1. Create a folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment:
```
pip install virtualenv
```

Create Virtual Environment:

- **For Windows**
    ```
    python -m venv venv
    ```
- **For Mac**
    ```
    python3 -m venv venv
    ```
- **For Linux**
    ```
    virtualenv .
    ```

Activate Virtual Environment:

- **For Windows**
    ```
    .\venv\Scripts\activate
    ```
- **For Mac**
    ```
    source venv/bin/activate
    ```
- **For Linux**
    ```
    source bin/activate
    ```

**3. Clone this project**
```
git clone https://github.com/Ansarimajid/College-ERP.git
```

Enter the project directory:
```
cd College-ERP
```

**4. Install requirements from `requirements.txt`**
```
pip install -r requirements.txt
```

**5. Configure Allowed Hosts**

- Open `settings.py`
- Set `ALLOWED_HOSTS` to your host(s), e.g.:
    ```python
    ALLOWED_HOSTS = []
    ```
  *Do not use the default allowed settings in this repo. It has security risks!*

**6. Run the Server**

- **For Windows**
    ```
    python manage.py runserver
    ```
- **For Mac/Linux**
    ```
    python3 manage.py runserver
    ```

**7. Create Superuser (HOD)**
```
python manage.py createsuperuser
```
or
```
python3 manage.py createsuperuser
```

---

## 📸 Project's Journey

| Admin/Staff/Student Login |
|--------------------------|
|<img width="455" alt="1" src="https://github.com/user-attachments/assets/273c843e-cda2-4ab1-8e66-6b588858efad" />
<img width="456" alt="2" src="https://github.com/user-attachments/assets/e7135035-4567-4bf9-9e58-88f26e9eca68" />
<img width="460" alt="3" src="https://github.com/user-attachments/assets/611c7e56-3122-4558-a8d7-1aac8727f11a" />
<img width="290" alt="4" src="https://github.com/user-attachments/assets/413cc5a1-8a08-4f05-a874-380028fa8efd" />
---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Questions?

For any questions or issues, please open an [issue](https://github.com/Ansarimajid/College-ERP/issues) or start a discussion.

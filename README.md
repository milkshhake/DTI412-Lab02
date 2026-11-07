# DTI412-Lab02: IT Department CoursePortal (Lab Assignment 2)

A modular, robust Django web application implementing the **Model-View-Template (MVT)** architectural design pattern, dynamic URL routing, template inheritance with Bootstrap 5, server-side form validation, and CSRF protection.

---

## Tech Stack
- **Python:** 3.12+
- **Django:** 5.2.x (`>=5.0, <6.0`)
- **Frontend:** Bootstrap 5.3.2 via CDN
- **Version Control:** Git

---

## Directory Architecture
```text
courseportal/
├── .gitignore
├── manage.py
├── courseportal/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── catalog/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── catalog/
            ├── base.html
            ├── home.html
            ├── course_list.html
            ├── course_detail.html
            └── inquiry.html
```

---

## Implemented Features & Endpoints

| Route | View Function | Description |
|---|---|---|
| `/` | `catalog:home` | Homepage rendering course statistics & featured course card |
| `/courses/` | `catalog:course_list` | Dynamic listing of all offered IT courses |
| `/courses/?q=<query>` | `catalog:course_list` | **Extension Challenge:** Case-insensitive search filtering by course code or title |
| `/courses/<course_id>/` | `catalog:course_detail` | Detailed syllabus page for specific course ID (e.g. `101`) |
| `/courses/999/` | `catalog:course_detail` | Dynamic HTTP 404 error page for non-existent courses |
| `/inquiry/` | `catalog:inquiry` | Interactive student inquiry form with CSRF token and server-side validation |

---

## How to Run

1. **Activate Virtual Environment:**
   - On Windows (PowerShell):
     ```powershell
     ..\venv\Scripts\Activate.ps1
     ```
   - On Windows (CMD):
     ```cmd
     ..\venv\Scripts\activate.bat
     ```

2. **Run Migrations (Optional):**
   ```bash
   python manage.py migrate
   ```

3. **Run Automated Test Suite:**
   ```bash
   python manage.py test
   ```

4. **Start Development Server:**
   ```bash
   python manage.py runserver
   ```
   Open your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Git Workflow & Submission

The repository is organized following feature branching guidelines:
- `main`: Clean initial project scaffolding.
- `feature/django-mvt-lab`: Complete MVT application code and test suite.

To push to your remote GitHub repository:
```bash
git remote add origin https://github.com/milkshhake/DTI412-Lab02.git
git push -u origin main
git push -u origin feature/django-mvt-lab
```
Then open a Pull Request on GitHub from `feature/django-mvt-lab` targeting `main`.

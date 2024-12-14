
# Title -  Django Quiz Application

This is a Django application that allows users to participate in quiz. The application features multiple-choice questions, scoring, and session management. Below is an overview of how to set up, use, and contribute to the project.


## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [API Endpoints](#api-endpoints)


## Features
- **Start a Quiz**: Initiates a new quiz session with randomly selected questions.
- **Submit Answers**: Users can submit their answers, and the application will grade them.
- **View Results**: After completing the quiz, users can view their score and detailed results.
- **Add Questions** (Optional): Admin can add new questions to the quiz via a web interface.

## Installation

1.Prerequisites :

```bash
  - Python 3.7+
  - pip (Python package installer)
  - SQLite (or another database you prefer, though the app is configured for SQLite by default)
```

2.Clone the repository :

   ```bash
   git clone https://github.com/vinodkumarkuruva/Quiz.git
   cd Quiz
   ```

3.Steps to Set Up :

```bash
      Create a virtual environment          :    python3 -m venv < name of virtual Environment > 
       	
      To activate the virtual Environment   :    < name of virtual Environment >/Scripts/activate 
       
      Install dependencies                  :    pip install django
       
      Set up the database                   :    python manage.py makemigrations
                                                 Python manage.py migrate
       
      Run the server                        :    Python manage.py runserver 
       
      * The application will start and be accessible at http://127.0.0.1:5000

   ```

4.API Endpoints

```bash
- /start-quiz/: Initiates a new quiz session and provides randomly selected questions.
- /submit-answer/: Accepts user answers and calculates the score.
- /results/: Displays the results of the quiz session.
```

** (Admin only) Adds a new question to the quiz.


5.Documentation

[Python_Documentation](https://docs.python.org/3/)

[Django_Documentation](https://docs.djangoproject.com/en/5.1/)

[SQLite_Documentation](https://www.sqlite.org/docs.html)




# Phoenix


## Managing.Build Better

### About

A minimal website for posting opportunities or other information by college/school teachers/professors for the students. Written in Django.


### Features
* Teachers can login and post notices.
* Students can only view notices.
* Individual section for each kind of opportunity eg- seminar,contests or hiring .
* Centrally controlled by a single user that is the admin ( whose priveledges are given to all teachers) .
* Opportunities can be mentioned by short descrition .
* Responsive design.



## How to setup

1. Install Python 3.6, Git and [Virtualenv] in your computer.

2. Get the source code on your machine.

    `git clone https://github.com/bhumirao/Phoenix.git`

3. Create a Python virtual environment and install Python and Django related dependencies.

    ```shell
    cd phoenix
    virtualenv venv # create virtual env
    venv\scripts\activate  # run this command everytime before starting on the project
    ---pip install -r requirements.txt
    ```

5. For running the server
   
    `python manage.py runserver`

6. Open the browser and go to to the following link.

    `http://127.0.0.1:8000/`


[virtualenv]: https://virtualenv.pypa.io/

# Simple-Reorder-Module

## Local Setup 
Before setting up, please make sure that you have Python3.6+ installed and running on your machine. 

1.  Clone the repo
```bash
  git clone git@github.com:nickmwangemi/Simple-Reorder-Module.git
```

2. Change directory into the project folder
```bash
  cd Simple-Reorder-Module
```

3. Setup virtual environment and activate it
```bash
  virtualenv env
  source env/bin/activate
```

4. Configure environment variables by using the `env.sh.example` file. Remove the `.example` suffix from the file and then load the environment variables.
``` bash
  source env.sh
```

5. Install dependencies
```bash
  pip3 install -r requirements.txt
```

6. Create database
```bash
  python manage.py migrate
```

7. Create admin account
```bash
  python manage.py createsuperuser
```

8. Run server
```bash
  python manage.py runserver
```

The server should be available at [http://127.0.0.1:8000](http://127.0.0.1:8000), while the admin panel will be at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


## Tech Stack
This application is built using Django.


## Live Demo
A live demo of this project is available at: [Simple Reorder Module](https://nicks-simple-reorder-module.herokuapp.com/)

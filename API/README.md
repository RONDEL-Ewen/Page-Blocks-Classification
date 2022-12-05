# Installation


* Create a virtual environment, activate it, and download the required packages:
```bash
python -m venv .venv
.venv\Scripts\activate.psl # or .venv\Scripts\activate.bat for cmd.exe
pip install -r requirements.txt
```

* Run the migrations
```
python manage.py migrate
```

* Launch the app
```
python manage.py runserver
```

The app is accessible at `http://127.0.0.1:8000/api/`

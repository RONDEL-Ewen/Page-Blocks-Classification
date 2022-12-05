# Installation


* Create a virtual environment, activate it, and download the required packages:
```bash
python -m venv .venv
.venv\Scripts\activate.psl # or .venv\Scripts\activate.bat for cmd.exe
pip intall -r requirements.txt
```

* Run the migrations
```
python manage.py migrate
```

* Launch the app
```
python manage.py runserver
```

You should get a message like the following:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 01, 2022 - 16:35:30
Django version 4.1.3, using settings 'pythondata_API.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

The app is accessible at `http://127.0.0.1:8000/api/` (replace `http://127.0.0.1:8000/` by your own development server if needed)

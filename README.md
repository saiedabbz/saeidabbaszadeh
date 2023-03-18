This is the Django application of Mehrsaman built on `python`.

# Setting up the environment

Open your terminal or command prompt and navigate to the directory where you have cloned the Django app


```Bash
python -m venv env
```
 This will create a new virtual environment inside your app's directory.

if Virtualenv not Installed :

```Bash
python -m pip install --user virtualenv
```

#


## Activate the virtual environment:

```Bash
source env/bin/activate
```
This will activate the virtual environment.

#
## Install the required dependencies:

```Bash
pip install -r requirements.txt 
```
This will install all the necessary dependencies for the app.

#

## Run the Django development server

Install cross-env package globally using this command

```Bash
python manage.py runserver
```
This will start the Django development server and you can access the app by opening your web browser and navigating to http://localhost:8000.

#
That's it! You have successfully cloned a Django app, installed the virtual environment, pip, all the necessary dependencies, and started the development server.





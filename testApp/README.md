Prereqs:
1) Have node.js setup on your environment
2) Have python setup on your enviornment

Setup:
1) Create a virtual environment setup(This can be created in any dir, it also doesn't have to be named venv):
  a) run: virtualenv -python=`which python3` venv
2) Activate the virtual enviroment:
  a) run: source [path to virtual enviorment]/bin/activate
  b) You should now see your virual enviroment in parentheses ex: (venv)
3) Install dependencies:
  a) run: pip install -r [path to]requirements.txt
4) Run migrations:
  a) run: python manage.py makemigrations
  b) run: python manage.py migrate
  c) run: python manage.py populate_db
5) Setup the frontend
  a) cd to frontend dir and run: "npm install" or "yarn install"

Running the services:
1) For the backwnd run: python manage.py runserver
2) For the frontend run in the frontend dir: "yarn start" or "npm start"

Use:
You will need a token to access the endpoints. You can get the token by making a post request passing a valid username and password. Then adding it to your "Autherization" header when making api calls for example: "Token [token]"
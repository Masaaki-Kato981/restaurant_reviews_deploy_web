## Pre-requiste:
- installed packages within `installments.txt`
- have `app.py` file with database credentials imported

## Create table
- run the following code within the terminal of the working directory of the flask app file
```python
# run flask shell
export FLASK_APP=app
flask shell

# import database object
from app import db, Reviews
db.create_all() # creates table in app.py
```
# resturant_reviews

This code was adapted from a class project and utlilized parts of code from [this website](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application) to create template of the web design.

This code was designed so that it can be run on your own local PostgreSQL database.
- the `installments.txt` provide the packages that should be installed for this code
- the `setup.md` provides instructions on how to create table in the PostgreSQL database directly through the flask shell
- NOTE: this code assumes that there is you already created a local PostgreSQL database
    - additionally, the connection to the database is dependent on the local database credentials (i.e., DB_user_name, DB_user_password, DB_host, DB_port)
    - These credentials are stored in a `config.py` file within the working directory and imported to the `app.py` file
    - For security, the `config.py` will not be uploaded to the Github Respository.
    - So, to properly run this code, create your own `config.py` file
    - For more information, use [this website](https://janakiev.com/blog/python-credentials-and-configuration/)


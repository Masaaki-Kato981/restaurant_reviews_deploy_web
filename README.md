# resturant_reviews

The web app can be accessed [here](https://restaurant-reviews-fun.onrender.com/)

This web app was created using python (flask) and the data is managed through a cloud PostgreSQL database on render.com. The website is also hosted on render.com

The code can be run by installing packages detailed in `requirements.txt`.
- However, you must change the `app.config['SQLALCHEMY_DATABASE_URI']` variable to fit your own database connection
- This code utilizes environment variables to store the database credentials, which are within a `.env` file (hidden)
- create your own `.env` file with your own database credential to run the app

This code was adapted from a class project and utlilized parts of code from [this website](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application) to create template of the web design.


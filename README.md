### Application Name
* BLOG-WEB

## Author
* JOHN Mariga

### Description
* A website for user to create their blogs depending on the categories of their choice,comment on other people's blogs and share the their views on trending things through their blogs.
* A user can also upload their image and create a bio for more followers and popularity.

## BDD
>Login Inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg johndoe``|
| Password  | Account password, ``eg parseword``|

>Signup inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg johndoe``|
| Email  | User email, ``eg morty@testmail.com``|
| Password  | Account password, ``eg parseword``|
| Confirm Password  | Account password, ``eg parseword``|


> Blog inputs

| Inputs | Description  |
|---|---|
|  Blog title | the title of the blog eg; `` Car news``  |
|  Blog post| The blog post itself|
| Comment| A comment on the blog post|




## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/Mariga123/BLOGS.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd BLOGS
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.6 manage.py server
  ```
5. Testing the application
  ```bash
  python3.6 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)
* [Bootstrap](https://getbootstrap.com/)


## Support and contact details
* email *johnmariga8@gmail.com*
* phn: *0742249975*
* fb *zellyjones*
* instagram *Mariga john*

### License
licensed under [MIT license](LICENSE)
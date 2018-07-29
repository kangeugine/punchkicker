### PunchKicker

Website for gathering human input data for MMA

## What does this code do?
 - Shows user a picture of two fighters on a browser
 - User draws rectangles around objects
 - User's input is collected to database
 - Repeat

## AWS Tech Stack
 - AWS S3
 - AWS RDS
 - AWS Elastic Beanstalk
 
## How to run this code?
```
$ git clone <repository url>
$ cd punchkicker
$ pip install -r requirements.txt
$ vim config.py
```
add "SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'" to config.py
```
$ python db_create.py
$ python application.py
```
point your browser to `http://0.0.0.0:5000`

You won't see any pictures because `image_url` is not provided from local database.

## Contact
 - eugine.project@gmail.com




# Test challenge for DevelopsToday
Setting up development version of this project:
1) Clone the repository using command:
   `git clone https://github.com/lncr/dt_test_task.git .`
2) Start the project with docker-compose:
   `docker-compose up --build`
3) All set. Now your server is running at http://0.0.0.0:8000


Then add some dummy data for testing, run this command:
`docker exec {name of your app container} ./manage.py filldb`

Deploy link:
https://dttesttaskapp.herokuapp.com/

Postman collection link:
https://documenter.getpostman.com/view/10265507/TWDWKdMy

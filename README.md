For running the DB follow these steps:

1. Run inside the Back folder the next command (with the dot):
docker build -t home_assignment_back . 

2. Run the next command:
docker run --name home_assignment_back_c -p 5000:5000 --rm home_assignment_back

3. Now there is a connection to DB and it's running on port 5000

4. To stop and remove the container just run this command:
docker stop home_assignment_back_c

5. Open README file in the front folder and follow its steps
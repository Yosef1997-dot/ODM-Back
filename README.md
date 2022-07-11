# To use this DB first add '.env' file and declare the 'CONNECTION_STR' inside

**Creating image and running the DB in container:**

1. Run inside the Back folder the next command (with the dot):
docker build -t home_assignment_back . 

2. Run the next command:
docker run --name home_assignment_back_c -p 5000:5000 --rm home_assignment_back

3. Now there is a connection to DB and it's running on port 5000

4. To stop and remove the container just run this command:
docker stop home_assignment_back_c

5. Open README file in the front folder and follow its steps


**Running locally using virtual env**

1. Run inside the Back folder the next command:
virtualenv env

2. Run the next command:
source env/bin/activate

3. Run the next command:
pip3 install -r requirements.txt

4. Run the next command:

python3 router.py
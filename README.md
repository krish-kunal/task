STEPS to follow to parse bank statement of SBI:

For State Bank of India

1)Create virtual environment
  python3 -m venv myenvname
  
2)activate virtual environment
  source myenvname/bin/activate
  
3)clone the repo to your system
git pull https://github.com/krish-kunal/task.git

4)change diretory to bank
cd bank

5)install all requirements using given command
  pip install -r requirements.txt

6)make sure to run makemigrations: Create the migrations (generate the SQLcommands).
  python manage.py makemigrations
 
7) make sure to run migrate:Run the migrations (execute the SQL commands)
  python manage.py migrate

8) start the server
  python manage.py runserver

9) API endpoints:

1) To upload pdf file (Sample file-- kk.pdf)
http://127.0.0.1:8000/upload/

2) To view the statement(sample name-- Mr. KRISHNA KUNAL)
http://127.0.0.1:8000/view/

3) Admin panel
http://127.0.0.1:8000/admin/

Username-krish

Password-kk2357

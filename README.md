### Practicing migrating my personal site from `Django` to `Flask`

* Front-end framework: `Bootstrap 4`
* Back-end framework: `Flask`
* PaaS: `Heroku`

-----

### Learning how to use pipenv

* Install `pipenv`
  ```shell
  $ pip install pipenv
  ```
* Create root directory for git repository
  ```shell
  $ mkdir RobertHWChiangFlask && cd RobertHWChiangFlask
  ```
* Specify the version of Python
  ```shell
  $ pipenv --python 3.7
  ```
* Create `.gitignore` file
* Create a new git repository and the first commit
  ```shell
  $ git init
  $ git add -A
  $ git commit -m 'first commit with pipenv installation'
  $ git remote add origin https://CutestPiglet@github.com/CutestPiglet/RobertHWChiangFlask.git
  $ git push -u origin master
  ```
-----

### Heroku

* Install `gunicorn`
  ```shell
  $ pipenv install gunicorn
  ```
* Create `Procfile` file to specify Heroku app process type
  ```
  web: gunicorn hwchiang.app:app
  ```
* Create `runtime.txt` file to specify which version of Python should be used
  ```
  python-3.7.5
  ```
* Install Heroku CLI
* Log in to Heroku
  ```shell
  $ heroku login
  ```
* Create a new Heroku app
  ```shell
  $ heroku create robertchiang
  ```
* Create a Heroku remote for exsiting Heroku app
  ```shell
  $ heroku git:remote -a robertchiang
  ```
* Deploy
  ```shell
  $ git push heroku master
  Counting objects: 176, done.
  Delta compression using up to 4 threads.
  Compressing objects: 100% (166/166), done.
  Writing objects: 100% (176/176), 3.60 MiB | 804.00 KiB/s, done.
  Total 176 (delta 56), reused 0 (delta 0)
  remote: Compressing source files... done.
  remote: Building source:
  remote: 
  remote: -----> Python app detected
  remote: -----> Installing python-3.7.5
  remote: -----> Installing pip
  remote: -----> Installing dependencies with Pipenv 2018.5.18…
  remote:        Installing dependencies from Pipfile.lock (e78d47)…
  remote: -----> Installing SQLite3
  remote: -----> Discovering process types
  remote:        Procfile declares types -> web
  remote: 
  remote: -----> Compressing...
  remote:        Done: 64.1M
  remote: -----> Launching...
  remote:        Released v3
  remote:        https://robertchiang.herokuapp.com/ deployed to Heroku
  remote: 
  remote: Verifying deploy... done.
  To https://git.heroku.com/robertchiang.git
   * [new branch]      master -> master
  ```

Install
=========

* Open terminal

* Go to the path you want create the project and create a folder

  ```
  mkdir cryptora && cd cryptora
  ```

* Create a virtual machine

    ```
    virtualenv env
    ```

* Open the virtual machine

    ```
    source env/bin/activate
    ```

* Create the project

    ```
    django-admin.py startproject --template=https://github.com/pedrosilva88/djagoTemplate/archive/master.zip --extension=py,rst,html cryptora
    ```

* Enter in the Prject folder

    ```
    cd cryptora
    ```

* Install the requirements
    ```
   pip install -r requirements/local.txt
    ```

 Database
 =========

  * Open Postgres shell (You should have PostGres installed)

   ```
   sudo su - postgres
   ```

 * Create Database

   ```
   CREATE DATABASE cryptora;
   ```

 * Create User to manage database

   ```

   CREATE USER  WITH PASSWORD '';
   ALTER ROLE  SET client_encoding TO 'utf8';
   ALTER ROLE  SET default_transaction_isolation TO 'read committed';
   ALTER ROLE  SET timezone TO 'UTC';
   \q
   ```

 Start Project
 ============

  ```

  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
  
  ```




Frontend & Backoffice Configs
=============================

```

cd  {PathToProject}/{ProjectName}/
mkdir libraries && cd libraries
npm init -y
npm i webpack webpack-cli --save-dev

```

* Now open up package.json and configure the scripts:

```
"scripts": {
  "dev": "webpack --mode development ./project/frontend/src/index.js --output ./project/frontend/static/frontend/main.js",
  "build": "webpack --mode production ./project/frontend/src/index.js --output ./project/frontend/static/frontend/main.js"
}
```

```
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties --save-dev
npm i react react-dom prop-types --save-dev
npm i weak-key --save-dev
npm install bulma--save-dev
npm install css-loader --save-dev
npm install extract-text-webpack-plugin@next --save-dev
npm install node-sass --save-dev
npm install sass-loader --save-dev
npm install style-loader --save-dev
```

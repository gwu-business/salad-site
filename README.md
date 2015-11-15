# Salad System (Python Implementation)

An example database-connected web app,
 with server-side software written in Python.

## Usage

Download the repository.

```` sh
git clone git@github.com:gwu-business/salad-site.git
cd salad-site
````

Create a new local database
 and populate it with menu data (requires mysql).

```` sh
# if your root user does not have a password: run these commands without the -p flag, or press enter when prompted for a password ...
cat database/create.sql | mysql -u root -p
mysql -uroot -p salad_db < database/migrate.sql
mysql -uroot -p salad_db < database/populate.sql
````

Install python package dependencies (requires python and pip).

```` sh
pip install -r software/requirements.txt
````

Create another menu item record, this time using a python script.

```` sh
python software/add_menu_item.py
````

Start a local web server.

```` sh
python software/start_local_web_server.py
````

Visit [localhost:8818](localhost:8818) in a browser
  to view the menu
  and create new menu items.


## [License](LICENSE.md)

# Salad Site

## Usage

Download the repository.

```` sh
git clone git@github.com:gwu-business/salad-site.git
cd salad-site
````

Run the scripts in the [database](database) directory in order (create, migrate, populate)
 to create a new MySQL database
 and populate it with data.

```` sh
# if your root user does not have a password:
# ... run these commands without the -p flag,
# ... or press enter when prompted for a password ...
cat database/create.sql | mysql -u root -p
mysql -uroot -p salad_db < database/migrate.sql
mysql -uroot -p salad_db < database/populate.sql
````

Install python package dependencies (requires python and pip).

```` sh
pip install -r software/requirements.txt
````

Start a local web server (requires python).

```` sh
python software/salad_server.py
````

Visit localhost:8818 in a browser.

## [License](LICENSE.md)

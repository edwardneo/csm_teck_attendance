## Setup

To setup this repository, create a new virtual environment and activate it with
```sh
python3 -m venv venv
source venv/bin/activate
```

Install all python dependencies with
```sh
pip3 install -r requirements.txt
```

Install all node dependencies with
```sh
npm i
```

Setup the backend database and create some dummy data with
```sh
python3 manage.py migrate
python3 manage.py createtestdata
```

Now, in two separate terminal windows,
* Run the Django server:
  ```sh
  python3 manage.py runserver
  ```

* Compile the React code (watching changes):
  ```sh
  npm run watch
  ```

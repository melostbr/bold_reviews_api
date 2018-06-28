# Bold Reviews API

## Prerequisites
  - Python ~= 2.7
  - [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)
  - PostgreSQL ~= 10

## Development
  - Download this project and `cd` inside of it;
  - Run `mkvirtualenv  reviewer_api`;
  - Run `pip install -r requirements.txt`;
  - Run `workon test_api`;
  - Edit `$VIRTUAL_ENV/bin/postactivate` to set these local variables:
    ```
    export APP_SETTINGS="config.DevelopmentConfig"
    export FLASK_APP="app/__init__.py"
    export FLASK_ENV=development
    export SQLALCHEMY_DATABASE_URI='postgresql://{user}:{passwd}@localhost/reviews_api'
    ```
  - Edit `$VIRTUAL_ENV/bin/postdeactivate` to unset them:
    ```
    unset APP_SETTINGS
    unset FLASK_APP
    unser FLASK_ENV
    unset SQLALCHEMY_DATABASE_URI
    ```

## Running
  - `make runserver` or `flask run` at root folder

## Testing


## License

Copyright © 2018 Stefanie Melo

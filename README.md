# Reviewer API

## Prerequisites
  - Python ~= 2.7
  - [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

## Development
  - Download this project and `cd` inside of it;
  - Run `mkvirtualenv  reviewer_api`;
  - Run `pip install -r requirements.txt`;
  - Run `workon test_api`;
  - Edit `$VIRTUAL_ENV/bin/postactivate` to set these local variables:
    ```
    export APP_SETTINGS="config.DevelopmentConfig"
    export FLASK_APP="app/app.py"
    ```
  - Edit `$VIRTUAL_ENV/bin/postdeactivate` to unset them:
    ```
    unset APP_SETTINGS
    unset FLASK_APP
    ```

## Running
  - `make runserver` or `flask run` at root folder

## Testing


## License

Copyright © 2018 Stefanie Melo

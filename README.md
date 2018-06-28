# Bold Reviews API

## Prerequisites
  - Python ~= 2.7.15
  - [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)
  - PostgreSQL ~= 10

## Development
  - Download this project and `cd` inside of it;
  - Run `mkvirtualenv  reviews_api`;
  - Run `pip install -r requirements.txt`;
  - Run `workon reviews_api`;
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

## Resources
  - <code>GET</code> `/{bold_application_name}/reviews` to get the first 20
    reviews;
  - <code>GET</code> `/{bold_application_name}/reviews?page={page_number}` to
    get more than the first 20 reviews/;

## Responses
### Success Response:
  - Status Code: 200;
  - JSON example:
  ```
    {
      "id": 6958,
      "shopify_domain": "islamicshopping24.myshopify.com",
      "app_slug": "product-upsell",
      "star_rating": 5,
      "previous_star_rating": null,
      "created_at": "2018-06-27T21:40:00.517504+00:00",
      "updated_at": null
    }
  ```

### Error Response:
  - Status Code: 404

## License

Copyright © 2018 Stefanie Melo

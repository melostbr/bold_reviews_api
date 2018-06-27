import requests

class ReviewsController:
    def all(self, app):
        uri = "https://apps.shopify.com/{}/reviews.json".format(app)
        res = requests.get(uri)
        if res.status_code != 200: return res.status_code

        return res.json()


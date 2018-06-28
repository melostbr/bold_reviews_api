import requests
import app
from sqlalchemy.sql import func
from app.models import *

class ReviewsController:
    def fetch_reviews(self, app, page):
        reviews = Review.query.filter(Review.app_slug == app).paginate(page=page)
        reviews_schema = ReviewSchema(many=True)
        return reviews_schema.dump(reviews.items)

    def save_reviews(self):
        bold_apps = ['product-upsell', 'product-discount', 'store-locator',
                    'product-options', 'quantity-breaks', 'product-bundles',
                    'customer-pricing', 'product-builder', 'social-triggers',
                    'recurring-orders', 'multi-currency', 'quickbooks-online',
                    'xero', 'the-bold-brain']

        for bold_app in bold_apps:
            uri = "https://apps.shopify.com/{}/reviews.json".format(bold_app)
            res = requests.get(uri)
            if res.status_code != 200: continue
            reviews = res.json()

            for review in reviews['reviews']:
                review_data = Review.query.filter_by(shopify_domain=review['shop_domain']).first()
                if review_data:
                    self.update(review_data, review)
                else:
                    self.create(review, bold_app)
        app.db.session.close()

    def update(self, review_data, review):
        review_data.previous_star_rating = review_data.star_rating
        review_data.star_rating = review['star_rating']
        review_data.updated_at = func.now()
        app.db.session.commit()

    def create(self, review, bold_app):
        review_data = Review(shopify_domain=review['shop_domain'],
                             app_slug=bold_app,
                             star_rating=review['star_rating'],
                             created_at=func.now())
        app.db.session.add(review_data)
        app.db.session.commit()

from app import db

class Review(db.Model):
    __tablename__ = "shopify_app_reviews"

    id = db.Column(db.Integer, primary_key=True)
    shopify_domain = db.Column(db.String())
    app_slug = db.Column(db.String())
    star_rating = db.Column(db.Integer)
    previous_star_rating = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)

    def __init__(self, shopify_domain, app_slug,
                 star_rating, previous_star_rating,
                 updated_at, created_at):
        self.shopify_domain = shopify_domain
        self.app_slug = app_slug
        self.star_rating = star_rating
        self.previous_star_rating = previous_star_rating
        self.updated_at = updated_at
        self.created_at = created_at

    def __repr__(self):
        return '<Review {}>'.format(self.id)

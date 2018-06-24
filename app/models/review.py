from app import db
from sqlalchemy.dialects.postgresql import JSON

class Review(db.Model):
    __tablename__ = "shopify_app_reviews"

    id = db.Column(db.Integer, primary_key=True)
    shopify_domain = db.Column(db.String())
    app_slug = db.Column(db.String())
    star_rating = db.Column(db.Integer)
    previous_star_rating = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)

    def __repr__(self):
        return 'Review {}'.format(self.id)

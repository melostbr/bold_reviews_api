from flask_marshmallow import Schema

class ReviewSchema(Schema):
     class Meta:
        ordered = True
        fields = ('id', 'shopify_domain', 'app_slug', 'star_rating',
                'previous_star_rating', 'updated_at', 'created_at')

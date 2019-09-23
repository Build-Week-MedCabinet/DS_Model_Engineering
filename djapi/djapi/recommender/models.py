from django.db.models import \
    (Model, DateTimeField, CharField, IntegerField, TextField)
from django.core.validators import MaxValueValidator, MinValueValidator


# User Classes
# Creates options list for UserRating.userclass
user_classes = ['default', 'recreational', 'medical']
user_class_choices = sorted(zip(range(len(user_classes)), user_classes))


# User Ratings Model for online analysis, updating the recommender ranking
class UserRating(Model):
    created = DateTimeField(
        auto_now=True)
    username = CharField(
        max_length=100,
        blank=True,
        default='defaultuser')
    userclass = CharField(
        choices=user_class_choices,
        default='default',
        max_length=100,
        blank=True)
    # Ratings must be scaled down to 1-5 per kaggle dataset original data or
    #  updated recommendations will be skewed.
    # These validators may not work in API context.
    strain_name = CharField(
        max_length=100,
        blank=False,
        editable=True,
        default='default'
    )
    rating = IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ])

    class Meta:
        ordering = ['created']


# Class for storing strain data.
# Includes both raw text information and embeddings
class Strain(Model):
    created = DateTimeField(
        auto_now=True)
    updated = DateTimeField(
        auto_now=True,
        editable=True)
    strain_name = CharField(
        max_length=100,
        blank=False,
        editable=True,
    )
    # Long form information to be stored as text (huge strings).
    #   Any request trying to input data to these fields will need to be
    #   formatted appropriately if using Sqlite3 database.
    # PostgreSQL offers some advance list-like and json fields, but
    #   requires setup and connection to external postgreSQL database.
    strain_effect_list = TextField(blank=False, editable=True)
    strain_flavor_list = TextField(blank=False, editable=True)
    strain_desc = TextField(blank=True, editable=True)
    strain_effect_embed = TextField(blank=True, editable=True)
    strain_flavor_embed = TextField(blank=True, editable=True)
    strain_desc_embed = TextField(blank=True, editable=True)

    class Meta:
        ordering = ['created']

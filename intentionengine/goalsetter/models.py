from django.db import models
from django.utils import timezone

# Create your models here.

category_choices = (
    (1, "Financial"),
    (2, "Spiritual"),
    (3, "Family"),
    (4, "Work/Career"),
    (5, "Social"),
    (6, "Physical/Health"),
    (7, "Mind/Intellect"),
    (8, "Personal Development"),
)

class Goals(models.Model):
    label = models.CharField(max_length=200)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    category = models.IntegerField('Category', choices=category_choices)

    def financial_goals(self):
        return self.category == 1

    def spiritual_goals(self):
        return self.category == 2

    def family_goals(self):
        return self.category == 3

    def work_career_goals(self):
        return self.category == 4

    def social_goals(self):
        return self.category == 5

    def physical_health_goals(self):
        return self.category == 6

    def mind_intellect_goals(self):
        return self.category == 7

    def personal_development_goals(self):
        return self.category == 8

    def __str__(self):
        return self.label

class Inspiration(models.Model):
    text = models.CharField(max_length=400)
    inspire_id = models.IntegerField('inspire_id')

    def __str__(self):
        return self.text
from django.db import models


class EducationFoodWaste(models.Model):
    date = models.DateField()
    food_item = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    reason = models.CharField(max_length=200)

    def __str__(self):
        return self.food_item

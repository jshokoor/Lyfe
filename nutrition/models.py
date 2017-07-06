from django.db import models
from django.core.urlresolvers import reverse


class DailyDietTotals(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    total_KCALS = models.IntegerField(default=0)
    total_protein = models.IntegerField(default=0)
    total_carbs = models.IntegerField(default=0)
    total_fat = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('nutrition:detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return str(self.total_KCALS) + ' - ' + str(self.total_protein) + ' - ' + str(self.total_carbs) + ' - ' + str(self.total_fat)


class Meal(models.Model):
    daily_diet = models.ForeignKey(DailyDietTotals, on_delete=models.CASCADE)
    type_of_meal = models.CharField(max_length=250)
    KCALS = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    is_favorite = models.BooleanField(default=False)

    def __self__(self):
        return self.type_of_meal

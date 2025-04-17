from django.db import models
from django.urls import reverse
# Create your models here.
# A tuple of 2-tuples added above our models
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

 # new code below
    def __str__(self):
        return self.name
    
# Define a method to get the URL for this particular cat instance
    def get_absolute_url(self):
        # Use the 'reverse' function to get the URL for the cat detail view
        return reverse("cat_detail", kwargs={'cat_id': self.id})
    


class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    # Create a cat_id column for each feeding in the database
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
     # Define the default order of feedings
    class Meta:
        ordering = ['-date']  # This line makes the newest feedings appear first

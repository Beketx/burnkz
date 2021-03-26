from django.db import models

class Progammer(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    main_job = models.ForeignKey(to="itskill.Category", on_delete=models.CASCADE, related_name="jobs")
    skills = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    city = models.OneToOneField(to="City", on_delete=models.CASCADE)
    year = models.DateField()
    rating = models.ForeignKey(to="Rating", on_delete=models.CASCADE)
    price_from = models.IntegerField()

    def __str__(self):
        return self.name

class ProgrammerImage(models.Model):
    programmer = models.ForeignKey(to="Progammer", on_delete=models.CASCADE)
    image = models.ImageField()

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Rating(models.Model):
    communication = models.FloatField()
    quality = models.FloatField()
    truth_review = models.FloatField()

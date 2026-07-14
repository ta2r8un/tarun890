from django.db import models

class Service(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    short = models.CharField(max_length=300)
    description = models.TextField()
    starting_price = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feature(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="features"
    )
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
class Technology(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="technologies"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Outcome(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="outcomes"
    )
    label = models.CharField(max_length=200)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.label} - {self.value}"
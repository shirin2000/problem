from django.db import models

class Problems(models.Model):
    sector = models.CharField(max_length=20)
    problem_definition = models.TextField()
    problem = models.CharField(max_length=100)  # Add the 'problem' field
    summary = models.TextField()  # Add the 'summary' field
    reff_link = models.URLField(max_length=200) 

    def __str__(self):
        return f"{self.sector} - {self.problem_definition[:50]}" 
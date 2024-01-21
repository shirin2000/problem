from django.db import models

class Problems(models.Model):
    sector = models.CharField(max_length=20)
    problem = models.CharField(max_length=100)  # Add the 'problem' field
    summary = models.TextField()  # Add the 'summary' field
    reff_link = models.URLField(max_length=200) 

    def __str__(self):
        return f"{self.sector} - {self.problem_definition[:50]}" 

class MyProject(models.Model):
    sector = models.CharField(max_length=20)
    problem = models.TextField()  # Corresponding values of the "Problem" column
    solution = models.TextField()
    current_status = models.CharField(max_length=100)
    works_left = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    heading = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def short_content(self):
        return self.content[:100] + ('...' if len(self.content) > 100 else '')

    def __str__(self):
        return self.heading

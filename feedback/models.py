from django.db import models

class Feedback(models.Model):
    CATEGORIES = [('Timely Project Completion', 'Timely Project Completion'),
                  ('Management Ratings','Management Ratings'),
                  ('Daily Projects Reports','Daily Projects Reports'),
                  ('Design Proficiency','Design Proficiency'),
                  ('Inspection','Inspection'),
                  ('Overall Client Rating','Overall Client Rating')]
    category = models.CharField(max_length=100, choices=CATEGORIES)  # e.g., "Timely Project Completion"
    rating = models.PositiveIntegerField()  # Percentage (0 to 100)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically adds the timestamp when a record is created


    def __str__(self):
        return self.category


from django.db import models

from django.db import models

class Count(models.Model):
    TITLE_CHOICES = [
        ('Happy Clients', 'Happy Clients'),
        ('Projects', 'Projects'),
        ('Hours Of Support', 'Hours Of Support'),
        ('Hard Workers', 'Hard Workers'),
    ]

    ICON_CLASS_CHOICES = [
        ('bi bi-emoji-smile', 'bi bi-emoji-smile'),
        ('bi bi-journal-richtext', 'bi bi-journal-richtext'),
        ('bi bi-headset', 'bi bi-headset'),
        ('bi bi-people', 'bi bi-people'),
    ]

    title = models.CharField(max_length=100, choices=TITLE_CHOICES)
    icon_class = models.CharField(max_length=100, choices=ICON_CLASS_CHOICES, blank=True)
    value = models.PositiveIntegerField()  # The numerical count

    def save(self, *args, **kwargs):
        if not self.icon_class:  # Set icon_class if it's not already set
            if self.title == 'Happy Clients':
                self.icon_class = 'bi bi-emoji-smile'
            elif self.title == 'Projects':
                self.icon_class = 'bi bi-journal-richtext'
            elif self.title == 'Hours Of Support':
                self.icon_class = 'bi bi-headset'
            elif self.title == 'Hard Workers':
                self.icon_class = 'bi bi-people'
        super().save(*args, **kwargs)  # Save the instance

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=255)  # You can store the client name as well
    logo = models.ImageField(upload_to='clients/')  # Store client logo image

    def __str__(self):
        return self.name

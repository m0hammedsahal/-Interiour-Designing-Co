from django.db import models



class Video(models.Model):
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')  # Use FileField for video upload

    class Meta:
        db_table = 'web_video'
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        ordering = ['-id']

    def __str__(self):
        return self.name



class TeamMember(models.Model):
    # Define the fields for the Team Member model
    name = models.CharField(max_length=255)  # To store the team member's name
    role = models.CharField(max_length=255)  # To store their position or role
    image = models.ImageField(upload_to='team_images/')  # To store the profile image

    class Meta:
        db_table = 'team_member'  # Custom table name
        verbose_name = 'Team Member'  # Admin display name
        verbose_name_plural = 'Team Members'
        ordering = ['id']  # Order by ID by default

    def __str__(self):
        return self.name  # Display team member's name as string representation

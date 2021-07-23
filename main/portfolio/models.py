from django.db import models


class Projects(models.Model):
    main_image = models.ImageField(upload_to='projects_image/')
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=1200)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.name} Project'


class ProjectSecondaryImage(models.Model):
    image = models.ImageField(upload_to='project_secondary_image/')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.image} {self.project}'


class About(models.Model):
    description = models.TextField(max_length=800)
    cv = models.FileField(upload_to="about/cv/")
    picture = models.ImageField(upload_to="about/picture/")

    def __str__(self):
        return 'About Description'


class Contact(models.Model):
    name = models.CharField(max_length = 200)
    value = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='contact_images')

    def __str__(self):
        return f'{self.name}'


class Messages(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    subject = models.CharField(max_length = 250)
    content = models.TextField()

    def __str__(self):
        return f'Message de {self.name} au sujet de {self.subject}'
    
    
    
    
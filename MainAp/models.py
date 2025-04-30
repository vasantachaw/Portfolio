from django.db import models


class Developer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    EMPLOYMENT_TYPE = [
        ('FT', 'Full-Time'),
        ('PT', 'Part-Time'),
        ('CT', 'Contract'),
        ('FR', 'Freelancer'),
    ]

    # Example field

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30)
    address = models.TextField()
    zip_code = models.CharField(max_length=10,default='44417')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    github_profile = models.URLField(blank=True, null=True)
    facebook_profile = models.URLField(blank=True, null=True)
    youtube_profile = models.URLField(blank=True, null=True)

    company_profile = models.URLField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    experience_years = models.PositiveIntegerField()
    current_employer = models.CharField(max_length=100, blank=True)
    employment_type = models.CharField(
        max_length=2, choices=EMPLOYMENT_TYPE, blank=True)
    available_for_hire = models.BooleanField(default=True)
    skills = models.TextField(
    default='''[
    "Python Developer.",
    "Django Developer .",
    "frontend Developer.",
    "Git.",
    "Machine Learning.",
    "Deep Learning.",
    "Natural Language Processing.",
    "Computer Vision.",
    "Data Analysis.",
    "AWS.",
    "Docker.",
    "Kubernetes.",
    "Linux."
    ]'''
)


    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='developer_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Company(models.Model):
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=150, default='Gaulley')
    industry_type = models.CharField(max_length=100, default='Food & Beverage')
    description = models.TextField(blank=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    logo = models.ImageField(
        upload_to='food_company_logos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    python_developer = models.ForeignKey(
        'Developer', on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=150)
    field_of_study = models.CharField(max_length=100, blank=True)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(blank=True, null=True)
    grade = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

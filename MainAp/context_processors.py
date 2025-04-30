from django.shortcuts import render
from MainAp.models import Developer, Company, Education
import json

def Informations(request):
    developer = Developer.objects.first()
    company = Company.objects.first()
    education = Education.objects.first()

    # Safely load skills
    try:
        skills_list = json.loads(developer.skills) if developer and developer.skills else []
    except json.JSONDecodeError:
        skills_list = []

    context = {
        'developer': developer,
        'company': company,
        'education': education,
        'skills': json.dumps(skills_list)
    }

    return  context

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Project, Skill, Testimonial


SKILL_CATEGORY_ORDER = [
    'Backend',
    'Frontend',
    'Databases',
    'DevOps & Deployment',
    'Workflow & Collaboration',
    'Other'
]


def get_skill_label(level):
    if level >= 90:
        return 'Expert'
    if level >= 80:
        return 'Advanced'
    if level >= 70:
        return 'Strong'
    if level >= 60:
        return 'Proficient'
    return 'Working Knowledge'


def get_skill_category(name):
    normalized_name = name.strip().lower()

    if normalized_name in {'django', 'python', 'gunicorn'}:
        return 'Backend'
    if normalized_name in {'html', 'css', 'bootstrap', 'javascript'}:
        return 'Frontend'
    if normalized_name in {'mysql', 'postgres', 'postgresql'}:
        return 'Databases'
    if normalized_name in {'nginx'}:
        return 'DevOps & Deployment'
    if normalized_name in {'github', 'jira', 'git'}:
        return 'Workflow & Collaboration'
    return 'Other'


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send email
        subject = f"Portfolio Contact: {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.CONTACT_EMAIL]  # You'll need to set this in settings
        
        try:
            send_mail(subject, body, from_email, recipient_list)
            messages.success(request, "Thank you! Your message has been sent successfully.")
        except Exception as e:
            messages.error(request, "Sorry, there was an error sending your message. Please try again.")
        
        return HttpResponseRedirect(reverse('home'))
    
    projects = Project.objects.all()
    skills = Skill.objects.all()
    testimonials = Testimonial.objects.all()
    grouped_skill_map = {category: [] for category in SKILL_CATEGORY_ORDER}

    for skill in skills:
        skill.level_label = get_skill_label(skill.level)
        skill.category = get_skill_category(skill.name)
        grouped_skill_map[skill.category].append(skill)

    skill_groups = [
        {'name': category, 'skills': grouped_skill_map[category]}
        for category in SKILL_CATEGORY_ORDER
        if grouped_skill_map[category]
    ]
    
    # Process projects to split tech_stack
    for project in projects:
        if project.tech_stack:
            project.tech_stack_list = [tech.strip() for tech in project.tech_stack.split(',')]
        else:
            project.tech_stack_list = []
    
    context = {
        'projects': projects,
        'skills': skills,
        'skill_groups': skill_groups,
        'testimonials': testimonials,
    }
    return render(request, 'core/home.html', context)

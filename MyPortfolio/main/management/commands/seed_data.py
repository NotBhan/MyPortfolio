from django.core.management.base import BaseCommand
from django.utils.text import slugify
from main.models import SkillCategory, Skill, Project

class Command(BaseCommand):
    help = 'Populates the database with sample skills and projects'

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")
        
        # Clear existing data
        Project.objects.all().delete()
        Skill.objects.all().delete()
        SkillCategory.objects.all().delete()

        # Create Skill Categories
        web_dev = SkillCategory.objects.create(
            name="Web Development",
            icon="fa-code",
            display_order=1
        )
        programming = SkillCategory.objects.create(
            name="Programming", 
            icon="fa-laptop-code",
            display_order=2
        )
        music = SkillCategory.objects.create(
            name="Music Production", 
            icon="fa-headphones-simple",
            display_order=2
        )

        # Create Skills
        html = Skill.objects.create(
            category=web_dev,
            name="HTML",
            proficiency=90,
            display_order=1
        )
        css = Skill.objects.create(
            category=web_dev,
            name="CSS",
            proficiency=85,
            display_order=2
        )
        bs5 = Skill.objects.create(
            category=web_dev,
            name="Bootstrap",
            proficiency=85,
            display_order=2
        )
        django = Skill.objects.create(
            category=web_dev,
            name="Django",
            proficiency=85,
            display_order=2
        )
        python = Skill.objects.create(
            category=programming,
            name="Python",
            proficiency=80,
            display_order=1
        )
        cpp = Skill.objects.create(
            category=programming,
            name="C, C++",
            proficiency=80,
            display_order=1
        )
        snd_des = Skill.objects.create(
            category=music,
            name="Sound Design",
            proficiency=80,
            display_order=1
        )
        sng_wrt = Skill.objects.create(
            category=music,
            name="Songwriting",
            proficiency=80,
            display_order=1
        )
        mixing = Skill.objects.create(
            category=music,
            name="Mixing",
            proficiency=80,
            display_order=1
        )

        # Create Projects with unique slugs
        portfolio = Project.objects.create(
            title="Portfolio Website",
            slug=slugify("Portfolio Website"),  # Add this line
            short_description="A Django-powered portfolio site",
            featured=True,
            display_order=1
        )
        portfolio.technologies.add(html, css, bs5, django)

        store = Project.objects.create(
            title="Ardnahc Sounds",
            slug=slugify("E-commerce"),  # Add this line
            short_description="An ecommerce website for selling sample packs",
            featured=True,
            display_order=2
        )
        store.technologies.add(html, css, bs5)

        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
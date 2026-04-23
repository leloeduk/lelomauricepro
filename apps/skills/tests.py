from django.test import TestCase
from django.urls import reverse
from .models import Skill


class SkillModelTest(TestCase):
    def setUp(self):
        self.skill = Skill.objects.create(
            name='Python',
            level=85,
            category='Backend'
        )

    def test_skill_creation(self):
        self.assertEqual(self.skill.name, 'Python')
        self.assertEqual(self.skill.level, 85)
        self.assertEqual(self.skill.category, 'Backend')

    def test_skill_str(self):
        self.assertEqual(str(self.skill), 'Python')

    def test_skill_default_level(self):
        skill = Skill.objects.create(name='Django', category='Backend')
        self.assertEqual(skill.level, 50)

    def test_skill_level_bounds(self):
        skill = Skill.objects.create(name='Test', level=0, category='Test')
        self.assertEqual(skill.level, 0)


class SkillsViewsTest(TestCase):
    def test_skills_view(self):
        response = self.client.get(reverse('skills'))
        self.assertEqual(response.status_code, 200)

    def test_skills_template(self):
        response = self.client.get(reverse('skills'))
        self.assertTemplateUsed(response, 'skills/skills.html')

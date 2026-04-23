from django.test import TestCase
from django.urls import reverse
from .models import Project


class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='Mon Projet',
            description='Description du projet',
            tech_stack='Django, Python, HTML',
            image='https://example.com/image.jpg',
            live_url='https://example.com',
            github_url='https://github.com/example'
        )

    def test_project_creation(self):
        self.assertEqual(self.project.title, 'Mon Projet')
        self.assertEqual(self.project.description, 'Description du projet')
        self.assertEqual(self.project.tech_stack, 'Django, Python, HTML')

    def test_project_str(self):
        self.assertEqual(str(self.project), 'Mon Projet')

    def test_project_urls_optional(self):
        project = Project.objects.create(
            title='Projet Simple',
            description='Description',
            tech_stack='Python'
        )
        self.assertIsNone(project.image)
        self.assertIsNone(project.live_url)
        self.assertIsNone(project.github_url)

    def test_project_created_at(self):
        self.assertIsNotNone(self.project.created_at)


class ProjectViewsTest(TestCase):
    def test_project_list_view(self):
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)

    def test_project_list_template(self):
        response = self.client.get(reverse('project_list'))
        self.assertTemplateUsed(response, 'dashboard/projects/list.html')

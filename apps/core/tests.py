from django.test import TestCase
from django.urls import reverse
from .models import SiteHeader


class SiteHeaderModelTest(TestCase):
    def setUp(self):
        self.header = SiteHeader.objects.create(
            title='Mon Titre',
            subtitle='Mon Sous-titre',
            description='Ma description',
            image='header/test.jpg'
        )

    def test_site_header_creation(self):
        self.assertEqual(self.header.title, 'Mon Titre')
        self.assertEqual(self.header.subtitle, 'Mon Sous-titre')
        self.assertEqual(self.header.description, 'Ma description')

    def test_site_header_str(self):
        self.assertEqual(str(self.header), 'Mon Titre')

    def test_site_header_updated_at(self):
        self.assertIsNotNone(self.header.updated_at)


class CoreViewsTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'core/home.html')

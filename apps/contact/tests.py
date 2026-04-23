from django.test import TestCase
from django.urls import reverse
from .models import ContactMessage


class ContactMessageModelTest(TestCase):
    def setUp(self):
        self.message = ContactMessage.objects.create(
            name='Jean Dupont',
            email='jean@example.com',
            subject='Question',
            message='Bonjour, j\'ai une question.'
        )

    def test_contact_message_creation(self):
        self.assertEqual(self.message.name, 'Jean Dupont')
        self.assertEqual(self.message.email, 'jean@example.com')
        self.assertEqual(self.message.subject, 'Question')

    def test_contact_message_str(self):
        self.assertEqual(str(self.message), 'jean@example.com')

    def test_contact_message_default_unread(self):
        self.assertFalse(self.message.is_read)

    def test_contact_message_created_at(self):
        self.assertIsNotNone(self.message.created_at)


class ContactViewsTest(TestCase):
    def test_contact_view_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view_post_valid(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test message'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_template(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'contact/contact.html')

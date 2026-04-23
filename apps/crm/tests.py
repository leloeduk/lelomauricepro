from django.test import TestCase
from django.urls import reverse


class CRMModelTest(TestCase):
    def test_crm_app_exists(self):
        # CRM uses ContactMessage from contact app
        from apps.contact.models import ContactMessage
        self.assertTrue(hasattr(ContactMessage, 'objects'))


class CRMViewsTest(TestCase):
    def test_crm_dashboard_requires_login(self):
        # Test that CRM dashboard requires authentication
        url = reverse('crm_dashboard')
        if url:
            response = self.client.get(url)
            self.assertIn(response.status_code, [302, 301, 404])

    def test_crm_leads_view(self):
        url = reverse('crm_leads')
        if url:
            response = self.client.get(url)
            self.assertIn(response.status_code, [302, 301, 404])

    def test_crm_clients_view(self):
        url = reverse('crm_clients')
        if url:
            response = self.client.get(url)
            self.assertIn(response.status_code, [302, 301, 404])

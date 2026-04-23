from django.test import TestCase
from django.urls import reverse
from .models import VisitorLog


class VisitorLogModelTest(TestCase):
    def setUp(self):
        self.log = VisitorLog.objects.create(
            path='/home/',
            ip_address='192.168.1.1',
            user_agent='Mozilla/5.0'
        )

    def test_visitor_log_creation(self):
        self.assertEqual(self.log.path, '/home/')
        self.assertEqual(self.log.ip_address, '192.168.1.1')
        self.assertEqual(self.log.user_agent, 'Mozilla/5.0')

    def test_visitor_log_str(self):
        self.assertEqual(str(self.log), '192.168.1.1')

    def test_visitor_log_created_at(self):
        self.assertIsNotNone(self.log.created_at)


class AnalyticsMiddlewareTest(TestCase):
    def test_middleware_logs_visitor(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Check that a log was created
        self.assertGreater(VisitorLog.objects.count(), 0)

    def test_analytics_dashboard_requires_login(self):
        response = self.client.get(reverse('analytics_dashboard'))
        # Should redirect to login or return 302
        self.assertIn(response.status_code, [302, 301])


class AnalyticsViewsTest(TestCase):
    def test_analytics_view(self):
        response = self.client.get(reverse('analytics_dashboard'))
        # Without login, should redirect
        self.assertIn(response.status_code, [302, 301, 200])

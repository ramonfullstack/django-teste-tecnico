from django.test import TestCase
from django.contrib.auth.models import User
from .models import Company

class CompanyModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.company = Company.objects.create(
            name='Test Company',
            created_by=self.user
        )

    def test_company_creation(self):
        company = Company.objects.get(name='Test Company')
        self.assertEqual(company.name, 'Test Company')
        self.assertEqual(company.created_by, self.user)

    def test_company_default_values(self):
        company = Company.objects.get(name='Test Company')
        self.assertEqual(company.timezone, '-03:00')
        self.assertEqual(company.language, 'pt')

    def test_company_str_representation(self):
        company = Company.objects.get(name='Test Company')
        expected_str = f"{company.name}"
        self.assertEqual(str(company.name), expected_str)

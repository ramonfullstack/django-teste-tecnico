from django.test import TestCase
from django.contrib.auth.models import User
from company.models import Company
from .models import Doc

class DocModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.company = Company.objects.create(name='Test Company', created_by=self.user)
        self.doc = Doc.objects.create(
            name='Test Document',
            company=self.company,
            created_by=self.user
        )

    def test_doc_creation(self):
        doc = Doc.objects.get(name='Test Document')
        self.assertEqual(doc.name, 'Test Document')
        self.assertEqual(doc.company, self.company)
        self.assertEqual(doc.created_by, self.user)

    def test_doc_default_values(self):
        doc = Doc.objects.get(name='Test Document')
        self.assertFalse(doc.deleted)
        self.assertIsNone(doc.sign_deadline)
        self.assertFalse(doc.signed)

    def test_doc_str_representation(self):
        doc = Doc.objects.get(name='Test Document')
        expected_str = f"{doc.name}"
        self.assertEqual(str(doc.name), expected_str)

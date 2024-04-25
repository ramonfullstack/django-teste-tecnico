from django.test import TestCase
from django.contrib.auth.models import User
from company.models import Company
from doc.models import Doc
from .models import UserProfile

class UserProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.company = Company.objects.create(name='Test Company', created_by=self.user)
        self.doc = Doc.objects.create(name='Test Document', company=self.company, created_by=self.user)
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            original_company=self.company
        )
        self.user_profile.companies.add(self.company)
        self.user_profile.docs.add(self.doc)

    def test_user_profile_creation(self):
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(user_profile.user, self.user)
        self.assertEqual(user_profile.original_company, self.company)

    def test_user_profile_default_values(self):
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertFalse(user_profile.email_verified)
        self.assertIsNone(user_profile.last_password_reset)

    def test_user_profile_associations(self):
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertIn(self.company, user_profile.companies.all())
        self.assertIn(self.doc, user_profile.docs.all())

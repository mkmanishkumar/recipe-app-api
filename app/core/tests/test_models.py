from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating with new users with email is successful"""
        email = "mkmanish.er@gmail.com"
        password = "Mkmanish@123"
        user = get_user_model().object.create_user(
               email=email,
               password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test the new user normalized"""
        email = "mkmanish.er@gmail.com"
        user = get_user_model().object.create_user(email, "Mkmanish@123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating userwith no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().object.create_user(None, "Mkmanish@123")

    def test_create_new_superuser(self):
        """Test creating new super user"""
        user = get_user_model().object.create_superuser(
               "mkmanish.er@outlook.com", "Mkmanish@123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

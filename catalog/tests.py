from django.test import TestCase, Client
from django.urls import reverse


class CoursePortalTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_view(self):
        """Test that the homepage renders with course summary metrics."""
        response = self.client.get(reverse('catalog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to DTI CoursePortal")
        self.assertContains(response, "Active Courses Offered")
        self.assertContains(response, "3")
        self.assertContains(response, "Featured Subject")
        self.assertContains(response, "DTI412")

    def test_course_list_view(self):
        """Test that course listing displays all offered courses."""
        response = self.client.get(reverse('catalog:course_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Offered IT Courses")
        self.assertContains(response, "DTI412")
        self.assertContains(response, "DTI201")
        self.assertContains(response, "DTI305")

    def test_course_list_search_filter(self):
        """Test Extension Challenge Task: GET search parameter filtering."""
        # Search by code
        response = self.client.get(reverse('catalog:course_list'), {'q': 'DTI412'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Special Topic in Application Development")
        self.assertNotContains(response, "Database Systems")
        self.assertNotContains(response, "Frontend Web Technologies")

        # Search by keyword in title
        response = self.client.get(reverse('catalog:course_list'), {'q': 'Database'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DTI201")
        self.assertNotContains(response, "Special Topic in Application Development")
        self.assertNotContains(response, "Frontend Web Technologies")

        # Search for non-existent course
        response = self.client.get(reverse('catalog:course_list'), {'q': 'NonExistentXYZ'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No courses are currently listed in the catalog.")

    def test_course_detail_view_valid(self):
        """Test course detail view for a valid course ID."""
        response = self.client.get(reverse('catalog:course_detail', args=[101]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DTI412")
        self.assertContains(response, "Special Topic in Application Development")
        self.assertContains(response, "Dr. Sirisuda Buathongkeow")

    def test_course_detail_view_404(self):
        """Test that non-existent course ID raises 404."""
        response = self.client.get(reverse('catalog:course_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_inquiry_get(self):
        """Test GET request to inquiry page."""
        response = self.client.get(reverse('catalog:inquiry'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Course Inquiry Form")

    def test_inquiry_post_success(self):
        """Test successful POST inquiry submission."""
        payload = {
            'student_name': 'Jane Doe',
            'email': 'student@example.com',
            'course_code': 'DTI412',
            'message': 'Can I take this course as an elective?',
        }
        response = self.client.post(reverse('catalog:inquiry'), data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Inquiry Processed Successfully!")
        self.assertContains(response, "Jane Doe")

    def test_inquiry_post_validation_errors(self):
        """Test validation error messages on empty/invalid POST submission."""
        # Empty submission
        response = self.client.post(reverse('catalog:inquiry'), data={
            'student_name': '',
            'email': '',
            'course_code': '',
            'message': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Student Name is required.")
        self.assertContains(response, "A valid Email address is required.")
        self.assertContains(response, "Inquiry message cannot be empty.")

        # Invalid email (no @)
        response = self.client.post(reverse('catalog:inquiry'), data={
            'student_name': 'John',
            'email': 'invalidemail',
            'course_code': '',
            'message': 'Hello',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A valid Email address is required.")

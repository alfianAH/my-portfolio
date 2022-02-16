from django.test import TestCase

from .models import (
    About,
    ProfessionalSummary,
)

# Create your tests here.
class HomeTestCase(TestCase):
    def setUp(self):
        # Create professional summary
        self.professional_summary = ProfessionalSummary.objects.create(
            title='Welcome and hello,',
            content="I'm Alfian Aldy Hamdani. I'm currently an Informatics college student in Hasanuddin University. I love talking about Games and Machine Learning. I am eager to learn about new technologies."
        )

        # Create about
        self.about = About.objects.create(
            description="Test",
            photo_url='https://google.com',
            resume_url='https://google.com',
        )

    def test_count_professional_sumary_exists(self):
        qs = ProfessionalSummary.objects.all()
        self.assertTrue(qs.exists())

    def test_count_about_exists(self):
        qs = About.objects.all()
        self.assertTrue(qs.exists())

    def test_count_professional_summary(self):
        qs = ProfessionalSummary.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_count_about(self):
        qs = About.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_professional_summary_fields(self):
        qs = ProfessionalSummary.objects.all()[0]
        self.assertEqual(qs.title, 'Welcome and hello,')
        print('Professional Summary')
        print(qs.created)
        print(qs.updated)

    def test_about_fields(self):
        qs = About.objects.all()[0]
        self.assertEqual(qs.description, 'Test')
        print('About')
        print(qs.created)
        print(qs.updated)


from django.test import TestCase
from shop.models import Category
# Create your tests here.

class MyTestCase(TestCase):
    def setUp(self):
        super().setUp()
        print("setUp being called for MyTestCase")

    def test_something(self):
        assert 2 == 2, "2 should be equal to 2"

    def test_category_creation(self):
        test_category = Category.objects.create(title="Test Category", description="Test Category Description")
        assert test_category.title == "Test Category", "BAD NAMING"

    def tearDown(self):
        super().tearDown()
        print("tearDown being called for MyTestCase")


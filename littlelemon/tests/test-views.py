from django.test import TestCase
from .models import Menu
import unittest

class MenuViewTest(TestCase):
    
    Menu.objects.create(title="testTitle",price=4,inventory=0)

    def test_getall(self):
        item = Menu.objects.get(title="testTitle")
        self.assertEqual(item,"testTitle: 4")
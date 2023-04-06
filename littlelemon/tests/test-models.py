from django.test import TestCase
from .models import Menu
import unittest

class MenuTest(TestCase):
    def instance(self):
        item = Menu.objects.create(title = "testTitle",price="testPrice",inventory = "testInventory")
        self.assertEqual(item,"testTitle : testPrice")
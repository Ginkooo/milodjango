from django.urls import resolve
from django.test import TestCase
from foobar.views import list_users, view_user, add_user, edit_user

class UrlTests(TestCase):

    def test_can_resolve_list_users(self):
        found = resolve('/list/')
        self.assertEqual(found.func, list_users)

    def test_can_resolve_view_user(self):
        found = resolve('/view/1')
        self.assertEqual(found.func, view_user)

    def test_can_resolve_add_user(self):
        found = resolve('/add/')
        self.assertEqual(found.func, add_user)

    def test_can_resolve_edit_user(self):
        found = resolve('/edit/1')
        self.assertEqual(found.func, edit_user)

    def test_can_resolve_download_csv(self):
        found = resolve('/list/true/')
        self.assertEqual(found.func, list_users)

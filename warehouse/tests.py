from django.http import HttpRequest 
from django.test import TestCase
from http import HTTPStatus
from warehouse.forms import ProcessReorderForm

# Create your tests here.
class TestProcessReorder(TestCase):
    def test_form_method(self):
        request = HttpRequest()
        request.POST = {
            "process_status": False
        }

        form = ProcessReorderForm(request.POST)
        self.assertTrue(form, request.method == 'POST')

    def test_form_is_valid(self):
        request = HttpRequest()
        request.POST = {
            "process_status": False
        }
        form = ProcessReorderForm(request.POST)
        self.assertFalse(form.is_valid())

    def test_empty_form(self):
        form = ProcessReorderForm()
        self.assertInHTML(
            '<input type="text" name="date" required id="id_date">', str(form)
        )
        self.assertInHTML(
            '<input type="text" name="due_date" required id="id_due_date">', str(form)
        )

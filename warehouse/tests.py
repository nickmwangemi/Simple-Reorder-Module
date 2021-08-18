from django.http import HttpRequest
from django.test import TestCase

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
            '<input type="checkbox" name="process_status" required id="id_process_status" >', str(form)
        )
        self.assertInHTML(
            '<input type="checkbox" name="process_status" required id="id_process_status" >', str(form)
        )

    def test_process_reorder(self):
        request = HttpRequest()
        form = ProcessReorderForm(request.POST)
        form['process_status'] == request.POST.get('process_status')
        self.assertFalse(form.is_valid())

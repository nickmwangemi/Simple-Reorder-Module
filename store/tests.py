from django.test import TestCase

# Create your tests here.
from django.http import HttpRequest
from django.test import TestCase

from store.forms import SellForm


# Create your tests here.
class TestSellProduct(TestCase):
    def test_form_method(self):
        request = HttpRequest()
        request.POST = {
            "process_status": False
        }

        form = SellForm(request.POST)
        self.assertTrue(form, request.method == 'POST')

    def test_form_is_valid(self):
        request = HttpRequest()
        request.POST = {
            "quantity": int('5')
        }
        form = SellForm(request.POST)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = SellForm()
        self.assertInHTML(
            '<input type="number" name="quantity" required id="id_quantity" >', str(form)
        )
        self.assertInHTML(
            '<input type="number" name="quantity" required id="id_quantity" >', str(form)
        )

    def test_process_reorder(self):
        request = HttpRequest()
        form = SellForm(request.POST)
        form['quantity'] == request.POST.get('quantity')
        self.assertFalse(form.is_valid())

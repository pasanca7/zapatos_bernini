from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from shoe.models import Shoe
from order.models import Order, OrderLine
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class OrderAPIViewTests(APITestCase):

    line_list_url = reverse("line-list")
    line_detail_url = reverse("line-detail", args=[1])
    line_detail_url_not_found = reverse("line-detail", args=[100])
    line_create = reverse("line-create")
    line_update = reverse("line-update", args=[1])
    line_update_not_found = reverse("line-update", args=[100])
    order_list_url = reverse("order-list")
    order_detail_url = reverse("order-detail", args=[1])
    order_detail_url_not_found = reverse("order-detail", args=[100])
    order_create = reverse("order-create")

    def setUp(self):
        # Users creation
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)

        self.customer = User.objects.create_user(username='customer', password='customer')
        self.customer_token = Token.objects.create(user=self.customer)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.customer_token.key)

        # Shoes
        self.shoe1 = Shoe.objects.create(
            name="shoe 1",
            size=39,
            stock=5,
            price=10,
            currency="€"
        )

        self.shoe2 = Shoe.objects.create(
            name="shoe 2",
            size=42,
            stock=10,
            price=20,
            currency="€"
        )
        

        # Order
        self.order = Order.objects.create(
            user=self.customer,
            created=timezone.now(),
            status="PENDING",
            currency="€",
            shipping_costs=1.5,
            total_amount=41.5,
        )

        #OrderLines
        OrderLine.objects.create(
            shoe=self.shoe1,
            order=self.order,
            shoe_name="shoe 1",
            quantity=2,
            currency="€",
            total_amount=20
        )

        OrderLine.objects.create(
            shoe=self.shoe2,
            order=self.order,
            shoe_name="shoe 2",
            quantity=1,
            currency="€",
            total_amount=20
        )

        self.no_stock_line = OrderLine.objects.create(
            shoe=self.shoe2,
            order=self.order,
            shoe_name="shoe 2",
            quantity=11,
            currency="€",
            total_amount=20
        )

    def test_get_line_list(self):
        response = self.client.get(self.line_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_get_line_detail(self):
        response = self.client.get(self.line_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["quantity"], 2)

    def test_get_line_detail_not_found(self):
        response = self.client.get(self.line_detail_url_not_found)
        self.assertEqual(response.status_code, 404)

    def test_create_line(self):
        data = {
            "order": None,
		    "shoe": 2,
		    "quantity": 6
        }
        response = self.client.post(self.line_create, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["shoe_name"], "shoe 2")
    
    def test_create_line_bad_request(self):
        data = {}
        response = self.client.post(self.line_create, data, format="json")
        self.assertEqual(response.status_code, 400)
    
    def test_update_line(self):
        data = {
            "order": None,
		    "shoe": 1,
		    "quantity": 1
        }
        response = self.client.put(self.line_update, data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["quantity"], 1)


    def test_update_line_not_found(self):
        data = {}
        response = self.client.put(self.line_update_not_found, data, format="json")
        self.assertEqual(response.status_code, 404)

    def test_update_line_bad_request(self):
        data = {}
        response = self.client.put(self.line_update, data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_get_order_list(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        response = self.client.get(self.order_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_order_list_unauthorized(self):
        response = self.client.get(self.order_list_url)
        self.assertEqual(response.status_code, 401)
    
    def test_get_order_detail(self):
        response = self.client.get(self.order_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["total_amount"], '41.50')

    def test_get_order_detail_not_found(self):
        response = self.client.get(self.order_detail_url_not_found)
        self.assertEqual(response.status_code, 404)

    def test_create_order(self):
        data = {"lines":[1,2]}
        response = self.client.post(self.order_create, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(Order.objects.all()), 2)

    def test_create_order_bad_request(self):
        data = {}
        response = self.client.post(self.order_create, data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_create_order_no_stock(self):
        data = {"lines":[3]}
        response = self.client.post(self.order_create, data, format="json")
        self.assertEqual(response.status_code, 400)



from django.contrib.auth.models import User
from django.urls import reverse
from shoe.models import Shoe
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status

class ShoeAPIViewTests(APITestCase):

    shoe_list_url = reverse('shoe-list')
    shoe_detail_url = reverse('shoe-detail', args=[1])
    shoe_detail_url_not_found = reverse('shoe-detail', args=[100])
    shoe_create_url = reverse('shoe-create')
    shoe_update_url = reverse('shoe-update', args=[1])
    shoe_update_url_not_found = reverse('shoe-update', args=[100])
    shoe_delete_url = reverse('shoe-delete', args=[1])
    shoe_delete_url_not_found = reverse('shoe-delete', args=[100])

    def setUp(self):
        # Users creation
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.customer = User.objects.create_user(username='customer', password='customer')
        self.customer_token = Token.objects.create(user=self.customer)

        # Shoes for examples
        Shoe.objects.create(
            name="shoe 1",
            size=39,
            stock=5,
            price=10,
            currency="€"
        )

        Shoe.objects.create(
            name="shoe 2",
            size=42,
            stock=10,
            price=20,
            currency="€"
        )

    def test_get_shoe_list(self):
        response = self.client.get(self.shoe_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_get_shoe_list_unauthenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.shoe_list_url)
        self.assertEqual(response.status_code, 401)

    def test_get_shoe_detail(self):
        response = self.client.get(self.shoe_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "shoe 1")

    def test_get_shoe_detail_not_found(self):
        response = self.client.get(self.shoe_detail_url_not_found)
        self.assertEqual(response.status_code, 404)

    def test_create_shoe(self):
        data =  {
            "name": "shoe 3",
            "currency": "€",
            "price": "15.00",
            "size": 40,
            "stock": 20
	    }
        response = self.client.post(self.shoe_create_url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], "shoe 3")
        self.assertEqual(len(Shoe.objects.all()), 3)

    def test_create_shoe_bad_request(self):
        data =  {}
        response = self.client.post(self.shoe_create_url, data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create_shoe_unathorized(self):
        data =  {}
        self.client.force_authenticate(user=self.customer, token=self.customer_token)
        response = self.client.post(self.shoe_create_url, data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_update_shoe(self):
        data =  {
            "name": "shoe 1",
            "currency": "€",
            "price": "5.00",
            "size": 39,
            "stock": 20
	    }
        response = self.client.put(self.shoe_update_url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "shoe 1")
        self.assertEqual(response.data["stock"], 20)
        self.assertEqual(len(Shoe.objects.all()), 2)

    def test_update_shoe_unauthorized(self):
        data =  {}
        self.client.force_authenticate(user=self.customer, token=self.customer_token)
        response = self.client.put(self.shoe_update_url, data, format='json')
        self.assertEqual(response.status_code, 401)
    
    def test_update_shoe_not_found(self):
        data =  {}
        response = self.client.put(self.shoe_update_url_not_found, data, format='json')
        self.assertEqual(response.status_code, 404)

    def test_update_shoe_bad_request(self):
        data =  {}
        response = self.client.put(self.shoe_update_url, data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_delete_shoe(self):
        response = self.client.delete(self.shoe_delete_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Shoe.objects.all()), 1)
    
    def test_delete_shoe_not_found(self):
        response = self.client.delete(self.shoe_delete_url_not_found)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(len(Shoe.objects.all()), 2)

    def test_delete_shoe_unauthorized(self):
        self.client.force_authenticate(user=self.customer, token=self.customer_token)
        response = self.client.delete(self.shoe_delete_url)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(len(Shoe.objects.all()), 2)
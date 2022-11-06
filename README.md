# Zapatos Bernini App

Application developed by Pablo de los Santos Carrión

## Requirements

1. [Docker](https://docs.docker.com/install/)
2. [Docker Compose](https://docs.docker.com/compose/install/)

## How to run it?
Run the application with Docker:
```
docker-compose up
```
## Credentials
There are two users to test the app.

- Superuser
    - username: admin
    - password: admin
- Customer
    - username: customer
    - password: testing1234


## Endpoints

It is necesary to add the Authentication header to consume the API. Example:

```
Authorization: Token <token>
JSON body:
{
	"username": "admin",
	"password": "admin"
}
```

### Authentication
- Get authentication token
```
localhost:8000/api-token-auth/ 
```
### Shoe
- Get all shoes [GET]
```
localhost:8000/shoe/all
```
- Get shoe by ID [GET]
```
localhost:8000/shoe/{ID}
```
- Create shoe [POST]
```
localhost:8000/shoe/

JSON body:
{
    "name": "Shoe 1",
    "currency": "€",
    "price": "15.00",
    "size": 40,
    "stock": 20
}
```
- Update shoe [PUT]
```
localhost:8000/shoe/update/{ID}

JSON body:
{
	"id": 2,
	"name": "Red high heels",
	"currency": "€",
	"price": "40.00",
	"size": 38,
	"stock": 2
}
```
- Delete shoe [DELETE]
```
localhost:8000/shoe/delete/{ID}
```

### Order line
- Get all order lines [GET]
```
localhost:8000/order/line/all
```
- Get order line by ID [GET]
```
localhost:8000/order/line/{ID}
```
- Create order line [POST]
```
localhost:8000/order/line/

JSON body:
{
    "order": null,
    "shoe": 2,
    "quantity": 1
}
```
- Update order line [PUT]
```
localhost:8000/order/line/update/{ID}

JSON body:
{
	"order": null,
	"shoe": 2,
	"quantity": 2
}
```
- Delete order line [DELETE]
```
localhost:8000/order/line/delete/{ID}
```

### Order
- Get all orders [GET]
```
localhost:8000/order/all
```
- Get order by ID [GET]
```
localhost:8000/order/{ID}
```
- Create order [POST]
```
localhost:8000/order/

JSON body:
{
	"lines": [1,2]
}
```
# shopify-backend-challenge
Shopify Backend Fall 2022 Challenge.

Created using Django.

Replit link:
https://replit.com/@arthurhohinng/shopify-backend-challenge#

## Instructions
Open the replit link and then open website.

## Endpoints

### Create inventory items
Endpoint: https://shopify-backend-challenge--arthurhohinng.repl.co/inventory/create-item/

### List all inventory items
Endpoint: https://shopify-backend-challenge--arthurhohinng.repl.co/inventory/list/

### Delete an inventory item
Pass an inventory item id into the url
Endpoint: https://shopify-backend-challenge--arthurhohinng.repl.co/inventory/delete-item/<int:pk>/
For example if I want to delete an inventory item with id = 1: https://shopify-backend-challenge--arthurhohinng.repl.co/inventory/delete-item/1/

### Edit an inventory item
Pass an inventory item id into the url
Endpoint: https://shopify-backend-challenge--arthurhohinng.repl.co/inventory/delete-item/<int:pk>/
For example if I want to edit an inventory item with id = 1: https://shopify-backend-challenge--arthurhohinng.repl.co/inventory/delete-item/1/

### Create a warehouse
Endpoint: https://shopify-backend-challenge--arthurhohinng.repl.co/warehouses/create/

### List stock in a warehouse
Pass a warehouse id into the url
Endpoint: https://shopify-backend-challenge--arthurhohinng.repl.co/warehouses/<int:pk>/
For example if I want to see the stock at warehouse with id = 1: https://shopify-backend-challenge--arthurhohinng.repl.co/warehouses/1/

### Assign stock to a warehouse
Endpoint: https://shopify-backend-challenge--arthurhohinng.repl.co/inventory/assign-stock/

This will reduce the unassigned_count of the inventory item by how much stock you assign to the warehouse.



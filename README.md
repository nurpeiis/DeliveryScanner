# DeliveryScanner
## Instructions:
1. To start run following commands:
    - pwd, and then copy the path 'path'
    - export PYTHONPATH = path
    - export DJANGO_SETTINGS_MODULE = DeliveryScanner.settings.dev
2. Admin SuperUser: 
    admin, 1234567del
3. Enter the food that you want to eat in searching tool
## Description of technologies:
1. Front end- bootstrap, photoshop
2. Back end- Django (web framework), SQlite3(database) 
3. Search tool: from django.db.models import Q library was used to filter relevant data by searching through the dish name and restaurant names
## Database and admin page:
1. Table Pricedata stores data scraped from websites
2. localhost:8000/admin enables you to add or delete data from Pricedata
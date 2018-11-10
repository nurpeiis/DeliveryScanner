# DeliveryScanner
## Aim:
Reduce time and cost of delivering food comparing various offers by food delivery companies near your location

## Future Improvement:
- Registering in our platform enables you to automatically register to all delivery services of your choice, so that checking out process will take even lower time
- Have bigger data set which means more delivery service companies and more extensive description for each food item, which will make output of the search tool more relevant
- Use stronger search engine tools, such as implementing N-gram indexing. Potential usage of whoosh library, which can be used to sort by priority que (i.e. higher match higher rank in the output)
## Instructions:
1. To start run following commands:
    - pwd, and then copy the path 'path'
    - export PYTHONPATH = path
    - export DJANGO_SETTINGS_MODULE = DeliveryScanner.settings.dev

3. Enter the food that you want to eat in searching tool
## Description of technologies:
1. Front end- bootstrap, photoshop
2. Back end- Django (web framework), SQlite3(database) 
3. Search tool: from django.db.models import Q library was used to filter relevant data by searching through the dish name and restaurant names
## Database and admin page:
1. Table Pricedata stores data scraped from websites
2. localhost:8000/admin enables you to add or delete data from Pricedata, use following account
3. Admin SuperUser: 
    username: admin
    password: 1234567del
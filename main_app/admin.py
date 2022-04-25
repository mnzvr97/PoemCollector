from django.contrib import admin
from .models import poem, Read, Author

# Register your models here.
admin.site.register(poem)
admin.site.register(Read)
admin.site.register(Author)
from django.contrib import admin
from .models import Course,Student,Book,Borrowing,Mentor

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Borrowing)
admin.site.register(Mentor)
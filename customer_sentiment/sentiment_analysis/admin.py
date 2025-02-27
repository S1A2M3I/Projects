from django.contrib import admin
from .models import CustomerReview

class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'sentiment', 'created_at')
    search_fields = ('text', 'sentiment')

admin.site.register(CustomerReview, CustomerReviewAdmin)

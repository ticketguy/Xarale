from django.contrib import admin
from .models import Feedback, Count, Client

# Admin configuration for the Feedback model
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('category', 'rating', 'created_at')  # Fields to show in the list view
    list_filter = ('category', 'rating')  # Filters for category and rating
    search_fields = ('category',)  # Search by category name
    ordering = ('-rating',)  # Ordering by rating (highest rating first)
    list_per_page = 10  # Show 10 feedback records per page

class CountAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'value')
    readonly_fields = ('icon_class',)  # Make icon_class read-only
    search_fields = ('title',)
    
# Admin configuration for the Client model
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview')  # Show name and logo preview in the list view
    search_fields = ('name',)  # Search by client name
    list_per_page = 10  # Show 10 clients per page

    def logo_preview(self, obj):
        return f'<img src="{obj.logo.url}" width="50" height="50" />'
    logo_preview.allow_tags = True  # Allow HTML to be rendered for logo preview

# Register the models with the admin site
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Count, CountAdmin)
admin.site.register(Client, ClientAdmin)

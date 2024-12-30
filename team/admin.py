from django.contrib import admin
from .models import Staff


admin.site.register(Staff)


list_display = ('id', 'trip_number', 'trip_link')




def trip_link(self, obj):
        if obj.trip_number:
            return "<a href='%s'>Link</a>" % obj.trip_number
        else:
            return ''
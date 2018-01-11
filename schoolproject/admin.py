from django.contrib import admin

from .models import Richting, Leraar, Klas, Contact

admin.site.register(Richting)
admin.site.register(Leraar)
admin.site.register(Klas)
admin.site.register(Contact)


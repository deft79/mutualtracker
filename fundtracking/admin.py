from mutualtracker.fundtracking.models import Fund, Price, Report, Company, Industry, Country
from django.contrib import admin

class FundAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)

class PriceAdmin(admin.ModelAdmin):
    list_display = ('fund', 'date', 'nav',)
    list_filter = ['date', ]
    search_fields = ['fund__code', 'fund__name']

# Add the admin modules
admin.site.register(Fund, FundAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Report)
admin.site.register(Company)
admin.site.register(Industry)
admin.site.register(Country)

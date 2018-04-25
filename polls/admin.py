from django.contrib import admin
from .models import DolotoDiametr, DiametrYBT, historyСalc, DolotoWithYBT, CasingDiametr, CasingWithYBT, BoringDiametr, BoringWithCasing, engine
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class Adminka(ImportExportModelAdmin):
	pass

admin.site.register(historyСalc, Adminka)		
admin.site.register(DolotoDiametr, Adminka)
admin.site.register(DiametrYBT, Adminka)
admin.site.register(DolotoWithYBT, Adminka)
admin.site.register(CasingDiametr, Adminka)
admin.site.register(CasingWithYBT, Adminka)
admin.site.register(BoringDiametr, Adminka)
admin.site.register(BoringWithCasing, Adminka)
admin.site.register(engine, Adminka)
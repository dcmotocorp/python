from django.contrib import admin
from .models import Account, Branch, Loan, User, Bank, Runner
admin.site.register(Bank)
admin.site.register(Branch)
admin.site.register(Account)
admin.site.register(Loan)
admin.site.register(User)
admin.site.register(Runner)

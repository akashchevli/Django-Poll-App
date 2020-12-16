from django.contrib import admin
from user_poll.models import Questions, Answers, Voting
# Register your models here.


admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Voting)
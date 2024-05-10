from django.contrib import admin
from .models import Poll, UserVote

# Register your models here.
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'option_one', 'option_two', 'option_three')
    list_filter = ('question',)

admin.site.register(UserVote)
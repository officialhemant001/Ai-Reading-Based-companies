from django.contrib import admin
from .models import (
    UserProfile,
    Document,
    Note,
    Learning,
    AIResult,
    DashboardStats,
    ChatHistory
)

admin.site.register(UserProfile)
admin.site.register(Document)
admin.site.register(Note)
admin.site.register(Learning)
admin.site.register(AIResult)
admin.site.register(DashboardStats)
admin.site.register(ChatHistory)
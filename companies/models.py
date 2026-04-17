from django.db import models
from django.contrib.auth.models import User


# ================= USER PROFILE =================
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# ================= DOCUMENT =================
class Document(models.Model):
    INPUT_TYPES = [
        ('pdf', 'PDF'),
        ('text', 'Text'),
        ('url', 'URL'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    input_type = models.CharField(max_length=10, choices=INPUT_TYPES)

    file_name = models.CharField(max_length=255, blank=True)
    file_size = models.IntegerField(default=0)
    language = models.CharField(max_length=50, default="english")
    page_count = models.IntegerField(default=0)

    uploaded_at = models.DateTimeField(auto_now_add=True)


# ================= AI RESULT =================
class AIResult(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE)

    summary = models.TextField()
    keywords = models.TextField()
    simplified_text = models.TextField(blank=True)
    explanation = models.TextField(blank=True)

    difficulty_level = models.CharField(max_length=50, default="medium")
    sentiment = models.CharField(max_length=50, blank=True)
    key_questions = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


# ================= NOTE =================
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    content = models.TextField()
    highlighted_text = models.TextField(blank=True)
    page_number = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)


# ================= LEARNING =================
class Learning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)

    total_documents = models.IntegerField(default=0)
    total_read_time = models.IntegerField(default=0)
    understanding_score = models.IntegerField(default=0)

    last_read = models.DateTimeField(auto_now=True)


# ================= DASHBOARD STATS =================
class DashboardStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    total_docs = models.IntegerField(default=0)
    total_summaries = models.IntegerField(default=0)
    total_notes = models.IntegerField(default=0)
    avg_reading_time = models.IntegerField(default=0)


# ================= CHAT HISTORY =================
class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True)

    message = models.TextField()
    response = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
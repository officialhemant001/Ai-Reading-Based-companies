from django.shortcuts import render,redirect
def dashboard(request):
    return render(request, 'dashboard.html')
def login(request):
    if request.method == "POST":
        return redirect('dashboard')
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')
def image_capture(request):
    return render(request, 'image_capture.html')
def learning(request):
    return render(request, 'learning.html')
def notes(request):
    return render(request, 'notes.html')
def summarization(request):
    return render(request, 'summarization.html')
def text_input(request):
    return render(request, 'text_input.html')
def text_processing(request):
    return render(request, 'text_processing.html')

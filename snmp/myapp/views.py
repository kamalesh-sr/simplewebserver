from django.http import HttpResponse
from pathlib import Path

def home(request):
    file_path = Path(__file__).parent / 'static' / 'sam.html'
    return HttpResponse(file_path.read_text(encoding='utf-8'))
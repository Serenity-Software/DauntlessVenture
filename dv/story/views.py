"""
Views for story.
"""
from django.shortcuts import render


def index(request):
    """Story list."""
    return render(request, 'story/index.html', {})

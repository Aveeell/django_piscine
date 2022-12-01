from django.shortcuts import render, redirect
from .form import TextForm
from django.conf import settings
import logging

def index(request):
    logging.basicConfig(filename=settings.HISTORY_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')
    logger = logging.getLogger('text')
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data['text'])
        return redirect('/ex02')
    try:
        file = open(settings.HISTORY_FILE)
        history = [line for line in file.readlines()]
    except:
        history = []
    return render(request, 'ex02/index.html', {'form': TextForm(), 'history': history})


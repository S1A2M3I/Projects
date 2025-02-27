from django.shortcuts import render
from .models import CustomerReview
from .forms import ReviewForm
from .classifier import analyze_sentiment

def home(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            sentiment = analyze_sentiment(text)
            CustomerReview.objects.create(text=text, sentiment=sentiment)
            return render(request, 'result.html', {'text': text, 'sentiment': sentiment})
    else:
        form = ReviewForm()
    
    return render(request, 'index.html', {'form': form})

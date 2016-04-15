import datetime
from .models import Article

def helper_get_random_article():
    return Article.objects.exclude(
        publication_date__gt=datetime.date.today()
    ).order_by(
        '?'
    ).first()

from datetime import datetime, timedelta


def get_timestamp(date):
    now = datetime.now()
    diff = now - date

    if diff < timedelta(seconds=60):
        return "just now"
    elif diff < timedelta(minutes=2):
        return "1 minute ago"
    elif diff < timedelta(hours=1):
        return f"{diff.seconds // 60} minutes ago"
    elif diff < timedelta(hours=2):
        return "1 hour ago"
    elif diff < timedelta(days=1):
        return f"{diff.seconds // 3600} hours ago"
    elif diff < timedelta(days=2):
        return "yesterday"
    elif diff < timedelta(days=7):
        return f"{diff.days} days ago"
    elif diff < timedelta(days=14):
        return "1 week ago"
    elif diff < timedelta(days=30):
        return f"{diff.days // 7} weeks ago"
    elif diff < timedelta(days=60):
        return "1 month ago"
    elif diff < timedelta(days=365):
        return f"{diff.days // 30} months ago"
    else:
        return f"{diff.days // 365} years ago"

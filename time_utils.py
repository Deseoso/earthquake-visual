from datetime import datetime, timedelta


def get_time():
    current_time = datetime.utcnow()
    day_ago = current_time - timedelta(hours=24)

    return {
        'current_time': current_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'day_ago': day_ago.strftime("%Y-%m-%dT%H:%M:%S")
    }
import json
import random
from datetime import datetime, timedelta, timezone

FILE_NAME = "events.json"
TARGET_SIZE = 1 * 1024 * 1024  # 1 MB

event_types = [
    "login_failed",
    "login_success",
    "file_access",
    "process_started",
    "connection_attempt",
    "account_locked"
]

usernames = [
    "admin",
    "john",
    "ahmed",
    "bob",
    "guest"
]

sources = [
    "windows",
    "linux",
    "firewall",
    "server"
]

events = []

start_time = datetime.now(timezone.utc)
current_time = start_time

while True:

    # أحيانًا ننشئ مجموعة محاولات تسجيل دخول مشبوهة
    if random.random() < 0.05:

        attack_users = random.sample(usernames, k=random.randint(2, 5))

        for username in attack_users:

            current_time += timedelta(
                milliseconds=random.randint(100, 900)
            )

            event = {
                "timestamp": current_time.strftime(
                    "%Y-%m-%dT%H:%M:%S.%f"
                )[:-3] + "+0000",

                "event_type": "login_failed",
                "username": username,
                "ip": f"192.168.1.{random.randint(1, 254)}",
                "severity": random.randint(5, 10),
                "source": random.choice(sources)
            }

            events.append(event)

    else:

        # حدث طبيعي
        current_time += timedelta(
            seconds=random.randint(1, 10)
        )

        event = {
            "timestamp": current_time.strftime(
                "%Y-%m-%dT%H:%M:%S.%f"
            )[:-3] + "+0000",

            "event_type": random.choice(event_types),
            "username": random.choice(usernames),
            "ip": f"192.168.1.{random.randint(1, 254)}",
            "severity": random.randint(1, 10),
            "source": random.choice(sources)
        }

        events.append(event)

    data = json.dumps(
        events,
        ensure_ascii=False,
        indent=2
    )

    if len(data.encode("utf-8")) >= TARGET_SIZE:
        break


with open(FILE_NAME, "w", encoding="utf-8") as file:
    file.write(data)

file_size = len(data.encode("utf-8"))

print("تم إنشاء الملف بنجاح.")
print(f"اسم الملف: {FILE_NAME}")
print(f"عدد الأحداث: {len(events)}")
print(f"الحجم: {file_size / (1024 * 1024):.2f} MB")
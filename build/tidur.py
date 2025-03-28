from datetime import datetime, timedelta


def hitung_waktu_tidur(jam_bangun, menit_bangun):
    waktu_bangun = datetime.strptime(f"{jam_bangun}:{menit_bangun}", "%H:%M")

    hasil_tidur = [
        {"jam": 0, "durasi": 4.5, "siklus": 3},
        {"jam": 0, "durasi": 6, "siklus": 4},
        {"jam": 0, "durasi": 7.5, "siklus": 5},
        {"jam": 0, "durasi": 9, "siklus": 6},
    ]

    for siklus in range(3, 7):
        durasi = siklus * 1.5
        waktu_tidur = waktu_bangun - timedelta(hours=durasi)

        waktu_tidur -= timedelta(minutes=0)

        hasil_tidur[siklus - 3]["jam"] = waktu_tidur.strftime("%H:%M")

    return hasil_tidur

from mutagen.mp3 import MP3
from mutagen.id3 import ID3

track_name = "Витя АК | Читали нажимав на запись"
audio = MP3(f"./music/{track_name}.mp3")
print(f"Заявленный битрейт: {audio.info.bitrate} бит/с")
print(f"Частота дискретизации: {audio.info.sample_rate} Гц")
print(f"Длительность: {audio.info.length} сек")
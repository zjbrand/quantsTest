import tkinter as tk
import time
import threading

# 歌词和时间戳（秒）
lyrics = [
    (9.0, "Brothers, let us come together"),
    (16.0, "Walking in the Spirit, there's much to be done..."),
    (23.0, "We will come reaching, out from our comforts"),
    (33.0, "And they will know us by our love..."),
    (41.0, "Sisters, we were made for kindness"),
    (44.0, "We can pierce the darkness as He shines through us..."),
    (53.0, "We will come reaching, with a song of healing..."),
    (63.0, "And they will know us by our love!"),
    (68.5, "The time is now"),
    (72.0, "Come Church Arise"),
    (76.0, "Love with His hands"),
    (80.0, "See with His eyes"),
    (82.5, "Bind it around you"),
    (87.0, "Let it never leave you"),
    (92.0, "And they will know us by our love"),
    (109.0, "Children, You are hope for justice,"),
    (116.0, "Stand firm in the Truth now, set your hearts above"),
    (123.0, "You will be reaching, long after we’re gone,"),
    (135.0, "And they will know you by your love!"),
    (140.0, "The time is now"),
    (144.0, "Come Church Arise"),
    (147.0, "Love with His hands"),
    (150.5, "See with His eyes"),
    (154.5, "Bind it around you"),
    (158.0, "Let it never leave you"),
    (163.5, "And they will know us by our love"),
    (168.5, "The time is now"),
    (173.0, "Come Church Arise"),
    (177.0, "Love with His hands"),
    (180.0, "See with His eyes"),
    (184.5, "Bind it around you"),
    (188.0, "Let it never leave you"),
    (192.5, "And they will know us by our love")
]

class LyricsPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("By Our Love - 歌词播放器")
        self.master.geometry("700x300")
        self.label = tk.Label(master, text="点击播放开始同步歌词", font=("Helvetica", 18), wraplength=680, justify="center")
        self.label.pack(pady=50)
        self.button = tk.Button(master, text="播放歌词", command=self.start_playback, font=("Helvetica", 14))
        self.button.pack()

    def start_playback(self):
        self.button.config(state=tk.DISABLED)
        threading.Thread(target=self.play_lyrics, daemon=True).start()

    def play_lyrics(self):
        start_time = time.time()
        for timestamp, line in lyrics:
            now = time.time()
            sleep_time = timestamp - (now - start_time)
            if sleep_time > 0:
                time.sleep(sleep_time)
            self.update_lyric(line)

    def update_lyric(self, text):
        self.label.config(text=text)

if __name__ == '__main__':
    root = tk.Tk()
    app = LyricsPlayer(root)
    root.mainloop()

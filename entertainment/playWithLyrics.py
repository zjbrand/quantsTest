import tkinter as tk
import time
import threading
import pygame

def load_lyrics(filename):
    """
    从文本文件中读取歌词，每行作为一句歌词，并返回歌词列表（去除空白行）。
    """
    with open(filename, "r", encoding="utf-8") as f:
        # 逐行读取且剔除空行和首尾空白
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines

# 预设每句歌词对应的时间戳（单位：秒）
# 请确保该列表与歌词文件中的行数对应
timings = [
    9.0, 16.0, 23.0, 33.0, 41.0, 44.0, 53.0, 63.0,
    68.5, 72.0, 76.0, 80.0, 82.5, 87.0, 92.0, 109.0,
    116.0, 123.0, 135.0, 140.0, 144.0, 147.0, 150.5, 154.5,
    158.0, 163.5, 168.5, 173.0, 177.0, 180.0, 184.5, 188.0,
    192.5
]

# 读取歌词文件
lyrics_file = "C:/PopMusic/新建文件夹 4/Christy Nockels - By Our Love.txt"
lyrics_lines = load_lyrics(lyrics_file)

# 检查歌词行数是否和时间戳对应
if len(lyrics_lines) != len(timings):
    print("警告：歌词行数({})与预设时间戳数量({})不匹配！".format(len(lyrics_lines), len(timings)))
    # 这里取二者较小的数以防止越界，你也可以选择退出程序
    min_count = min(len(lyrics_lines), len(timings))
    timings = timings[:min_count]
    lyrics_lines = lyrics_lines[:min_count]

# 合并为 (时间戳, 歌词) 对
lyrics = list(zip(timings, lyrics_lines))

class LyricsPlayer:
    def __init__(self, master, audio_file):
        self.master = master
        self.master.title("By Our Love - 歌词播放器")
        self.master.geometry("700x300")
        self.label = tk.Label(master, text="点击播放开始同步歌词", font=("Helvetica", 18), wraplength=680, justify="center")
        self.label.pack(pady=50)
        self.button = tk.Button(master, text="播放歌词", command=self.start_playback, font=("Helvetica", 14))
        self.button.pack()
        self.audio_file = audio_file

        # 初始化 pygame 的音频播放
        pygame.mixer.init()
        pygame.mixer.music.load(self.audio_file)

    def start_playback(self):
        # 禁用播放按钮，防止多次点击
        self.button.config(state=tk.DISABLED)
        # 同时启动音乐播放和歌词同步线程
        pygame.mixer.music.play()
        threading.Thread(target=self.play_lyrics, daemon=True).start()

    def play_lyrics(self):
        start_time = time.time()
        for timestamp, line in lyrics:
            # 计算到显示当前歌词需要等待的时长
            now = time.time()
            sleep_time = timestamp - (now - start_time)
            if sleep_time > 0:
                time.sleep(sleep_time)
            # 更新歌词显示（Tkinter 的 widget 可直接在此线程更新，但也可以使用 after 回调保证线程安全）
            self.update_lyric(line)

    def update_lyric(self, text):
        # 使用 Tkinter 的 .config 更新显示文字
        self.label.config(text=text)

if __name__ == '__main__':
    root = tk.Tk()
    # 指定音频文件路径，请确保文件存在于指定路径中
    audio_path = "C:/PopMusic/新建文件夹 4/Christy Nockels - By Our Love_SQ.mp3"
    app = LyricsPlayer(root, audio_path)
    root.mainloop()

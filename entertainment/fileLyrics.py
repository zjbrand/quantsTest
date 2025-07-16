import tkinter as tk
import time
import threading
import ast

def load_lyrics_file(filename):
    """
    读取歌词文件，每一行为 (timestamp, "lyric") 格式，
    使用 ast.literal_eval 将字符串转换为元组，
    并返回所有歌词元组的列表。
    """
    lyrics = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            # 去掉前后空格以及可能存在的末尾逗号
            line = line.strip().rstrip(',')
            if line:
                try:
                    # 安全地将字符串转为元组
                    lyric_tuple = ast.literal_eval(line)
                    lyrics.append(lyric_tuple)
                except Exception as e:
                    print("解析歌词时出错：", line, "错误信息：", e)
    return lyrics

# 歌词文件路径
lyrics_file = "C:/PopMusic/新建文件夹 4/Christy Nockels - By Our Love.txt"
# 从文件中读取歌词，结果格式为 [(9.0, "Brothers, let us come together"), ...]
lyrics = load_lyrics_file(lyrics_file)

class LyricsPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("By Our Love - 歌词播放器")
        self.master.geometry("700x300")
        self.label = tk.Label(master, text="点击播放开始同步歌词", font=("Helvetica", 18),
                              wraplength=680, justify="center")
        self.label.pack(pady=50)
        self.button = tk.Button(master, text="播放歌词", command=self.start_playback,
                                font=("Helvetica", 14))
        self.button.pack()

    def start_playback(self):
        self.button.config(state=tk.DISABLED)
        # 启动一个后台线程同步显示歌词
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

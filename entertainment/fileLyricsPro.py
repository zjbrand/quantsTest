import tkinter as tk
import time
import threading
import ast
import bisect


def load_lyrics_file(filename):
    """
    读取歌词文件，每一行应该为
    (时间戳, "歌词")
    格式，使用 ast.literal_eval 将字符串转换为元组，
    并返回所有歌词元组的列表。
    """
    lyrics = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            # 去除首尾空白和末尾可能的逗号
            line = line.strip().rstrip(',')
            if line:
                try:
                    lyric_tuple = ast.literal_eval(line)
                    lyrics.append(lyric_tuple)
                except Exception as e:
                    print("解析歌词时出错：", line, "错误信息：", e)
    return lyrics


# 歌词文件路径
lyrics_file = "C:/PopMusic/新建文件夹 4/Christy Nockels - By Our Love.txt"
# 调用函数读取歌词列表，每个元素为 (时间戳, 歌词) 的形式
lyrics = load_lyrics_file(lyrics_file)


class LyricsPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("By Our Love - 歌词播放器")
        self.master.geometry("700x300")

        # 用来调整播放进度的偏移量（单位：秒）
        self.offset = 0

        self.label = tk.Label(master, text="点击播放开始同步歌词", font=("Helvetica", 18),
                              wraplength=680, justify="center")
        self.label.pack(pady=30)

        # “播放歌词”按钮，点击后开始同步显示歌词
        self.button = tk.Button(master, text="播放歌词", command=self.start_playback,
                                font=("Helvetica", 14))
        self.button.pack(pady=10)

        # 创建一个控制按钮区（放“退后1秒”和“快进1秒”按钮）
        control_frame = tk.Frame(master)
        control_frame.pack(pady=10)

        self.button_backward = tk.Button(control_frame, text="退后1秒", command=self.backward, font=("Helvetica", 14))
        self.button_backward.pack(side=tk.LEFT, padx=20)

        self.button_forward = tk.Button(control_frame, text="快进1秒", command=self.forward, font=("Helvetica", 14))
        self.button_forward.pack(side=tk.RIGHT, padx=20)

    def start_playback(self):
        # 禁用播放按钮，防止重复点击
        self.button.config(state=tk.DISABLED)
        # 启动独立线程执行歌词同步（确保不会阻塞Tkinter主循环）
        threading.Thread(target=self.play_lyrics, daemon=True).start()

    def play_lyrics(self):
        start_time = time.time()
        # 提前提取所有歌词的时间戳列表，用于二分查找
        times = [t for t, _ in lyrics]
        current_index = -1
        while True:
            # 计算有效时间 = 实际经过时间 + offset
            effective_time = time.time() - start_time + self.offset
            # 使用 bisect 查找当前有效时间应对应的歌词索引
            new_index = bisect.bisect_right(times, effective_time) - 1
            if new_index < 0:
                new_index = 0
            # 当索引发生变化时，更新显示的歌词
            if new_index != current_index:
                current_index = new_index
                self.update_lyric(lyrics[current_index][1])
            # 如果已经到了最后一句，并且有效时间超过最后一句3秒以上，则退出循环
            if current_index >= len(lyrics) - 1 and effective_time > times[-1] + 3:
                break
            time.sleep(0.05)

    def update_lyric(self, text):
        self.label.config(text=text)

    def forward(self):
        # 快进1秒：增加 offset
        self.offset += 1
        print("快进1秒, 当前 offset:", self.offset)

    def backward(self):
        # 退后1秒：减少 offset
        self.offset -= 1
        print("退后1秒, 当前 offset:", self.offset)


if __name__ == '__main__':
    root = tk.Tk()
    app = LyricsPlayer(root)
    root.mainloop()

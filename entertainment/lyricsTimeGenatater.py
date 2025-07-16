import tkinter as tk
import pygame
import time
import re
from threading import Thread


# ------------------------------
# 解析 LRC 歌词文件函数
# ------------------------------
def parse_lrc(filename):
    """
    解析LRC文件，返回一个按时间排序的列表，每个元素为 (time_in_sec, lyric) 元组。
    """
    pattern = re.compile(r'\[(\d{2}):(\d{2}(?:\.\d{2})?)\](.*)')
    lyrics = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.match(line)
            if match:
                minutes = int(match.group(1))
                seconds = float(match.group(2))
                time_sec = minutes * 60 + seconds
                text = match.group(3).strip()
                lyrics.append((time_sec, text))
    # 按时间排序
    lyrics.sort(key=lambda x: x[0])
    return lyrics


# ------------------------------
# 卡拉OK显示更新函数
# ------------------------------
class KaraokeApp:
    def __init__(self, master, audio_file, lyrics_file):
        self.master = master
        self.master.title("卡拉OK播放器")
        self.master.geometry("800x400")
        self.audio_file = audio_file

        # 解析歌词
        self.lyrics = parse_lrc(lyrics_file)
        self.current_index = 0

        # 设置文本显示框（使用Text widget便于格式化）
        self.text = tk.Text(master, font=("Helvetica", 24), bg="black", fg="white", bd=0, highlightthickness=0)
        self.text.pack(expand=True, fill="both")
        self.text.configure(state='disabled')

        # 初始化 pygame 音频播放
        pygame.mixer.init()
        pygame.mixer.music.load(self.audio_file)

        # 开始播放音频(异步播放)
        pygame.mixer.music.play()
        self.start_time = time.time()  # 用于计算播放时长

        # 定时更新歌词显示
        self.update_lyrics()

    def update_lyrics(self):
        # 获取当前播放时间（秒）
        # 注意：pygame.mixer.music.get_pos() 返回的是毫秒（从播放开始计时），但可能在暂停/跳转时不完全准确，因此这里同时计算启动时间。
        current_time = (time.time() - self.start_time)

        # 查找当前歌词索引。假设歌词按时间顺序排列，下一个歌词的时间大于当前时间则为当前行
        while self.current_index < len(self.lyrics) - 1 and current_time >= self.lyrics[self.current_index + 1][0]:
            self.current_index += 1

        # 构建显示文本：显示当前行以及前后几行（例如前2行、后2行），当前行高亮
        display_lines = []
        start = max(0, self.current_index - 2)
        end = min(len(self.lyrics), self.current_index + 3)
        for idx in range(start, end):
            time_stamp, line = self.lyrics[idx]
            if idx == self.current_index:
                # 当前行高亮显示：可以使用大写、特殊符号或其它方式标识
                display_lines.append(">> " + line.upper())
            else:
                display_lines.append("   " + line)

        # 更新 Text widget 内容
        self.text.configure(state='normal')
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, "\n".join(display_lines))
        self.text.configure(state='disabled')

        # 每 100 毫秒更新一次
        self.master.after(100, self.update_lyrics)


# ------------------------------
# 独立线程播放pygame（如果需要避免阻塞tkinter）
# ------------------------------
def run_app(audio_file, lyrics_file):
    root = tk.Tk()
    app = KaraokeApp(root, audio_file, lyrics_file)
    root.mainloop()


# ------------------------------
# 主程序入口
# ------------------------------
if __name__ == "__main__":
    # 指定音频文件和歌词文件路径（请根据实际路径修改）
    audio_path = "C:/PopMusic/新建文件夹 4/Christy Nockels - By Our Love_SQ.mp3"
    lyrics_path = "C:/PopMusic/新建文件夹 4/Christy Nockels - By Our Love.txt"

    # 如果需要在独立线程中启动播放，可使用Thread（当前代码直接运行tkinter主循环，不会阻塞pygame播放）
    app_thread = Thread(target=run_app, args=(audio_path, lyrics_path))
    app_thread.start()

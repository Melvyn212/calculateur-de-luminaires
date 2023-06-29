import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("YouTube")

# Create a left frame for the video thumbnails
left_frame = ttk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a right frame for the video player and comments
right_frame = ttk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create a list of video thumbnails in the left frame
for i in range(10):
    video_frame = ttk.Frame(left_frame)
    video_frame.pack(fill=tk.X)
    video_thumbnail = ttk.Label(video_frame, text=f"Video {i+1}")
    video_thumbnail.pack(side=tk.LEFT)
    video_title = ttk.Label(video_frame, text=f"Video Title {i+1}")
    video_title.pack(side=tk.LEFT)

# Create a video player in the right frame
video_player = ttk.Label(right_frame, text="Video Player")
video_player.pack()

# Create a comment section in the right frame
comments = ttk.Label(right_frame, text="Comments")
comments.pack()

root.mainloop()

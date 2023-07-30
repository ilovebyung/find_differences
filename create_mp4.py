import cv2

bg = cv2.imread('bg.jpg')
height, width, _ = bg.shape

output_video = 'output_video.mp4'
fps = 30.0  # Frames per second (adjust this according to your needs)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Video codec (use 'XVID' for AVI)
video_out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

image_files = []
for i in range(10):
    video_out.write(bg)

fg = cv2.imread('fg.jpg')
video_out.write(fg)
video_out.release()

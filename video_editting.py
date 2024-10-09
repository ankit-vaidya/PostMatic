from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, TextClip
import os
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

def split_and_resize_video(video_path : str, chunk_length : int, output_folder : str, overlap : int, tittle : str):
    # Load the video
    video = VideoFileClip(video_path)
    duration = video.duration

    # Calculate the number of chunks
    num_chunks = int(duration // chunk_length) + (1 if duration % chunk_length else 0)

    # Split and resize the video into chunks
    for i in range(num_chunks):
        start_time = i * chunk_length
        if i > 0:
            start_time -= overlap  # Overlap previous chunk by 3 seconds
        end_time = min((i + 1) * chunk_length, duration)
        
        chunk = video.subclip(start_time, end_time)

        # Prepare the chunk file path
        chunk_filename = os.path.join(output_folder, f"chunk_{i + 1}.mp4")

        # Check for last chunk
        if chunk.duration <= overlap : break

        # Resize the video to fit 1080x1920 (9:16 aspect ratio)
        resize_and_save_chunk(chunk, chunk_filename, i + 1, tittle)

    print(f"Video split into {num_chunks} chunks.")
    video.close()

def resize_and_save_chunk(video, output_path, chunk_number, tittle):
    video_w, video_h = video.size
    video_duration = video.duration

    # Set the size for the black background (1920x1080)
    background_width, background_height = 1080, 1920
    background = ColorClip(size=(background_width, background_height), color=(0, 0, 0)).set_duration(video_duration)

    # Resize the video to fit the background width while maintaining aspect ratio
    video_resized = video.resize(height = (background_width / video_w) * video_h)

    # Get the size of the resized video
    video_width, video_height = video_resized.size

    # Calculate the video position (center it horizontally and vertically)
    video_x = (background_width - video_width) // 2
    video_y = (background_height - video_height) // 2 - 50  # Adjust Y to leave space for text

    # Add text below the video
    chunk_text = TextClip(f"Part - {chunk_number}", fontsize=50, color='white', font="Amiri", size=(background_width, 100))
    chunk_text = chunk_text.set_position(('center', video_y + video_height + 160)).set_duration(video_duration)

    title_text = TextClip(tittle, fontsize=80, color='white', font="Amiri-Bold", size=(background_width, 100))
    title_text = title_text.set_position(('center', video_y - video_height + 30)).set_duration(video_duration)

    # Create the final composite video by placing the resized video on top of the background
    final_video = CompositeVideoClip([background, video_resized.set_position((video_x, video_y)), chunk_text, title_text])

    # Export the result in one step
    final_video.write_videofile(output_path)

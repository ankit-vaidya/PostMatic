# from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# def convert_and_add_text(video_path, output_path, text, font_size=50):
#     # Load the video
#     video = VideoFileClip(video_path)
    
    # # Define the target 9:16 resolution (1080x1920 for full HD)
    # target_width = 1080
    # target_height = 1920
    
    # # Resize the video to fit 9:16 aspect ratio
    # video_resized = video.resize(height=target_height)
    
    # # If the width is smaller than target width after resizing, pad the sides
    # if video_resized.w < target_width:
    #     video_resized = video_resized.margin(left=(target_width - video_resized.w) // 2,
    #                                          right=(target_width - video_resized.w) // 2,
    #                                          color=(0, 0, 0))  # Black padding
    
    # # Create a TextClip for adding text to the video
    # text_clip = TextClip(text, fontsize=font_size, color='white', bg_color='black', font="Amiri-Bold")
    
    # # Set the duration of the text to be the same as the video
    # text_clip = text_clip.set_duration(video.duration)
    
    # # Position the text in the center of width and bottom third of the height
    # text_x_position = 'center'  # Horizontally centered
    # text_y_position = int(target_height * 2 / 3)  # Bottom third (y = 2/3 of the height)
    
    # # Apply the text position and resize the text to fit within the video width
    # text_clip = text_clip.set_position((text_x_position, text_y_position)).resize(width=video_resized.w * 0.8)
    
#     # Overlay the text on the video
#     final_video = CompositeVideoClip([video_resized, text_clip])
    
#     # Write the output video file
#     final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

# # Example usage
# convert_and_add_text(r"Input_Video\chunk_1.mp4", r"Video_Chunks", text="Part-1", font_size=70)

# from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip
# from PIL import Image

# # Ensure compatibility with newer Pillow versions
# # if hasattr(Image, 'Resampling'):
# # resampling_filter = Image.Resampling.LANCZOS  # Pillow 9.1.0 and above
# # else:
# #     resampling_filter = Image.ANTIALIAS  # Older versions of Pillow

# # Load the video
# video = VideoFileClip(r"Input_Video\chunk_1.mp4")

# # Set the size for the black background (1920x1080)
# background_width, background_height = 1080, 1920
# background = ColorClip(size=(background_width, background_height), color=(0, 0, 0))

# # Resize the video to fit the background width while maintaining aspect ratio
# # video_resized = video.resize(width=background_width)

# # Calculate video position (center it horizontally and vertically)
# video_x = (background_width - video.w) // 2
# video_y = (background_height - video.h) // 2 - 50  # Adjust the Y position to leave space for text below

# # Add text below the video
# # text = TextClip("Your text here", fontsize=40, color='white', font="Amiri-Bold")
# # text = text.set_position(('center', video_y + video.h + 10)).set_duration(video.duration)

# # Create the final composite video
# final_video = CompositeVideoClip([background, video.set_position((video_x, video_y))])

# # Export the result
# final_video.write_videofile(r"Video_Chunks\output_video.mp4")


# from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip

# # Load the video
# video = VideoFileClip(r"Input_Video\chunk_1.mp4")

# # Set the size for the black background (1920x1080)
# background_width, background_height = 1080, 1920
# background = ColorClip(size=(background_width, background_height), color=(0, 0, 0)).set_duration(video.duration)

# # Get the size of the video
# video_width, video_height = video.size

# # Calculate the video position (center it horizontally and vertically)
# video_x = (background_width - video_width) // 2
# video_y = (background_height - video_height) // 2 - 50  # Adjust Y to leave space for text

# # Add text below the video
# text = TextClip("Your text here", fontsize=40, color='white', font="Amiri-Bold", size=(background_width, 100))
# text = text.set_position(('center', video_y + video_height + 10)).set_duration(video.duration)

# # Create the final composite video by placing the video on top of the background and text below the video
# final_video = CompositeVideoClip([background, video.set_position((video_x, video_y)), text])

# # Export the result
# final_video.write_videofile("output_video.mp4", fps=24)


from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, TextClip
import os
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

# Load the video
video = VideoFileClip(r"Input_Video\chunk_1.mp4")
video_w, video_h = video.size
video_duration = video.duration

# Set the size for the black background (1920x1080)
background_width, background_height = 1080, 1920
background = ColorClip(size=(background_width, background_height), color=(0, 0, 0)).set_duration(video_duration)

# # Resize the video to fit the background width while maintaining aspect ratio
video_resized = video.resize(width=background_width, height=(background_width/video_w)*video_h)

# Get the size of the video
video_width, video_height = video_resized.size

# Calculate the video position (center it horizontally and vertically)
video_x = (background_width - video_width) // 2
video_y = (background_height - video_height) // 2 - 50  # Adjust Y to leave space for text

# Add text below the video
chunk_text = TextClip(f"Part - 1", fontsize=60, color='white', font="Amiri", size=(background_width, 100))
chunk_text = chunk_text.set_position(('center', video_y + video_height + 160)).set_duration(video_duration)

title_text = TextClip(f"Chi va Chisau ka", fontsize=80, color='white', font="Amiri-Bold", size=(background_width, 100))
title_text = title_text.set_position(('center', video_y - video_height + 30)).set_duration(video_duration)

# Create the final composite video by placing the video on top of the background and the text below the video
final_video = CompositeVideoClip([background, video_resized.set_position((video_x, video_y)), chunk_text, title_text])

# Export the result
final_video.write_videofile(r"output_video2.mp4", threads = 32)
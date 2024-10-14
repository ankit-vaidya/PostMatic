from video_editting import split_and_resize_video
from upload_to_insta import get_long_lived_token, upload_video_to_instagram

if __name__ == "__main__":
    split_and_resize_video(video_path = r"Input_Video\chunk_1.mp4",chunk_length = 10,output_folder =  r"Video_Chunks", tittle = "Chi Va Chisauka")
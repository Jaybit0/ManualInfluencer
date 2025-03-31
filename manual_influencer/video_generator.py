import os
import subprocess

import cv2
import ffmpeg
import imageio_ffmpeg


def generate_video(image_folder="data/images", audio_file="./data/synthesis.wav"):
    os.remove("./finished_video.mp4")
    os.remove("./video.avi")
    os.remove("./video.mp4")

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter("./video.avi", 0, 1, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    # cv2.destroyAllWindows()
    video.release()

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run(
        [
            ffmpeg_exe,
            "-y",  # overwrite output if exists
            "-i",
            "video.avi",  # input video
            "-c:v",
            "libx264",  # video codec
            "-c:a",
            "aac",  # audio codec
            "-shortest",  # finish when the shorter stream ends
            "video.mp4",  # output file
        ]
    )

    input_video = ffmpeg.input("./video.mp4")

    input_audio = ffmpeg.input(audio_file)

    ffmpeg.concat(input_video, input_audio, v=1, a=1).output("finished_video.mp4").run(
        cmd=ffmpeg_exe
    )
    os.remove("./video.avi")
    os.remove("./video.mp4")


def concat_videos(video_paths, output_path="concatenated.mp4"):
    # Create the concat input text file
    with open("concat_list.txt", "w") as f:
        for path in video_paths:
            f.write(f"file '{os.path.abspath(path)}'\n")

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

    # Run ffmpeg concat
    subprocess.run(
        [
            ffmpeg_exe,
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            "concat_list.txt",
            "-c",
            "copy",
            output_path,
        ]
    )

    os.remove("concat_list.txt")


# concat_videos(['./test_data/finished_video(3).mp4', './test_data/finished_video(2).mp4'], output_path='./test_data/out.mp4')

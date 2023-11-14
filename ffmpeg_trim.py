# import pip
# pip.main(['install', 'ffmpeg-python'])  needed to use pip to install ffmpeg

import subprocess
import ffmpeg

import pathlib
import os
import datetime

# Define path of txt file with class settings
file_path = r"C:\Users\omark\PycharmProjects\Silence_Trimmer\AudioTrim_Classes.txt"

# Open the text file in read mode
with open(file_path, 'r') as file:
    # Load the data into a Python dictionary and execute code
    data = file.read()
    exec(data)  # pops out a nested_classes variable with all the classes information

n_files = []


def trim_silence(directory, directory_out, course, n_files):
    n = 0
    file_list = []

    # Iterate through input directory and add every file in directory to a list
    for filename in os.listdir(directory):
        files = os.path.join(directory, filename)
        if os.path.isfile(files):
            file_list += [files]

    for input_audio in file_list:
        # Establishing name of file for export
        name_pre = input_audio.split('\\')
        name_split = name_pre[-1].split('.')
        if "_" in name_split[0]:
            rename = name_split[0]
            true_name = rename.split("_")[0]
        else:
            true_name = name_split[0]

        if true_name == "desktop":
            pass
        else:
            n += 1
            genre = []
            language = []
            # Metadata values
            for lang in nested_classes[course]["language"]:
                if lang in true_name:
                    index = nested_classes[course]["language"].index(lang)
                    genre.append(nested_classes[course]["genre"][index])
                    language.append(lang)
            artist = nested_classes[course]["artist"]
            album = nested_classes[course]["album"]
            short_name = nested_classes[course]["short_name"]

            # Get the timestamp of the last modification of input file
            timestamp = os.path.getmtime(input_audio)

            # Convert the timestamp to a readable date and time
            modified_time = datetime.datetime.fromtimestamp(timestamp)

            # Formatted date time to YYYY-MM-DD
            title = modified_time.strftime("%Y-%m-%d") + "_" + language[0]

            output = directory_out
            for item in os.listdir(directory_out):
                path_item = os.path.join(directory_out, item)
                if os.path.isdir(path_item):
                    if language[0] in item:
                        output = path_item
                        break
                    else:
                        pass

            # ffmpeg commands to first filter out silence (-33 dB, min_duration = 3s), add metadata, convert wav to mp3
            ffmpeg_command = [
                'ffmpeg', '-i', input_audio,
                '-af',
                'silenceremove=stop_periods=-1:stop_duration=4:stop_threshold=-40dB:start_periods=1:start_duration=0.07:start_threshold=-40dB',
                '-metadata', f'title={title}',
                '-metadata', f'artist={artist}',
                '-metadata', f'album={album}',
                '-metadata', f'genre={genre[0]}',
                f"{output}\\{short_name}_{language[0]}_{modified_time.strftime('%m-%d-%Y')}.mp3"
            ]
            subprocess.run(ffmpeg_command)

    n_files.append(n)

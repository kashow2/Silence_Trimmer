# Silence_Trimmer
## Program tool to trim the silence from audio files
### Components

- ffmpeg_trim --- performs the silence trimming from audio files.
> Uses a function trim_silence which takes three arguments, the directory input folder, the directory output folder and the course associated with the audio files.

- dashboard --- main script that will execute audio trimming + rendering
> Creates a dashboard to prompt users to select the input folder with all audio files of interest, the output folder to save resulting files and to then trim + render audio!
> Calls upon the trim_silence function in ffmpeg_trim
> Uses tkinter library for the dashboard creation.

- AudioTrim_Classes --- modifiable text file holding metadata information
> Nested dictionary with information associated with the audio files desired to be trimmed.


**IMPORTANT NOTES:**
1. Must download ffmpeg.exe from the web ([Link Text](https://ffmpeg.org/download.html)) and 
   place ffmpeg.exe, ffplay.exe and ffprobe.exe into your working Path.
> [On Windows] Your Path can be found by searching Path in the Windows search bar, navigating to the Advanced tab of system properties and going into Environmental Variables.
2. On both dashboard.py and ffmpeg_trim.py, you need to change the file_path variable to where you've stored the AudioTrim_Classes.txt file! 
> line 11 on dashboard.py & line 12 on ffmpeg_trim.py

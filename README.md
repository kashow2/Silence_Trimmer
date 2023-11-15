# Silence_Trimmer
## Program tool to trim the silence from audio files
### Components

- dashboard --- Main python file creating a dashboard that executes audio trimming + rendering with user input
> Creates a dashboard to prompt users to select the input folder with all audio files of interest, the output folder to save resulting files and to then trim + render audio!
> 
> Calls upon the trim_silence function in ffmpeg_trim
> 
> Uses tkinter library for the dashboard creation.

- ffmpeg_trim --- python file that performs the silence trimming from audio files
> Uses a function trim_silence which takes three arguments, the directory input folder, the directory output folder and the course associated with the audio files.

- AudioTrim_Classes --- modifiable text file holding metadata information
> Nested dictionary with information associated with the audio files desired to be trimmed.

- requirements --- text file with dependencies required for this project

- SilenceTrimmer --- batch file that can be used as an executable shortcut on your desktop.
> edit this file by modifying the file path to where you will have saved the dashboard.py file to

---

**INSTALLATION INSTRUCTIONS:**

**1**. Download this code as a zip file and extract it into a working project folder. **OR** clone the repository using the following command into your terminal.

 ```bash
 git clone https://github.com/kashow2/Silence_Trimmer
 ```

**2**. Create a virtual environment in this working folder and install requirements.txt to install ffmpeg and tk (tkinter) into your venv.

&nbsp;&nbsp;&nbsp;&nbsp; - You can use pip to install these packages. Make sure you're upgraded to the most recent pip version
 
 ```python
 pip install -r requirements.txt
 ```

**3**. Download ffmpeg.exe from the web ([ffmpeg](https://ffmpeg.org/download.html)) and 
   place ffmpeg.exe, ffplay.exe and ffprobe.exe into your working Path.
   
&nbsp;&nbsp;&nbsp;&nbsp; - [*On Windows*] Your Path can be found by searching Path in the Windows search bar, navigating to the Advanced tab of 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system properties and going into Environmental Variables.

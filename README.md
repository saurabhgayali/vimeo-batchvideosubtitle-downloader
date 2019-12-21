# Vimeo batch video subtitle downloader

This project consists of two scripts. They can download all video and subtitles within the folder that contains saved html file for the vimeo video. As the vimeo keeps changing tokes with expiry details, the html downloaded has to be fresh, or error might occur.

## It also works for website that contain embedded private vimeo videos.
Just download the html that contains the embedded videos. The associated folder will contain multiple html files for individual vimeo videos. Place the two scripts inside that folder and run it.

### The current version download 720p only.
Setting 1080p causes 404 for several files.

#Requirments
1. Python
2. Python library: requests
3. wget [With path entry]

# Discord Chat Simulator

## Info

*This README file will be updated with a demo video tomorrow :)*

This repository contains code that simulates and produces a fake discord conversation between multiple people. It takes in a text file of the form :-

```
AutoGPT:
#!@everyone$^1
I WILL TAKE OVER THE PLANET$^1.5
I WILL DESTORY HUMANITY$^1.5

Billy:
who asked?$^1.3
lol$^1

# this line is ignore becaused it starts with hashtag (#) sign
Doge:
true lol$^1.2
```

and produces a full video of the chat, like those found in Beluga or Mr. P Solver videos. Messages from the same person stack: for example, in the chat above, the sequence of messages produced by the first chats of `AutoGPT` are `“I WILL TAKE OVER THE PLANET”` and then `“I WILL TAKE OVER THE PLANET (newline) I WILL DESTORY HUMANITY”`

***I know it must seem overwhelming at first sight, but it really isn't.***

## About the chat file

1. Lines starting with `#` are ignored (like comments)

***Did you know, you can even take screenshots of discord messages (which contain pings, as this script does not support that \*currently\*) and put them in the video too?***

***But you need to rename those images properly, (for example, if you are taking a picture of the 5th message, the file should be 005.png)***

2. Lines starting with `#!` mean - You took a picture of message/anything from discord and the code should not generate image for that message.

3. There should be `$^` followed by a number after every message (including which start with `#!`) to express the number of seconds each message should be shown in the video.

##  Usage

- **The only prerequisites are [Python](https://www.python.org) and [FFmpeg](https://ffmpeg.org), which should be installed in order to run this script.**

- **First download the repository and follow the steps given below.**

1. `pip install -r requirements.txt`

2. Add all desired profile pictures to the `profile_pictures/` folder.

3. Inside the `profile_pictures/` folder, update the `profile_pic_dict.json` with names (corresponding to the names in whatever script txt file you want to convert) and corresponding profile pictures. Also make sure to add their role colours in `role_colors.json` file.

4. Inside the repository folder, run `python generate_chat.py`. It will prompt you to choose a `.txt` file of a script (format outlines above) somewhere on your computer. The images will be saved in a newly created `chat/` folder with the form `007.png` where the numbers represent the image number in the entire sequence.
# Discord Chat Simulator

This repository contains code that produces a fake discord conversation between multiple people. It takes in a text file of the form

```
Jim:
Hey Bob
What kind of chocolate...
Do you find in airports?

Bob:
idk Jim
what kind?

# this line is ignore becaused it has a # sign
Jim:
plain
```

and produces a sequence of discord messages, like those found in Beluga or Mr. P Solver videos. Messages from the same person stack: for example, in the chat above, the sequence of messages produced by the first chats of Jim are "Hey Bob" then "Hey Bob (newline) What kind of chocolate..." and then "Hey Bob (newline) What kind of chocolate... (newline) Do you find in airports?"

To run

1. `pip install -r requirements.txt`
2. Add all desired profile pictures to the `profile_pictures/` folder.
3. Inside the `profile_pictures/` folder, update the `profile_pic_dict.json` with names (corresponding to the names in whatever script txt file you want to convert) and corresponding profile pictures.
4. Inside the repository folder, run `python generate_chat.py`. It will prompt you to choose a `.txt` file of a script (format outlines above) somewhere on your computer. The images will be saved in a newly created `chat/` folder with the form `007T.png` where the first 3 numbers represent the image number in the entire sequence and the letter is the first letter of speakers name. 

The file naming convention for saved `.PNG` chats is used because videos (very likely) have less than 1000 messages and the three digits allows for easy importing and sorting into a software like premiere pro.


### Typewriter
A Python bot that auto-completes most typing challenges from [Typing.com](https://typing.com)

#
#### 1. Configuration in `config.json`
```JSON
{
    "TargetWPM": 100,
    "TargetAccuracy": 95,
    "MistakeReactionTime": 0.3
}
```
 - `TargetWPM`: The bot's target typing speed in Words Per Minute (note that some randomness is applied alongside this strict target)
 - `TargetAccuracy`: The target percentage of letters to type correctly (a `TargetAccuracy` of 90 will result in around 90% accuracy in the challenge)
 - `MistakeReactionTime`: The amount of time (in seconds) before the bot will "realize" it made a mistake and press the Backspace key to correct the letter.

#### 2. Screen Setup
 - Bot is coded to recognize text on a single **1920x1080** display (1080p) with the [typing.com](https://typing.com) zoom level at **100%**.
    - Tested on Microsoft Edge (Linux) at 1080p, 100% scaling.

#### 3. OCR Models
 - Download Tesseract for your respective operating system. Check Tesseract's installation instructions for your operating system for more information.
 - Download the [tesseract-ocr/tessdata](https://github.com/tesseract-ocr/tessdata) repository and extract it to a folder if needed.
 - Set the `TESSDATA_PREFIX` environment variable to the path of the `tessdata` folder.
   - Linux: `export TESSDATA_PREFIX=AbsolutePathToYourTessdataFolder`

#### 4. Running
 - Currently, you have to start the Python script and then switch the focused window to [typing.com](https://typing.com) for the bot to type.
   - Make sure that the entire letter area is unobstructed and clearly visible.
   - The delay before typing starts can be adjusted on Line 27 of `Typewriter.py`.
 - This process will be made easier in future updates.

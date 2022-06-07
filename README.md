<p align="center">
 <img width="100px" src="https://icon-library.com/images/moon-icon-png/moon-icon-png-4.jpg" align="center" alt="Github Readme Stats" />
 <h2 align="center">DeepAI Nudity Detection API Wrapper DEMO</h2>
</p>

# DeepAI-Nudity-Detection
<p>
This python package implements a wrapper class around DeepAI Nudity Detection API. Please be aware that this is not an official API.
It Detects the likelihood that an image contains nudity and should be considered NSFW. Returns a number between 0 and 1, with 1 being 100% likely to contain nudity and be NSFW.
<br>

### It can output:
* NSFW Score
* Confidence Value
* Detected Parts
* Bounding Boxes Position (where is the part shown)
</p>

## Installation
Sadly, I'm lazy enough to package the module and upload it to Pypi,
So you need to put the file in your packages file or in your project file specifically.<br>
#### Getting the file
```
wget https://raw.githubusercontent.com/MoleTheDev/DeepAI-Nudity-Detection/main/nsfw_detection.py
```
Running this command in terminal will download the file in the directory you are in.

## Documention
There's no documention yet. lol, since the module has 1 use only.

## Usage
-> (assuming you already downloaded the module file in your project directory, or your packages directory)
### Using Image local file
<img src="image.jpg"><br>
*A-Ahem..* you can try more lewd stuff

```py
from nsfw_detection import detect

api_key = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"

# detect(api_key, img, link, output)
result = detect(api_key, "image.jpg", False, True)

print(result)
```
#### Output
```javascript
{
'id': '10aa0275-10f5-4330-8f5c-05d97c90bdd8',
'output': 
   {
    'detections': [], 
    'nsfw_score': 0.4273429811000824
   }
}

```
### Using Image URL
```py
from nsfw_detection import detect

api_key = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"

img_url = "https://raw.githubusercontent.com/MoleTheDev/DeepAI-Nudity-Detection/main/image.jpg"

# detect(api_key, img, link, output)
result = detect(api_key, False, img_url, True)

print(result)
```
It would be the same output, *sooo* i don't have to put the output again.

### DISCORD:
**MOLE#2165**

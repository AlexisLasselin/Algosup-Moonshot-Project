# ALGOSUP Moonshot Project

## Context and Problematic

There are over 70 million deaf people in the world.
Although there are 121 sign languages, these are rarely learned by the people concerned, and even less by people without this disability.
When we ask the people concerned why, it's for two main reasons:

- A lack of education about it
- A lack of usefulness, because few people can understand them.

## My solution

Although I can't help people learn sign language, I want to help people who can speak it by enabling them to communicate with as many people as possible.

How can I do this? My idea is to design an application that translates sign language into a natural language, like Google Translate.
I know that there's a company called SignAll, that has partially implemented my project. But this company works more in B2B and requires a certain amount of hardware, whereas my idea would be to make it in the form of a mobile application to democratize this.

My aim for the very first version would be to translate LSF, the French Sign Language,then go the ASL, the American Sign Language as it is the most widely signed in the world with almost half a million signers, into English.

### How does it work?

The idea is to use a camera to film the person signing, then use a neural network to detect the signs and translate them into text.
The neural network will be trained on a dataset of videos of people signing, with the corresponding text as labels.
The neural network will be able to detect the signs in real time and translate them into text, which will then be displayed on the screen.

### Can I try it?

Sure! You can try it by currently downloading the repository and running the file `test.py`.
This will open a window with the camera and you can start signing in front of it. The application will then detect the letter you are signing and display it on the screen.
The application is currently trained on the French Sign Language alphabet, but I plan to train it on the whole LSF.

### How to use it?

1. Clone the repository
2. Install the requirements
3. Run the file `test.py` to test the application

#### Requirements

- Python 3.11
- OpenCV
- TensorFlow
- NumPy
- Mediapipe

> [!NOTE]
> The software has been tested only on Ubuntu 24.04 but it should work on Windows and MacOS too.

#### What are the other files?

- **test.py**: The main file that runs the sign language detection.
- **data_collection.py**: The main file that allows you to generate images from the webcam for the training.
- **main.py**: An outdated file that was used to detect the various parts of the body that are needed to detect the signs.

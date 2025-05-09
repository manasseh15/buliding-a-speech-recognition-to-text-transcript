Noise Robust Speech-to-Text System

Overview

This project focuses on building a basic speech-to-text (STT) system that works reliably in noisy environments using Python and Google's Speech Recognition API. It calibrates the microphone to account for ambient background noise and transcribes live speech input through a microphone.

This project satisfies the requirements of Unit 1 - NMU, covering real-world use cases like customer support automation, lecture transcription, and accessibility tools.

Features

Microphone input with real-time listening
Ambient noise adjustment for better accuracy
Measures and displays speech duration
Transcribes speech using Google’s Speech Recognition API
Saves raw transcript to a file
Requirements

Python 3.x
speechrecognition
pyaudio
Installation

Make sure Python and pip are installed, then run:

pip install -r requirements.txt
You may also need:

pip install pipwin
pipwin install pyaudio
Usage

To run the program:

python main/project1_noise_robust_stt.py
The script will:

Adjust to your environment’s background noise
Prompt you to speak
Transcribe your voice into text
Save the transcript into output/transcript_log.txt
Output

Transcription results are saved in the /output/ folder as plain text files. You can also view the printed transcription directly in the console.
Screenshots of terminal output can be added to the output/ folder.
Example

Calibrating microphone for ambient noise...
Ready. Start speaking.
Speech duration: 3.42 seconds
Transcript: The weather in Mumbai is sunny today
✅ Transcript saved to output/transcript_log.txt

author:
manasseh v
Be.cse
k.s.k college of engineering and technology

# **Context**

- [**Context**](#context)
- [**Day 12 - Building an Iron Man JARVIS System**](#day-12---building-an-iron-man-jarvis-system)
  - [**Features in JARVIS System**](#features-in-jarvis-system)
  - [**JARVIS System Setup**](#jarvis-system-setup)
- [**Day 13 - Multilingual AI Assistant**](#day-13---multilingual-ai-assistant)
  - [**Extending Jarvis Chatbot**](#extending-jarvis-chatbot)
- [**Day 28 - Jarvis Using Arduino**](#day-28---jarvis-using-arduino)
  - [**JARVIS Smart Home Controller**](#jarvis-smart-home-controller)
  - [**Smart Home Features**](#smart-home-features)
  - [**Arduino Jarvis System Diagram**](#arduino-jarvis-system-diagram)
  - [**JARVIS Smart Home Setup and Usage**](#jarvis-smart-home-setup-and-usage)
  - [**How to Run JARVIS Smart Home**](#how-to-run-jarvis-smart-home)

# [**Day 12 - Building an Iron Man JARVIS System**](./Day%2012%20-%20Building%20an%20Iron%20Man%20JARVIS%20System/)

- JARVIS is a Python-based voice assistant that can interact with the user through speech recognition, perform tasks like opening applications, searching on Google or Wikipedia, playing music randomly, telling jokes, and having small talk.

- This project uses speech recognition and text-to-speech (TTS) to provide a hands-free assistant experience similar to Iron Man's JARVIS.

[⬆️ Go to Context](#context)

## **Features in JARVIS System**

- Greet the user according to the time of day (morning, afternoon, evening)
- Recognize voice commands using Google Speech Recognition
- Speak responses using pyttsx3
- Time & Date announcements
- Wikipedia search with spoken summary
- Open websites like Google, Facebook, YouTube
- Play random music from a specified folder
- Open system applications: Calculator, Notepad, CMD
- Open Calendar (Google Calendar via browser)
- Tell jokes and respond to basic small talk
- Exit gracefully with a voice command

[⬆️ Go to Context](#context)

## **JARVIS System Setup**

- Python `3.13` or higher
- Packages

  ```sh
  PyAudio==0.2.14
  pyttsx3==2.99
  SpeechRecognition==3.14.4
  wikipedia==1.4.0
  ```

- Create [virtual env](../Module%2010%20-%20Virtual%20Environment%20&%20Requirements/) then install package and run [jarvis.py](./Day%2012%20-%20Building%20an%20Iron%20Man%20JARVIS%20System/jarvis.py)

[⬆️ Go to Context](#context)

# [**Day 13 - Multilingual AI Assistant**](./Day%2013%20-%20Multilingual%20AI%20Assistant/)

## **Extending Jarvis Chatbot**

- Add new requirement `google-generativeai` to use gemini flash model `gemini-2.5-flash`
- And `python-dotenv` for loading secrete variable from `.env` like API key

  ```sh
  PyAudio==0.2.14
  pyttsx3==2.99
  SpeechRecognition==3.14.4
  wikipedia==1.4.0
  google-generativeai==0.8.5
  python-dotenv==1.2.1
  ```

- Get Free API from [Google AI Studio](https://aistudio.google.com/api-keys)
- Apply it in [jarvis.py](./Day%2013%20-%20Multilingual%20AI%20Assistant/jarvis.py)
- Use it for others query from user
- Run [jarvis.py](./Day%2013%20-%20Multilingual%20AI%20Assistant/jarvis.py)

[⬆️ Go to Context](#context)

# [**Day 28 - Jarvis Using Arduino**](./Day%2028%20-%20Jarvis%20Using%20Arduino/)

## **JARVIS Smart Home Controller**

- A simple **voice-controlled smart home system** using **Python + Arduino (Serial Communication)**.
The system allows you to control lights, fan, and TV using voice commands processed in Python and sent to Arduino via serial.

[⬆️ Go to Conext](#context)

## **Smart Home Features**

- Bedroom light ON / OFF
- Table lamp ON / OFF
- Fan ON / OFF
- TV ON / OFF
- Turn **everything ON**
- Turn **everything OFF**
- Real-time serial communication
- Easy to extend (add more devices or commands)

[⬆️ Go to Context](#context)

## **Arduino Jarvis System Diagram**

  ```mermaid
  flowchart LR
      A[User Voice Command] --> B[Microphone]

      B --> C[Python Voice Recognition]
      C --> D[Command Processing Logic]

      D -->|Single Character Command| E[Serial Communication]

      E --> F[Arduino Controller]

      F --> G[Bedroom Light]
      F --> H[Table Lamp]
      F --> I[Fan]
      F --> J[TV]

      subgraph Python Side
          C
          D
          E
      end

      subgraph Arduino Side
          F
      end

      subgraph Devices
          G
          H
          I
          J
      end
  ```

[⬆️ Go to Context](#context)

## **JARVIS Smart Home Setup and Usage**

- Hardware Requirements
  - Arduino Uno / Nano / Mega
  - Relay Module (4-channel recommended)
  - Lights, Fan, TV (or LEDs for testing)
  - Jumper wires
  - USB cable
- Software Requirements
  - Arduino IDE
  - Python 3.x
  - Python Libraries:
    - `pyserial`
    - `speechrecognition`
    - `pyttsx3`
    - `logging`

- Pin Configuration (Arduino)

  | Device        | Arduino Pin |
  | ------------- | ----------- |
  | Bedroom Light | D2          |
  | Table Lamp    | D3          |
  | Fan           | D4          |
  | TV            | D5          |

- Serial Command Mapping

  | Command | Action              |
  | ------- | ------------------- |
  | `1`     | Bedroom Light ON    |
  | `2`     | Bedroom Light OFF   |
  | `3`     | Table Lamp ON       |
  | `4`     | Table Lamp OFF      |
  | `5`     | Fan ON              |
  | `6`     | Fan OFF             |
  | `7`     | TV ON               |
  | `8`     | TV OFF              |
  | `9`     | Turn ON Everything  |
  | `0`     | Turn OFF Everything |

- Arduino Code
  - Initializes serial communication at **9600 baud**
  - Sets all device pins as `OUTPUT`
  - Listens for serial input
  - Uses `switch-case` to control devices
  - Safe startup (everything OFF)

- Python Voice Command Logic
  - Listens for voice input
  - Matches phrases like:
    - `"turn on fan"`
    - `"turn off tv"`
  - Sends **single-byte commands** to Arduino using `ser.write(b'X')`
  - Uses text-to-speech feedback
  - Logs all user actions

[⬆️ Go to Context](#context)

## **How to Run JARVIS Smart Home**

- Arduino
  - Open Arduino IDE
  - Upload the Arduino sketch
  - Note the COM port

- Python

  ```sh
  pip install pyserial speechrecognition pyttsx3
  python main.py
  ```

- Example Voice Commands
  - "Turn on bedroom light"
  - "Turn off table lamp"
  - "Turn on everything"
  - "Turn off fan"
  - "Turn on TV"

[⬆️ Go to Context](#context)

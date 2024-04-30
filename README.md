


# SIXTH SENSE

![logo](https://github.com/Kishorecoder96/sixth-_sense/blob/main/logo.png)

### ARCHITECTURE:
![Overview Archictecture](https://github.com/Kishorecoder96/sixth-_sense/blob/main/Mobile_app/assets/images/archi.png)
### TECHNOLOGY ARSENAL:
1. Firebase <img width="30" height="20" src="https://img.icons8.com/color/48/firebase.png" alt="firebase"/> - Infrastructure and Security: Provides a reliable and scalable backend with built-in security features for data management and user authentication.
2. React Native <img width="30" height="20" src="https://img.icons8.com/officel/30/react.png" alt="react"/> - App for Caretaker: Cross-platform mobile application framework ensuring a consistent user experience across different devices and operating systems.
3. Pi OS <img width="30" height="20" src="https://img.icons8.com/color/48/raspberry.png" alt="raspberry"/>- Lightweight and Automation: Optimized operating system for Raspberry Pi devices, conserving resources and enabling automation tasks.
4. Gemini  - Personal Companion: Core intelligence system offering environmental awareness, navigation, alerts, and voice messaging for personalized assistance.
5. OpenCV <img width="30" height="20" src="https://img.icons8.com/color/48/opencv.png" alt="opencv"/>- Face Recognition: Utilized for facial recognition functionalities to enhance security and provide personalized assistance.
6. Torch - Speech to Text: Enables voice command interaction through speech-to-text conversion, enhancing accessibility and user experience.
7. OCR <img width="30" height="20" src="https://img.icons8.com/material/24/printed-ocr.png" alt="printed-ocr"/>- Extracting Images: Extracts text from images to improve comprehension and facilitate data processing.
8. Google Maps API <img width="30" height="20" src="https://img.icons8.com/color/48/google-maps-new.png" alt="google-maps-new"/>- Directions API: Integrates reliable navigation information from Google Maps for safe and efficient travel planning.
9. Google Calendar API <img width="30" height="20" src="https://img.icons8.com/color/48/google-calendar--v2.png" alt="google-calendar--v2"/>:provide virtual assistant functionalities, including accessing calendar events and creating notes using speech recognition and text-to-speech.
10. Coral TPU <img width="30" height="20" src="https://img.icons8.com/office/30/coral.png" alt="coral"/>- Accelerated Machine Learning: Integrates Coral TPU for accelerated machine learning tasks, enhancing performance and efficiency.
11. TensorFlow Lite - Lightweight Machine Learning: Utilizes TensorFlow Lite for deploying machine learning models on resource-constrained devices, optimizing performance on edge devices.
12. MediaPipe - MediaPipe is chosen for its real-time hand tracking and gesture recognition capabilities, allowing the device to understand hand movements and translate them into action
13. Google Speech-To-Text <img width="30" height="20" src="https://img.icons8.com/ios-glyphs/30/speech-to-text.png" alt="speech-to-text"/>-  converts speech to text for situations where an internet connection allows real-time processing for greater accuracy and features. 
14. Whisper Speech-To-Text <img width="30" height="20" src="https://img.icons8.com/ios-filled/50/whisper.png" alt="whisper"/> - For offline use, our device employs a built-in speech recognition model for real-time speech-to-text conversion, ensuring functionality without an internet connection
15. pyttsx3 - converts text to speech on your device itself (locally), providing voice feedback without needing an internet connection. 
16. langchain -  acts as a bridge, smoothing communication between the user and Gemini. It refines the questions and requests for optimal understanding by the large language model.
17. Face-Recognition <img width="30" height="20" src="https://img.icons8.com/external-flat-circular-vectorslab/68/external-Face-Recognition-interior-flat-circular-vectorslab.png" alt="external-Face-Recognition-interior-flat-circular-vectorslab"/>- it recognizes faces, helping identify people visually imapired individual meet.
18. pyaudio - it acts as a microphone, capturing spoken words for the device to understand.
19. geopy - it bridges the gap, calculating distances between locations based on their coordinates.
20. easyocr - it empowers the device to "read" text, converting images of characters to digital text.

## MACHINE LEARNING:
### Optical Character Recognition(OCR)

**Introduction:**
The OCR module is specifically designed to assist visually impaired individuals in accessing textual content from images. Leveraging the EasyOCR library, it provides a user-friendly interface for extracting text from various sources, thereby enhancing accessibility and independence for individuals with visual impairments. 

**Implementation:**
The OCR module utilizes the EasyOCR library to process images and extract text. It offers a simplified interface for text extraction, requiring minimal user interaction. By leveraging OpenCV for image processing, the module ensures efficient and accurate recognition of textual content from diverse sources, including printed materials, digital documents, and handwritten notes.

**Benefits for Visually Impaired Individuals:**

1. **Accessible Information:** The OCR module enables visually impaired individuals to access textual information from a wide range of sources, including books, documents, labels, and signs, which may otherwise be inaccessible to them.
2. **Independence:** By providing the ability to extract text independently, the module empowers visually impaired users to access information without relying on sighted assistance, promoting self-reliance and confidence.
3. **Real-Time Feedback:** With its quick and efficient text extraction capabilities, the module offers real-time feedback, allowing users to instantly access and interact with textual content in their environment.
4. **Multilingual Support:** Supporting multiple languages, the module caters to the diverse linguistic needs of visually impaired individuals, facilitating access to information in their preferred language.

**Integration with Sixth Sense:**
The OCR module has been integrated with Sixth Sense to enhance its usability and accessibility for visually impaired users. By leveraging our existing assistive technologies, the module extends its functionality and ensures compatibility with diverse user preferences and needs.

**Voice Command Integration:**
The OCR module features voice command integration, allowing visually impaired users to interact with the system using voice commands. Users can issue commands such as "take a picture" to capture an image using the device's camera. Additionally, they can say "extract text from the image" to initiate text extraction using the OCR module.

### Optical Character Recognition(OCR)

***Introduction:**
The OCR module is specifically designed to assist visually impaired individuals in accessing textual content from images. Leveraging the EasyOCR library, it provides a user-friendly interface for extracting text from various sources, thereby enhancing accessibility and independence for individuals with visual impairments. 

**Implementation:**
The OCR module utilizes the EasyOCR library to process images and extract text. It offers a simplified interface for text extraction, requiring minimal user interaction. By leveraging OpenCV for image processing, the module ensures efficient and accurate recognition of textual content from diverse sources, including printed materials, digital documents, and handwritten notes.

**Benefits for Visually Impaired Individuals:**

1. **Accessible Information:** The OCR module enables visually impaired individuals to access textual information from a wide range of sources, including books, documents, labels, and signs, which may otherwise be inaccessible to them.
2. **Independence:** By providing the ability to extract text independently, the module empowers visually impaired users to access information without relying on sighted assistance, promoting self-reliance and confidence.
3. **Real-Time Feedback:** With its quick and efficient text extraction capabilities, the module offers real-time feedback, allowing users to instantly access and interact with textual content in their environment.
4. **Multilingual Support:** Supporting multiple languages, the module caters to the diverse linguistic needs of visually impaired individuals, facilitating access to information in their preferred language.

**Integration with Sixth Sense:**
The OCR module has been integrated with Sixth Sense to enhance its usability and accessibility for visually impaired users. By leveraging our existing assistive technologies, the module extends its functionality and ensures compatibility with diverse user preferences and needs.

**Voice Command Integration:**
The OCR module features voice command integration, allowing visually impaired users to interact with the system using voice commands. Users can issue commands such as "take a picture" to capture an image using the device's camera. Additionally, they can say "extract text from the image" to initiate text extraction using the OCR module.

### Optical Character Recognition(OCR)

***Introduction*:**
The OCR module is specifically designed to assist visually impaired individuals in accessing textual content from images. Leveraging the EasyOCR library, it provides a user-friendly interface for extracting text from various sources, thereby enhancing accessibility and independence for individuals with visual impairments. 

***Implementation*:**
The OCR module utilizes the EasyOCR library to process images and extract text. It offers a simplified interface for text extraction, requiring minimal user interaction. By leveraging OpenCV for image processing, the module ensures efficient and accurate recognition of textual content from diverse sources, including printed materials, digital documents, and handwritten notes.

***Benefits for Visually Impaired Individuals*:**

1. **Accessible Information:** The OCR module enables visually impaired individuals to access textual information from a wide range of sources, including books, documents, labels, and signs, which may otherwise be inaccessible to them.
2. **Independence:** By providing the ability to extract text independently, the module empowers visually impaired users to access information without relying on sighted assistance, promoting self-reliance and confidence.
3. **Real-Time Feedback:** With its quick and efficient text extraction capabilities, the module offers real-time feedback, allowing users to instantly access and interact with textual content in their environment.
4. **Multilingual Support:** Supporting multiple languages, the module caters to the diverse linguistic needs of visually impaired individuals, facilitating access to information in their preferred language.

***Integration with Sixth Sense*:**
The OCR module has been integrated with Sixth Sense to enhance its usability and accessibility for visually impaired users. By leveraging our existing assistive technologies, the module extends its functionality and ensures compatibility with diverse user preferences and needs.

***Voice Command Integration*:**
The OCR module features voice command integration, allowing visually impaired users to interact with the system using voice commands. Users can issue commands such as "take a picture" to capture an image using the device's camera. Additionally, they can say "extract text from the image" to initiate text extraction using the OCR module.

###  Natural Language Processing(NLP) using Spacy

**Overview**

This code implements a voice-controlled assistant system that utilizes natural language processing (NLP) to interpret user commands and perform various tasks. The system integrates functionalities such as image processing, text extraction, notification sending, message sending, and currency detection. The primary goal of using NLP in this context is to enable intuitive interaction with the assistant by understanding and responding to spoken commands.

**Usage of Natural Language Processing (NLP)**

1. **Command Interpretation**:
    - **Purpose**: NLP is employed to interpret user commands provided through voice input.
    - **Implementation**: The **`spacy`** library is used to process and analyze the input text, allowing the system to identify key elements such as verbs, nouns, and adjectives.
    - **Example**: Commands like "take a photo," "send a message," "detect currency," and "alert" are identified and processed using NLP techniques.
2. **Task Execution Based on Commands**:
    - **Purpose**: After interpreting user commands, the system executes corresponding tasks based on the identified actions.
    - **Implementation**: Conditional statements are used to check for specific keywords or phrases indicative of different actions, such as capturing a photo, sending a message, or detecting currency. NLP is leveraged to identify these keywords and trigger the appropriate functions accordingly.
    - **Example**: If the user mentions "alert," the system sends a notification with an emergency message. Similarly, commands related to sending messages or capturing photos are executed based on NLP-based command interpretation.

**Conclusion**

The integration of natural language processing enables intuitive interaction with the voice-controlled assistant system. By interpreting user commands and executing tasks based on the identified actions, the system provides a seamless user experience. Ongoing enhancements and refinements to the NLP model can further improve the accuracy and effectiveness of command interpretation, enhancing the overall usability of the system.
 
 
### Optimisation of Code

 Overview

This document outlines the refactoring process for the SixthSense project, focusing on the conversion of the initial script-based implementation into a modular, object-oriented design. The refactor aimed to improve code organization, readability, and maintainability by encapsulating related functionalities into classes and separating concerns into different modules.

 Objectives

- **Modularity:** Divide the project into modular components, each responsible for a specific functionality.
- **Object-oriented design:** Utilize classes and objects to encapsulate related data and behaviors.
- **Code organization:** Organize the project structure to enhance readability and maintainability.
- **Separation of concerns:** Decouple different functionalities to improve code clarity and reusability.

 Changes Made

1. **Creation of Classes:**
    - Identified distinct functionalities in the initial script and encapsulated them into individual classes.
    - Defined classes for WebcamCapture, OCR, Gemini, NotificationSender, MessageSender, and CurrencyDetection.
2. **Module Separation:**
    - Split the project into separate modules, each containing related classes and functions.
    - Modules include capture, ocr, gemini, notification, message, and currency_detection.
3. **Code Refactoring:**
    - Refactored the initial script to utilize the newly created classes and modules.
    - Organized the code into logical sections within each class, following best practices for code readability.
4. **Dependency Management:**
    - Ensured proper dependency management by importing required libraries within each module.
    - Utilized virtual environments or package managers to manage dependencies and versioning.
5. **Documentation:**
    - Documented each class and module, outlining its purpose, functionalities, and usage.
    - Provided inline comments and docstrings to clarify code intent and usage.

 Benefits

- **Improved Readability:** The modular structure and object-oriented design make the code more readable and understandable.
- **Enhanced Maintainability:** Changes or updates to specific functionalities can be made within their respective classes or modules without affecting other parts of the codebase.
- **Reusability:** Encapsulating functionalities into classes promotes code reuse, allowing similar tasks to be easily implemented in different contexts.
- **Scalability:** The organized structure facilitates the addition of new features or functionalities in the future without significant code restructuring.

 Conclusion

The refactoring process successfully transformed the initial script-based implementation of the SixthSense_Gdsc project into a well-organized, modular codebase. By leveraging classes and modules, the project now offers improved readability, maintainability, and scalability. The separation of concerns and encapsulation of functionalities into classes lay a solid foundation for future development and expansion of the project.

---

### Gemini

 Overview

This documentation outlines the conversion of the original code for optimization purposes, focusing on reducing content size and improving retrieval speed. The primary objectives of this conversion are to streamline the codebase, minimize redundant operations, and enhance overall performance.

 Changes Made

1. **Class Segmentation**:
2. **Introduction of Assistant Class**:
3. **Output Formatting**:

 Optimization Strategies

1. **Content Size Reduction**:
2. **Speed Optimization**:

 Performance Evaluation

1. **Content Size Reduction**:
2. **Speed Optimization**:

 Conclusion

The conversion of the code for optimization purposes aims to enhance both content size and retrieval speed. By segmenting the code into classes, limiting response length, and introducing streamlined processing, the refactored version achieves better efficiency and performance. Ongoing monitoring and evaluation will ensure continued optimization and responsiveness.

---
### Multiprocessing using ProcessPoolExecutor

 Overview

The multiprocessing library in Python provides support for parallelizing tasks across multiple CPU cores or processes. It offers several classes and functions to create and manage concurrent processes, improving efficiency and performance in multiprocessing environments.

 ProcessPoolExecutor

The **`ProcessPoolExecutor`** is a high-level interface provided by the concurrent.futures module, built on top of the multiprocessing library. It enables concurrent execution of multiple tasks or functions within separate processes, allowing for parallelism and efficient resource utilization.

 Usage

1. **Initialization**:
    - The **`ProcessPoolExecutor`** is initialized with the desired maximum number of worker processes (**`max_workers`**).
    - `with ProcessPoolExecutor(max_workers=2) as ex:`
2. **Submit Tasks**:
    - Tasks or functions are submitted for execution using the **`submit`** method.
    - `future1 = ex.submit(object_Detection) future = ex.submit(hi)`
3. **Retrieve Results**:
    - The **`submit`** method returns a **`Future`** object representing the result of the submitted task.
    - Results can be retrieved synchronously using the **`result`** method of the **`Future`** object.
    - `result1 = future1.result() result2 = future.result()`
4. **Completion**:
    - The main process waits for the completion of all submitted tasks before proceeding further.
    - `future1.result() future.result()`

 Dependencies

- Python multiprocessing library
- concurrent.futures module

 Notes

- Ensure that tasks submitted to the **`ProcessPoolExecutor`** are designed to be parallelizable and do not rely on shared state or resources that might lead to race conditions.
- Experiment with different values for **`max_workers`** to find the optimal number of worker processes based on system specifications and workload characteristics.

 Conclusion

In summary, the multiprocessing library, coupled with the ProcessPoolExecutor, offers a convenient approach for concurrent task execution in Python, enhancing performance by utilizing multiple CPU cores. By judiciously configuring the executor and task distribution, developers can optimize resource utilization and improve application responsiveness, contributing to efficient parallel processing.

### Voice Assistant

 **Introduction**

This documentation outlines a Python script for a speech recognition assistant that listens for specific wake words and responds to user speech using text-to-speech conversion. The script utilizes various libraries for speech recognition and audio manipulation.

 **Imports**

The script imports the following libraries:

- **`speech_recognition`** (**`sr`**): Recognizes speech from audio recordings.
- **`pyaudio`**: Interacts with the computer's audio hardware for recording.
- **`os`**: Interacts with the operating system.
- **`time`**: Provides timing functionalities.
- **`playsound`**: Plays audio files on the system.
- **`gtts`**: Converts text to speech and saves it as an audio file.

 **GTTS Function**

- **`GTTS(text)`**: Converts text to speech and plays the generated audio using **`playsound`**.

 **get_audio Function**

- **`get_audio()`**: Captures user speech and converts it to text using the **`Recognizer`** instance from **`speech_recognition`**. It listens for audio input from the microphone, records audio, and attempts to recognize the spoken words using Google Speech-to-Text.

 **Main Function**

- **`main()`**: Entry point of the program. Calls **`get_audio()`** to capture and recognize user speech. It then checks if the recognized text contains the wake word "hello". If found, responds with "Hey, how are you?" using **`GTTS`**.

 **Wake Word and Loop**

- **`WAKE = "hello everyone"`**: Defines the wake word that triggers the assistant.
- The script enters a loop that continuously listens for audio using **`get_audio()`**. If the wake word is detected, the assistant responds and listens for further instructions.

 **Usage**

To use the speech recognition assistant, run the script and wait for the prompt. Speak the wake word "hello everyone" to trigger the assistant, then give instructions or ask questions as needed.

### Google Calendar API

**Introduction**

This documentation outlines a Python script that integrates with the Google Calendar API to provide virtual assistant functionalities, including accessing calendar events and creating notes using speech recognition and text-to-speech.

**Imports**

- Standard library imports: **`datetime`**, **`pickle`**, **`os`**, **`time`**
- Google Calendar API imports: **`build`** from **`googleapiclient.discovery`**, **`Credentials`**, and **`InstalledAppFlow`** from **`google_auth_oauthlib.flow`**
- Speech recognition and Text-to-Speech (TTS) imports: **`sr`** for speech recognition, **`pyttsx3`**, and **`gTTS`** for text-to-speech
- Other imports: **`playsound`** for playing audio files, **`subprocess`** for opening external applications

**Google Calendar Authentication**

- **`SCOPES`**: Defines the permissions required to access Google Calendar data.
- **`create_service(client_secret_file, ...)`**: Function to create a service object for interacting with the Google Calendar API. It handles OAuth2 authentication and stores credentials for future use.

 **Helper Functions**

- **`convert_to_RFC_datetime(year, month, day, hour, minute)`**: Converts date and time information to a format compatible with the Google Calendar API.
- **`speak(text)`**: Converts text to speech and plays the audio using either **`pyttsx3`** or **`gTTS`**.

**Voice Class**

- Provides methods for speech recognition and interaction with the virtual assistant:
    - **`get_audio()`**: Listens for user input and converts it to text using **`sr`** (SpeechRecognition).
    - **`authenticate_google()`**: Function for an alternative authentication approach (currently commented out).
    - **`get_events(day, service)`**: Retrieves calendar events for a specific day using the Google Calendar service object.
    - **`get_date(text)`**: Parses user's spoken text to extract date information in various formats.
    - **`note(text)`**: Creates a text file with the provided note text and opens it using **`notepad.exe`** (Windows specific).

 **Main Loop**

- **`WAKE = "hello"`**: Defines the wake word to activate the virtual assistant.
- **`SERVICE = authenticate_google()`**: Calls the authentication function.
- The script continuously listens for user input:
    - Captures user's spoken command.
    - Processes the command based on keywords related to calendar and note functionalities.
    - If no matching keywords are found, responds with "I don't understand".

 **Conclusion**

This documentation provides an overview of a Python script that integrates with the Google Calendar API to create a virtual assistant capable of accessing calendar events and creating notes using speech recognition and text-to-speech functionalities.

### Distance Warning system using Midas 2.1V small

**Introduction:**
The Depth Estimation module, powered by the MIDAS (Monocular Depth Estimation in Real-Time with Deep Learning on Large-Scale Datasets) model, incorporates a Distance Warning System to assist visually challenged individuals in navigation. This addendum outlines the implementation, benefits, and impact of the distance warning system in conjunction with depth estimation.

**Implementation:**
The Distance Warning System is integrated into the existing depth estimation workflow. Upon estimating depth from input images using the MIDAS model, the system analyzes the depth map to identify obstacles in proximity. If an object is detected within a predefined threshold distance, the system triggers an alert to warn the individual about the obstacle's presence.

**Benefits of the Distance Warning System:**

1. **Enhanced Safety:** The Distance Warning System enhances safety for visually challenged individuals by providing real-time alerts about nearby obstacles, enabling them to navigate with increased awareness and confidence.
2. **Independence:** By providing timely warnings, the system promotes independence and autonomy for visually challenged individuals, empowering them to navigate environments with reduced reliance on assistance.
3. **User-Friendly Interface:** The system offers a user-friendly interface, delivering audible or tactile alerts that are easily perceivable and actionable by individuals with visual impairments.

**Impact and Use Cases:**

1. **Indoor Navigation:** The Distance Warning System facilitates indoor navigation for visually challenged individuals, enabling them to maneuver through spaces such as homes, offices, and public buildings with greater ease and safety.
2. **Outdoor Mobility:** In outdoor environments, the system assists individuals in navigating sidewalks, pedestrian crossings, and other urban settings, reducing the risk of collisions with obstacles and hazards.
3. **Public Transportation:** When accessing public transportation services, the system helps individuals locate boarding points, navigate platforms, and avoid obstacles in transit stations.

**Integration with our Sixth Sense:**

The Distance Warning System has been  integrated with our Sixth Sense to provide seamless access and enhanced functionality. By leveraging existing  technologies in Sixth Sense, the system can reach a wider user base and integrate with other accessibility features.

**Conclusion:**

The integration of the Distance Warning System with the Depth Estimation module leveraging the MIDAS model represents a significant advancement in assistive technology for visually challenged individuals. By combining real-time depth estimation with proactive obstacle detection and warning capabilities, the system contributes to improved mobility, independence, and safety in navigating diverse environments.
















































































































































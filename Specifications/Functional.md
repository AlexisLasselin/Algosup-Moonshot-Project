# Functional Specifications

## Table of Contents

<details><summary>Click to expand</summary>

- [Functional Specifications](#functional-specifications)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [Product description](#product-description)
    - [Product functional capabilities](#product-functional-capabilities)
    - [User Roles](#user-roles)
    - [Use Cases for all operations](#use-cases-for-all-operations)
    - [General constraints](#general-constraints)
    - [Assumptions](#assumptions)
    - [Other Software Dependencies](#other-software-dependencies)
  - [Specific Function Descriptions](#specific-function-descriptions)
    - [Camera](#camera)
    - [AI's "Sign Reader"](#ais-sign-reader)
    - [AI's "Sign Maker"](#ais-sign-maker)
    - [User Interface](#user-interface)
    - [Inputs](#inputs)
    - [Processing](#processing)
    - [Outputs](#outputs)
    - [Hardware Interfaces](#hardware-interfaces)
    - [Performance](#performance)
    - [Design Constraints](#design-constraints)
  - [Attributes](#attributes)
    - [Security](#security)
    - [Reliability, Availability, Maintainability](#reliability-availability-maintainability)
    - [Configurability and Compatibility](#configurability-and-compatibility)
    - [Installability](#installability)
    - [Usability](#usability)
  - [Additional Requirements](#additional-requirements)
    - [Database](#database)
    - [Administration](#administration)
    - [User documentation](#user-documentation)
    - [Other requirements](#other-requirements)

</details>

## Overview

<!-- Describe the purpose, scope, and organization of the Functional Specification. -->

### Product description

This document details the functional specifications for **MonSigne**, a mobile application designed to bridge communication gaps between sign language users and non-signing individuals. The first version of the app will support French Sign Language (LSF) to French, followed by American Sign Language (ASL) to American English.

<!-- Describe briefly why the software (or upgrade) is being developed, and list the most important features and capabilities. -->

### Product functional capabilities

The application must have the following capabilities:

- **LSF to French Translation**

  - Utilize smartphone cameras to capture sign language.
  - AI-based "Sign Reader" to interpret and convert LSF into text.
  - Adjust translations for proper syntax.
  - Display real-time translated text.
  - Provide user feedback options for accuracy improvement.

- **French to LSF**
  - Accept user input via text or voice.
  - Convert spoken/written language into LSF syntax.
  - Utilize AI-based "Sign Maker" to generate sign language through an avatar.
  - Display real-time signed output.
  - Offer feedback options for improving AI accuracy.

### User Roles

<!-- Describe the intended users of the software in terms of job roles, specialized knowledge, skill levels, etc. Considers various user roles such as managers, administrators, auditors, etc. -->

The application is designed for a broad audience, including:

- Deaf and Hard-of-Hearing Users – Primary users who need to communicate with non-signers.
- General Public – Individuals who need to interact with sign language users.
- Healthcare Professionals, Government Staff, and Customer Service Representatives – Users who require quick translation services in professional settings.

### Use Cases for all operations

<!-- Describe how persons will normally use the software and the tasks they will most frequently perform. Also covers how users might use the software on an occasional basis, such as creating data backups or importing data from another program. -->

The application will enable seamless communication in real-world scenarios such as medical consultations, where a deaf patient needs to interact with a doctor who does not know sign language. In government offices, the app can assist deaf individuals in filling out forms or receiving official information. Educational settings, such as conferences or lectures, will also benefit from the real-time translation feature, allowing attendees to follow spoken presentations more easily. The app is designed to function across a variety of environments, making sign language communication more accessible.

### General constraints

<!-- Describe any algorithm limitations, user interface limitations, data limitations, etc. Include items such as minimum space or room needed to house equipment, type of electrical and HVAC required (e.g. conditioned power), and maintenance requirements. Also, state if training is required for optimum use, or if calculated results are only applicable in certain situations. -->

The application requires a stable internet connection to process translations in real time, as AI models will primarily operate on cloud-based servers. It must work effectively across smartphone models, camera qualities, and lighting conditions to ensure accurate sign recognition. The translation process must have a minimal delay to enable fluid conversations. Additionally, privacy considerations must be addressed, ensuring that user data is processed securely and in compliance with relevant regulations.

### Assumptions

<!-- List any assumptions that were made in specifying the functional requirements. -->

It is assumed that most users will have at least basic fluency in LSF or ASL, allowing them to interact with the app effectively. The application is expected to be free to use, with an optional tipping feature to support ongoing development and improvements. Users will be willing to provide feedback on translations, helping to refine AI accuracy over time. It is also assumed that the app will be used in environments where a smartphone camera and microphone can function without significant obstruction.

### Other Software Dependencies

<!-- How does the program interact with other software, such as spreadsheets, word processing, or presentation software? For example, can a user cut and paste from the application to other Windows software programs? Does the program import/export data to other software? Does the program use any communication, integration, or protocols to exchange data with other software? -->

The application will require access to the device's camera and microphone to capture and process sign language and spoken language. AI models will rely on cloud-based processing for real-time translation, meaning the app must communicate with remote servers. If necessary, offline translation capabilities may be explored in future versions, but initial versions will prioritize cloud-based AI for improved accuracy and adaptability.

## Specific Function Descriptions

<!-- This section is repeated for each function of the software. Some examples of functions are: engineering calculations, sorting or sequencing, other operations relating inputs to outputs, validity checks on inputs, error handling, and recovery. -->

The product will be split into 4 main functions: the camera, the AI's "Sign Reader", the AI's "Sign Maker" and the user interface.

### Camera

<!-- Describe the function and its role in the software. -->

The camera will serve as the primary input method for capturing sign language gestures. It must function under various lighting conditions and adapt to different camera resolutions to ensure accuracy. The captured gestures will be analyzed by the AI’s "Sign Reader", which will then process the data into a structured format for translation. Users should be able to position themselves correctly within the frame for optimal recognition.

### AI's "Sign Reader"

<!-- Describe the function and its role in the software. -->

The AI’s "Sign Reader" is responsible for translating sign language gestures into written or spoken language. It must recognize hand movements, facial expressions, and contextual meaning to ensure accurate translations. Since LSF and ASL have different grammar structures than spoken languages, the AI must reformat the translation to align with proper sentence structure. Continuous learning from user feedback will help refine its accuracy over time.

### AI's "Sign Maker"

<!-- Describe the function and its role in the software. -->

The AI’s "Sign Maker" will convert spoken or written language into sign language, displaying the translated message through an animated avatar. Since LSF and ASL have unique grammatical rules, the AI must restructure sentences accordingly. The avatar must be clear, expressive, and natural in its signing movements to ensure comprehension. The system should also allow users to provide feedback on translation accuracy.

### User Interface

<!-- Describe the function and its role in the software.

Describe all major screens, pages, and forms, including any complex dialog boxes. This is usually best done via simulated, non-functioning screenshots, and may take the form of a separate document.

The navigation flow of the windows, menus, and options is described, along with the expected content of each window. Examples of items included are screen resolutions, color scheme, primary font type, and size. Discussion also includes how input validation will be done, and how data will be protected from accidental changes. Specific items are described for each screen such as input fields, control buttons, sizing options, and menus. -->

The user interface will be minimalistic and intuitive to ensure ease of use in real-time conversations. It will display translated text or the signing avatar clearly on the screen. Users will have the option to provide feedback on translations by confirming or correcting the output. Since the app may be used in public spaces, the interface should be adaptable to various screen sizes and camera positions. Accessibility features such as high-contrast modes and font size adjustments should also be available.

### Inputs

<!-- Describe the inputs to the function. Where user interface (UI) elements are present, these are described. Examples of UI elements are checkboxes, dropdown lists, and alphanumeric fields. Input validation strategy, allowed data types, and value ranges are specified for each input. -->

The primary inputs for the application will be sign language gestures captured by the camera and spoken or typed text input. The camera must accurately track hand and facial movements to process sign language effectively. For voice input, a speech recognition system will transcribe spoken words into text before conversion into sign language. Input validation and error detection mechanisms must ensure that incorrect or incomplete inputs do not disrupt translations.

### Processing

<!-- Describe what is done by the function. Where algorithms, equations, or other logic are used, they are described here. If calculations are done utilizing the methods of specific standards or references, these are cited. Database definitions are also included where relevant. -->

The translation process will involve AI models analyzing sign language gestures or spoken text, restructuring the data to fit the correct grammatical format, and displaying the final output in either text or sign language. AI models must continuously learn from user feedback to improve accuracy. The system should optimize data processing to minimize delays, ensuring real-time translation with high reliability.

### Outputs

<!-- Describe the outputs of the function. Where a user interface description is relevant, it is included. Define any reports. -->

The application’s output will include translated text for sign language users and an animated avatar performing sign language for non-signers. The text will be displayed prominently on the screen, ensuring readability. If an avatar is used, its gestures must be smooth and natural to maintain comprehension. The system should allow users to adjust display settings for better visibility based on their preferences.

### Hardware Interfaces

<!-- Describe the equipment needed to run the software, and also other output or input devices such as printers or handheld devices. -->

The application will require a smartphone with a functional camera and microphone to operate effectively. It must support different camera resolutions to accommodate a variety of device models. The app should also be optimized for both touch-based and voice-based interactions, ensuring accessibility across different user preferences.

### Performance

<!-- Discuss items such as response times, throughput requirements, data volume requirements, maximum data file size or problem complexity, maximum number of concurrent uses, and peak load requirements (for web-based applications). Includes expected response times for entering information, querying data files and databases, performing calculations of various complexities, and importing/exporting data. -->

The translation process must be completed within one second to maintain the natural flow of conversation. AI models should be optimized to run efficiently on mobile hardware while offloading intensive processing to cloud-based services when necessary. The application must support at least 100 concurrent translations per second on the cloud infrastructure to accommodate high demand. It should function effectively under various lighting conditions and camera resolutions, ensuring consistent accuracy in sign recognition. The voice recognition system should have at least 95% accuracy in detecting spoken language and converting it into text. Furthermore, the app should consume minimal battery and data to remain usable for extended periods without draining the device’s resources.

### Design Constraints

<!-- Examples of constraints that affect software design choices are items such as memory constraints involving minimum and maximum RAM and hard disk space, and limitations arising from hardware, software, or communications standards. -->

The application must operate efficiently on both high-end and low-end smartphones, which limits the complexity of AI models running on the device. It must adhere to platform-specific guidelines for Android and iOS to ensure smooth user experience and compliance with store policies. The interface should remain minimalistic and distraction-free to facilitate effective communication, particularly in public and professional settings. Real-time translation demands low-latency processing, requiring optimization of AI models to balance accuracy and speed. Additionally, the app must be designed with accessibility in mind, ensuring compatibility with assistive technologies like screen readers and voice commands.

## Attributes

### Security

<!-- Describe any password-protected access levels such as operator, engineer/modeler, manager, or database administrator which functionality will be accessible to each access level. If relevant, describe the planned approach to locking the software. -->

User authentication may be required for personalized settings, but anonymous usage should remain an option. Data transmission must be encrypted to protect user privacy. Users should have the ability to opt out of data collection used for AI improvements. No personally identifiable information should be stored without explicit consent.

### Reliability, Availability, Maintainability

<!-- Describe requirements items such as days or weeks of continuous operation, strategy for data recovery, and code structuring for ease of future modification. -->

The application must ensure an uptime of at least **95.5%**, allowing for continuous availability. AI models should receive periodic updates to improve translation accuracy. A cloud-based infrastructure should be utilized to scale translation services efficiently. Logs should be maintained to track errors and translation accuracy for future improvements.

### Configurability and Compatibility

<!-- Describe requirements such as those connected with individual customization or operation in specific computing environments. -->

The app should support both Android and iOS devices, ensuring compatibility across major smartphone brands. It must adapt to various screen sizes and resolutions for consistent usability. Users should have the option to configure settings such as font size, contrast, and translation speed based on their preferences.

### Installability

<!-- Describe the planned method for installation: done by the user independently, done by customer company internal IT services, done by an external contractor. Specifies the handling of such items as data transfer from prior releases, and the presence of software elements from prior releases. -->

The application should be easily downloadable from official app stores, with a simple, guided installation process. Updates should be delivered seamlessly through over-the-air (OTA) updates, requiring minimal user intervention. Installation should not require significant manual setup or configuration.

### Usability

<!-- Describe items that will ensure the user-friendliness of the software. Examples include error messages that direct the user to a solution, input range checking as soon as entries are made, and order of choices and screens corresponding to user preferences. -->

The interface must be intuitive, allowing users to operate the app without prior training. Accessibility features, such as screen reader compatibility and customizable visual settings, should be incorporated. Error messages should provide clear guidance to help users resolve issues quickly.

## Additional Requirements

<!-- Describe other characteristics the software must have, that were not covered in the prior sections. -->

### Database

<!-- Describe any specific requirements relating to the database, such as database type (e.g. relational), capability to handle large text fields, real-time capability (e.g. handling an incoming data stream, as from instruments), multi-user capability, and special requirements relating to queries and forms. -->

A cloud-based database will store AI training data and user feedback to enhance translation accuracy. The system must support real-time data processing to ensure efficient AI performance. User preferences should be stored locally for offline functionality when needed.

### Administration

<!-- Include any periodic updating or data management needed. -->

Administrative tools should allow monitoring of system performance and AI accuracy. Scheduled maintenance windows should be planned for updates without disrupting user experience. A reporting dashboard should be available to track translation errors and user engagement trends.

### User documentation

<!-- Describe the user documentation to be delivered with the software, including both hard copy and online requirements. -->

A built-in tutorial should guide new users through the app’s features. An FAQ section and troubleshooting guide should be easily accessible within the app. Users should have the option to contact support directly for assistance.

### Other requirements

<!-- Describe any other requirements not already covered above that need to be considered during the design of the software. -->

The application must comply with **GDPR** and other data protection regulations. AI models should be continuously updated to recognize new signs and improve accuracy. Community feedback should be actively incorporated to refine the translation system over time.

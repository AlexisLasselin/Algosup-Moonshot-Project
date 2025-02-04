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
    - [Other software Dependencies](#other-software-dependencies)
  - [Specific Function Descriptions](#specific-function-descriptions)
    - [Camera](#camera)
    - [AI's "Sign Reader"](#ais-sign-reader)
    - [AI's "Sign Maker"](#ais-sign-maker)
    - [User Interface](#user-interface)
    - [Inputs](#inputs)
    - [Processing](#processing)
    - [Outputs](#outputs)
    - [Hardware Interfaces](#hardware-interfaces)
    - [Communication Interfaces](#communication-interfaces)
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

<!-- Describe how persons will normally use the software, and the tasks they will most frequently perform. Also covers how users might use the software on an occasional basis, such as creating data backups or importing data from another program. -->

There will be only one real use, allow communication in a quick and efficient way, now I'll show you different use cases:

1. Medical Scenario: A deaf patient communicates with a doctor who does not know sign language.
2. Government Services: A deaf individual filling out paperwork at a local office.
3. Education & Conferences: Attendees using the app to understand spoken presentations.

### General constraints

<!-- Describe any algorithm limitations, user interface limitations, data limitations, etc. Include items such as minimum space or room needed to house equipment, type of electrical and HVAC required (e.g. conditioned power), maintenance requirements. Also, state if training is required for optimum use, or if calculated results are only applicable in certain situations. -->

- Requires a stable internet connection for real-time AI translation.
- Must function across varying camera qualities and lighting conditions.
- Translation latency must be minimized to enable fluid conversations.

### Assumptions

<!-- List any assumptions that were made in specifying the functional requirements. -->

- Users are primarily fluent in LSF or ASL.
- The app will remain free, with an optional tipping feature to support development.

### Other software Dependencies

<!-- How does the program interact with other software, such as spreadsheets, word processing or presentation software? For example, can a user cut and paste from the application to other Windows software programs? Does the program import/export data to other software? Does the program use any communication, integration, or protocols to exchange data with other software? -->

- Requires camera and microphone access.
- Cloud-based AI models for translation processing.

## Specific Function Descriptions

<!-- This section is repeated for each function of the software. Some examples of functions are: engineering calculations, sorting or sequencing, other operations relating inputs to outputs, validity checks on inputs, error handling and recovery. -->

The product will be splited in 4 mains functions: the camera, the AI's "Sign Reader", the AI's "Sign Maker" and the user interface.

### Camera

<!-- Describe the function and its role in the software. -->

The camera will be used to capture the sign language and transform it into a digital format that the AI's "Sign Reader" can understand.

### AI's "Sign Reader"

<!-- Describe the function and its role in the software. -->

The AI's "Sign Reader" will be used to translate the sign language into spoken language.
However, as LSF's grammar is different from the French one, the AI's "Sign Reader" will need to reapply the correct synthax to the translated text.

### AI's "Sign Maker"

<!-- Describe the function and its role in the software. -->

Similarly to the AI's "Sign Reader", the AI's "Sign Maker" will be used to translate the spoken language into sign language.
The AI's "Sign Maker" will need to transform the sentence to adapt it as the LSF synthax.
Thanks to an avatar, the AI's "Sign Maker" will be able to sign the sentence.

### User Interface

<!-- Describe the function and its role in the software.

Describe all major screens, pages, forms, including any complex dialog boxes. This is usually best done via simulated, non-functioning screen shots, and may take the form of a separate document.

The navigation flow of the windows, menus, and options is described, along with the expected content of each window. Examples of items included are screen resolutions, color scheme, primary font type and size. Discussion also includes how input validation will be done, and how data will be protected from accidental changes. Specific items are described for each screen such as input fields, control buttons, sizing options, and menus. -->

The user interface will be used to display the result of the translation on the smartphone screen.
The app will be really simple to use and the design will be minimalist to not disturb the conversation.
During the testing phase, a button asking if the translated line was correctly translated will appear at the bottom of the screen, and if not, ask the user to rewrite the correct sentence, same goes for the signed sentence.

As the application will be used in public places, the user interface will need to be adapted to every type of camera.

### Inputs

<!-- Describe the inputs to the function. Where user interface (UI) elements are present, these are described. Examples of UI elements are check boxes, dropdown lists, and alphanumeric fields. Input validation strategy, allowed data types and value ranges are specified for each input. -->

The inputs of the application will be the sign language and the spoken language.

The sign language will be captured by the camera, and the spoken language will be typed or spoken by the user.

The application will need a good internet connection to work properly, as it will use AI to translate the sign language into spoken language and vice versa.

### Processing

<!-- Describe what is done by the function. Where algorithms, equations, or other logic are used, they are described here. If calculations are done utilizing the methods of specific standards or references, these are cited. Database definitions are also included where relevant. -->

The application will use AI to translate the sign language into spoken language and vice versa.

The AI's "Sign Reader" will be used to translate the sign language into spoken language meanwhile the AI's "Sign Maker" will be used to translate the spoken language into sign language.

The AI's "Sign Reader" will need to reapply the correct synthax to the translated text, and the AI's "Sign Maker" will need to transform the sentence to adapt it as the LSF synthax.

### Outputs

<!-- Describe the outputs of the function. Where a user interface description is relevant, it is included. Define any reports. -->

The outputs of the application will be the translated sign language and the translated spoken language.

The application will display the result of the translation on the smartphone screen, possibly below the camera to get the two different displays at the same time, even if the translation might take a bit of latency.

### Hardware Interfaces

<!-- Describe the equipment needed to run the software, and also other output or input devices such as printers or handheld devices. -->

The application will require a camera access to work properly, as it will use the camera to translate the sign language into spoken language and vice versa.
A microphone might be used to allow the user to speak the sentence to be translated.

### Communication Interfaces

<!-- Describes how the software product will communicate with itself (for multi-platform applications) or other software applications, including items such as networking, email, intranet, and Internet communications. -->

### Performance

<!-- Discuss items such as response times, throughput requirements, data volume requirements, maximum data file size or problem complexity, maximum number of concurrent uses, and peak load requirements (for web-based applications). Includes expected response times for entering information, querying data files and databases, performing calculations of various complexities, and importing/exporting data. -->

### Design Constraints

<!-- Examples of constraints that affect software design choices are items such as memory constraints involving minimum and maximum RAM and hard disk space, and limitations arising from hardware, software or communications standards. -->

## Attributes

### Security

<!-- Describe any password-protected access levels such as operator, engineer/modeler, manager, database administrator-and which functionality will be accessible to each access level. If relevant, describes the planned approach to locking the software. -->

### Reliability, Availability, Maintainability

<!-- Describe requirements items such as days or weeks of continuous operation, strategy for data recovery, code structuring for ease of future modification. -->

### Configurability and Compatibility

<!-- Describe requirements such as those connected with individual customization or operation in specific computing environments. -->

### Installability

<!-- Describe the planned method for installation: done by the user independently, done by customer company internal IT services, done by an external contractor. Specifies the handling of such items as data transfer from prior releases, and the presence of software elements from prior releases. -->

### Usability

<!-- Describe items that will ensure the user-friendliness of the software. Examples include error messages that direct the user to a solution, input range checking as soon as entries are made, and order of choices and screens corresponding to user preferences. -->

## Additional Requirements

<!-- Describe other characteristics the software must have, that were not covered in the prior sections. -->

### Database

<!-- Describe any specific requirements relating to the database, such as database type (e.g. relational), capability to handle large text fields, real-time capability (e.g. handling an incoming data stream, as from instruments), multi-user capability, special requirements relating to queries and forms. -->

### Administration

<!-- Include any periodic updating or data management needed. -->

### User documentation

<!-- Describe the user documentation to be delivered with the software, including both hard copy and online requirements. -->

### Other requirements

<!-- Describe any other requirements not already covered above that need to be considered during the design of the software. -->

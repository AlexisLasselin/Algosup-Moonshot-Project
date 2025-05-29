# Moonshot Project Report

## Table of Contents

<details>
<summary>Click to expand</summary>

- [Moonshot Project Report](#moonshot-project-report)
	- [Table of Contents](#table-of-contents)
	- [I. Introduction](#i-introduction)
	- [II. Problem Statement](#ii-problem-statement)
	- [III. Project Overview](#iii-project-overview)
		- [Project Description](#project-description)
		- [Target Users](#target-users)
		- [Contexts of Use](#contexts-of-use)
		- [Added Value and Impact](#added-value-and-impact)
	- [IV. Functional Specifications](#iv-functional-specifications)
	- [V. Technical Specifications](#v-technical-specifications)
	- [VI. Software Architecture](#vi-software-architecture)
	- [VII. Algorithm and Model Design](#vii-algorithm-and-model-design)
	- [VIII. Testing Strategy](#viii-testing-strategy)
	- [IX. Deployment and Production](#ix-deployment-and-production)
	- [X. Project Management](#x-project-management)
	- [XI. Future Developments](#xi-future-developments)
	- [XII. Conclusion](#xii-conclusion)

</details>

## I. Introduction

In France, approximately 200,000 people are completely deaf, and many more are hard of hearing. For many of them, French Sign Language (LSF) is the primary means of communication. Yet, despite its importance, LSF remains marginalized — it is not officially recognized as a language by the French government, and is not taught in schools as foreign languages like English or Spanish are.

This lack of formal recognition creates a significant communication gap between the deaf and hearing populations. While some individuals do learn LSF, it is far from widespread. As a result, deaf people often struggle to communicate effectively in key situations — particularly in administrative, medical, or social contexts — where LSF interpreters are not always available, especially outside of major cities.

To cope, many rely on written communication, which can be frustrating, limited, and far from inclusive.

This project aims to help bridge that gap by developing a mobile application that translates French Sign Language (LSF) into text and vice versa, using machine learning models for real-time translation. The goal is to empower deaf individuals to communicate more easily and independently in their daily lives.

You might wonder why existing tools, like Google Translate or other sign language apps, are not used instead. The reason is simple: most of them do not support LSF. They typically focus on American Sign Language (ASL), or occasionally Indian Sign Language (ISL), and cannot be reliably used in the French context.

![Sign Language Family Tree](./SignLanguageFamilyTree.png)

As shown above, sign languages differ greatly across countries. Even those with shared roots — like French Sign Language (LSF) and Belgian French Sign Language (LSFB) — have distinct grammar, vocabulary, and cultural contexts. A tool built for ASL or BSL cannot simply be adapted to LSF without risking significant inaccuracies.

Some innovative solutions like [SignAll](https://signall.world/) exist, but they are mainly targeted at ASL and do not offer support for LSF. This is where my project comes in — to create a solution tailored to the needs of French signers.

I chose this project because I’ve always wanted to use my technical skills to make a real impact. I believe this app can improve the daily lives of many deaf individuals in France, while also allowing me to explore fields I’m passionate about: machine learning, mobile development, and digital accessibility.

## II. Problem Statement

As mentioned in the introduction, the core issue is the persistent communication gap between deaf individuals who use French Sign Language (LSF) and the hearing population. This gap is deepened by the lack of official recognition and widespread teaching of LSF in France, which limits the ability of most hearing people to understand or use the language.

Many deaf individuals depend on sign language interpreters to navigate essential services. However, interpreters are expensive, not always available, and generally concentrated in major cities. In rural or less populated regions, access is often nonexistent, leaving deaf individuals isolated in critical moments such as medical consultations, administrative procedures, or everyday social interactions.

While there are some existing tools in France, such as [Keia](https://www.keia.io/), an AI-based solution that translates written content from government or insurance websites into LSF videos, these solutions focus on static, one-way translation of formal content. They do not support real-time, bidirectional communication for day-to-day conversations.

This project aims to fill that gap by developing a mobile application capable of real-time translation between LSF and written French. By leveraging machine learning to recognize and translate sign language gestures, the application will enable more inclusive, accessible, and autonomous communication for deaf individuals in a variety of everyday situations.

## III. Project Overview

The goal of this project is to develop a mobile application that bridges the communication gap between deaf and hearing individuals in France by enabling real-time translation between French Sign Language (LSF) and written French.

### Project Description

The application is designed as an assistive communication tool for deaf users, allowing them to interact more independently and fluidly in daily situations where LSF is not understood by the people around them. It will include the following core features:

- **Sign-to-Text Translation**: Users perform signs in front of the camera, and the app recognizes the gesture and displays its meaning in written French.
- **Text-to-Sign Translation**: Users input text or speech, and the app returns the equivalent LSF gesture, using either animations or sign videos.

> [!NOTE]
> Regarding my scholar project, I will focus on the sign-to-text translation feature, as it is the most complex and technically challenging part of the application, according to my research and discussions with experts in the field.

### Target Users

This application is primarily designed for:

- **Administrative and Medical Professionals**: To facilitate communication with deaf clients or patients who use LSF.
- **Deaf Individuals Able to Use LSF**: To empower them to communicate more effectively in everyday situations, such as shopping, asking for directions, or attending appointments.
  Note than the app is intended to help them, so the person that might use it is not the deaf individual, but rather the hearing person who needs to communicate with them.
- **Companies and Organizations**: To improve inclusivity in customer service, healthcare, and public services by enabling staff to communicate with deaf clients.
  > [!NOTE]
  > Since the law [n° 2005-102 from February 11, 2005](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000809647?isSuggest=true) mandates accessibility for people with disabilities, including those who are deaf or hard of hearing, this app can help organizations comply with these requirements.

### Contexts of Use

The app is intended to be used in various contexts, including:

- **Medical Settings**: During consultations, check-ups, or emergencies where communication with healthcare professionals is essential.
- **Administrative Offices**: For tasks like filling out forms, understanding procedures, or asking questions in government offices.
- **Public Services**: In places like banks, post offices, or public transportation where deaf individuals need to interact with staff who may not know LSF.
- **Social Interactions**: In everyday situations like shopping, dining, or asking for help in public spaces, even if I don't plan to focus on this part of the application.

### Added Value and Impact

Compared to existing tools that focus on American Sign Language (ASL) or static content translation (mainly an alphabet and that's it), this application offers a **real-time, LSF-specific** solution tailored to the **cultural and linguistic context of France**. It promotes:

- Greater autonomy for deaf individuals
- Increased public awareness of LSF
- Improved inclusivity in essential services

By focusing specifically on French Sign Language and real-life interaction, this project aims to make a meaningful social and technological contribution.

## IV. Functional Specifications

- Core features
- User roles
- Interaction flow (e.g., sign-to-text, voice-to-sign)
- Accessibility considerations

## V. Technical Specifications

- Technology stack
- System architecture
- Model architecture (if applicable)
- Dataset structure and sources

## VI. Software Architecture

- Backend and frontend structure
- Data flow diagram
- Model integration
- APIs and components

## VII. Algorithm and Model Design

- Chosen algorithm(s) and frameworks
- Training methodology
- Performance evaluation
- Strengths and limitations

## VIII. Testing Strategy

- Functional testing
- Model accuracy and validation
- User feedback and iterations
- Tools used

## IX. Deployment and Production

- Hosting strategy
- App publication plans (e.g., app stores)
- Maintenance and updates
- Data privacy and ethical concerns

## X. Project Management

- Methodology used (Agile, Kanban, etc.)
- Timeline and planning
- Tools for organization (Trello, GitHub, etc.)
- Challenges encountered and how they were managed

## XI. Future Developments

- Short-term enhancements
- Long-term vision
- Potential collaborations and scaling

## XII. Conclusion

- Summary of learnings
- Reflections on the project
- Next steps professionally and technically

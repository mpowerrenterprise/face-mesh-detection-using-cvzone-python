# Face Detection with CVZONE

## Introduction

A computer vision prototype to detect key facial points in a human face. This is called as Face Mesh Detection, it is a machine learning model for detecting & analyzing key facial features from images. It is like a 3D model of a face.

MediaPipe Face Mesh is a face geometry solution that estimates 468 3D face landmarks in real-time even on mobile devices. It employs machine learning (ML) to infer the 3D surface geometry, requiring only a single camera input without the need for a dedicated depth sensor. Utilizing lightweight model architectures together with GPU acceleration throughout the pipeline, the solution delivers real-time performance critical for live experiences.

Additionally, the solution is bundled with the Face Geometry module that bridges the gap between the face landmark estimation and useful real-time augmented reality (AR) applications. It establishes a metric 3D space and uses the face landmark screen positions to estimate face geometry within that space.

The face geometry data consists of common 3D geometry primitives, including a face pose transformation matrix and a triangular face mesh. Under the hood, a lightweight statistical analysis method called Procrustes Analysis is employed to drive a robust, performant and portable logic. The analysis runs on CPU and has a minimal speed/memory footprint on top of the ML model inference.

## Features
- Detect human face Mesh.
- Able to analyze facial key points.
- Able to build geometry-based face recognition application with this prototype.  


## Technologies & Frameworks

- Python 3.8
- OpenCV
- CVzone

## What is CVZONE?

CVzone is the main Framework that is used in this prototype, it is a computer vision package that makes us easy to run like face detection, hand tracking, pose estimation, etc., and also image processing and other AI functions.


## Configuration and Setup

Python is the main programming language of this prototype, OpenCV and CVzone are the major Frameworks.


- Installing OpenCV

  ```python
  pip install opencv-python
  ```

- Installing cvzone using GitHub, (If "pip install cvzone" does not work)

    ```python
    pip install git+https://github.com/cvzone/cvzone.git
    ```


## Demo

![](github-readme-content/demo.gif)

Social Media Links
---

* [Linkedin Profile](https://www.linkedin.com/in/gunarakulangunaretnam/)
* [Facebook Page](https://www.facebook.com/gunarakulangunaretnam)
* [Twitter Profile](https://twitter.com/gunarakulan)
* [Instagram Profile](https://www.instagram.com/gunarakulangunaretnam/)
* [Youtube Channel](https://www.youtube.com/channel/UCMWkED5sabgVZSCKjZuRJXA)

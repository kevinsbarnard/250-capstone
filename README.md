# 250-capstone
CSCI250 capstone project repository, Group 11.

## Virtual Calculator: 2D Triangulation from a Multi-Accelerometer System

For this project, we will be building a multi-accelerometer sensor system to triangulate points in 2D space from recorded vibration signals. We will use these points, in conjunction with a pre-made piece of paper outlined as a calculator, to make a virtual calculator based on where a user touches on the piece of paper.

## Team Roles

**Azam Abidjanov:** Circuit design

**Kevin Barnard:** Software & data processing

**Brendan Paver:** Report & video

## Project Requirements

**Make use of at least 3 different sensors.**
We will make use of accelerometers, a push button, and an LED. We will use the accelerometers to triangulate the points, the push button to perform a calibration on the board, and an LED to signal that the program has received a valid point.

**Collect and store data (or status info) in external files.**
We will store the accelerometer calibration data in binary files so that calibration only needs to be done once.

**Process data using NumPy arrays and efficient (vectorized, concurrent) calculations.**
We will collect the signal data in numpy arrays for processing. Most of these calculations can be vectorized, as signal processing cares little for individual data points, and more so for aggregate patterns to be matched.

**Display data in the final report to demonstrate the project functionality.**
We will create 2D plots of the triangulated points to show what the accelerometer triangulation is finding.

**Interpret the project data and provide a discussion on the project outcome/success.**
We will analyze the 2D points for accuracy and consistency, as well as our signal processing algorithms for their efficacy and efficiency. These results will be numeric, so that we can compare different iterations and configurations of the hardware.

## Project timeline and milestones

### Week 1
* Acquire hardware elements
* Construct first iteration of the hardware
* Write code base for signal processing and triangulation

### Week 2
* Complete signal processing algorithm
* Complete triangulation algorithm
* First tests on triangulation

### Week 3
* Modify hardware and software as needed from tests
* Test further and iterate
* Create demonstration video
* Write project final report

### Week 4
* Finalize video and report
* Submit entire project

## Hardware Elements
* Sparkfun accelerometer x 3
* Sparkfun LED x 1
* Sparkfun push button x 1
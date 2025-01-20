# TRACTOR-X: Autonomous Tractor Simulation in Webots<br>

## Overview<br>
TRACTOR-X is a student project developed as part of the *Industrie 4.0 Projekt* module during the Winter Semester 2024/2025 under the guidance of Prof. M. Wiehl.<br>
The project demonstrates the autonomous behavior of a tractor in a simulated farm environment using **Webots R2023b or newer**.<br>
The tractor can navigate to specified locations, recognize and avoid animals, and return to its starting position autonomously.<br>

---

## Objectives<br>
- Develop an autonomous tractor simulation in a farm scenario using **Webots**.<br>
- Demonstrate navigation to four predefined points on the farm and back to the origin.<br>
- Integrate animal recognition and obstacle avoidance using sensors and/or camera with **OpenCV**.<br>
- Enable functionality to pause for a random interval (5-10 seconds) before restarting the navigation sequence.<br>

---

## Key Features<br>
1. **Autonomous Navigation**: Navigate the tractor to predefined points on the farm.<br>
2. **Animal Recognition**: Detect animals using the onboard camera and avoid collisions.<br>
3. **Obstacle Avoidance**: Navigate around detected obstacles during the traversal.<br>
4. **Real-time Sensor Display**: Output current coordinates and sensor values on the console.<br>
5. **Restart Functionality**: Automatically restart the navigation after a random pause.<br>

---

## Tools and Resources<br>
- **Webots R2023b or newer**: Simulation environment for robotics.<br>
- **Python**: Programming language for all controller implementations.<br>
- **OpenCV**: For image processing and animal recognition using the camera.<br>
- **OTH Resources**:<br>
  - GPU laboratory<br>
  - PC rooms (Faculty of MBUT)<br>
  - Creative Space<br>
  - GitLab for repository management<br>
  - Moodle for file exchange<br>
  - Rocket Chat for communication<br>
  - OTH Filr for file sharing<br>

---

## Setup Instructions<br>
1. **Install Webots**:<br>
   - Download Webots R2023b or newer from the [official website](https://cyberbotics.com/).<br>
2. **Clone the Repository**:<br>
   ```bash<br>
   git clone https://github.com/your-username/TRACTOR-X.git<br>
   cd TRACTOR-X<br>
   ```<br>
3. **Install Dependencies**:<br>
   - Python 3.x<br>
   - OpenCV: Install using pip:<br>
     ```bash<br>
     pip install opencv-python<br>
     ```<br>
4. **Run the Simulation**:<br>
   - Open Webots and load the `boomer` world from the `samples/vehicles` category.<br>
   - Adapt the environment and tractor controller as specified in the project.<br>

---

## Implementation Details<br>
### Milestone Deliverables<br>
- **Console Output**: Display sensor values, including current coordinates.<br>

### Final Demonstration<br>
- Navigate through four points:<br>
  1. **Point A**<br>
  2. **Point B**<br>
  3. **Point C**<br>
  4. **Point D**<br>
- Return to the origin.<br>
- Pause for 5-10 seconds and restart.<br>

### Sensors and Features<br>
- **GPS**: For coordinate tracking.<br>
- **Camera**: For animal detection and recognition (integrated with OpenCV).<br>

---

## Project Timeline<br>
| Phase                  | Date Range       | Description                                |<br>
|------------------------|------------------|--------------------------------------------|<br>
| Distribution of Info   | 16th October     | Share project details and objectives.      |<br>
| Team Building          | 16th - 20th Oct  | Formation of teams.                        |<br>
| Kickoff Meeting        | 21st - 27th Oct  | Initial meeting with Professor Wiehl.      |<br>
| Milestone Meeting      | 2nd - 6th Dec    | Present progress and sensor outputs.       |<br>
| Report Submission      | 13th January     | Submit project report.                     |<br>
| Final Presentation     | 13th - 20th Jan  | Demonstrate the project.                   |<br>

---

## Usage of Results<br>
1. Demonstrate robot navigation in robotics courses.<br>
2. Showcase simulation results on large screens during marketing events.<br>

---

## Licensing and Legal Framework<br>
- Students retain copyrights to their work.<br>
- Third parties interested in project results must arrange agreements with the students.<br>
- No confidential data should be processed during the project.<br>

---

## Acknowledgments<br>
We thank Prof. M. Wiehl and OTH Amberg-Weiden for providing resources and guidance throughout the project.<br>
Special thanks to the Webots community for tutorials and support.<br>

---

## Contact<br>
For inquiries or collaborations, please contact the project team through OTH GitLab or Rocket Chat.<br>

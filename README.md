# 🤖 Assistive-Bot-FYDP

This repository contains all code and assets related to our Final Year Design Project: an **Autonomous Assistive Bot** designed for malls and industrial environments. The system is modular, with components including **dual display screens**, **autonomous movement**, and **cloud-integrated navigation**.

---

## 🧠 Project Overview

The Assistive Bot is a modular robotic system composed of:

* **Secondary Display**: Shows promotional banners and highlights discounts on a map.
* **Primary Display**: Displays gestures and interactive content for user engagement.
* **Autonomous Navigation**: Uses ROS for floor mapping and movement based on cloud-stored store location data.
* **Cloud Integration**: Floor and discount locations are retrieved dynamically via the cloud.

---

## 📂 Repository Structure

```
Assistive-Bot-FYDP/
├── Secondary_Display/      # Code for secondary (promo) display screen
├── Primary_Display/        # Code for primary (gesture/interactive) screen
├── Movement/               # Autonomous movement code using ROS
├── assets/                 # Images, banners, logos, etc.
├── scripts/                # Helper scripts (optional)
├── README.md               # Project overview
└── .gitignore              # Ignored files list
```

---

## 🛠️ Tech Stack

* ROS (Robot Operating System)
* Python
* OpenCV (for gesture detection and visualization)
* HTML/CSS/JavaScript (for UI screens)
* RViz, Gazebo (for ROS simulation)
* Cloud storage (for map and location data)

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/AssistiveRobot/Assistive-Bot-FYDP.git
cd Assistive-Bot-FYDP
code .
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run ROS launch files (example):

```bash
roslaunch movement navigation.launch
```

---

## 👥 Team Workflow (Using Git + VS Code)
These steps ensure all team members stay in sync and contribute efficiently.

* **1️⃣ Set Up Git in VS Code (One Time)**
- git config --global user.name "assistiverobotfydp@gmail.com"
- git config --global user.email "assistive@robot123"

* **2️⃣ Pull Latest Code Before Starting Work**
- git pull origin main

* **3️⃣ Create a New Branch for Your Task**
- git checkout -b feature/task-name

* **Examples:**
- feature/primary-display-gesture
- bugfix/floor-map-error

* **4️⃣ Stage & Commit Your Work**
- git add .
- git commit -m "Meaningful message about your change"

* **5️⃣ Push to GitHub**
- git push origin feature/task-name
- Then open GitHub → Create Pull Request → Get it reviewed → Merge to main.

* **6️⃣ After Merging Pull Requests**

- git checkout main
- git pull origin main
- git branch -d feature/task-name

---

## ✅ Best Practices     

| ❌ Don't	                     |     ✅ Do                         |
| ------------------------------- | -----------------------------------|
| Push to main directly	          | Use feature branches               |
| Work without pulling updates	  |Run git pull origin main regularly  |
| Leave unclear commit messages	  |Use short, clear descriptions       |

---

## 💡 General Guidelines

- Create **feature branches** off `main`.
- **Never commit directly to `main`** — always use a Pull Request (PR).
- Write clear commit messages:
  - ✅ `git commit -m "Added discount banner logic to secondary display"`
- **Always `git pull` before starting new work.**

---

## 🌿 Branch Naming

Use this format:
- `feature/secondary-display-ui`
- `bugfix/map-highlight-issue`
- `docs/readme-update`

## 🧪 Testing

Please test your code **before** pushing. For ROS nodes:
- Launch in simulation (Gazebo or RViz)
- Confirm no errors in `roscore`

## ✅ Pull Requests

- Assign 1 team member for review
- Add a short summary of what was added
- Mention related issue or task

## 📁 Folder Rules

- Keep all `Secondary_Display` code in that folder
- Store images in `/assets`
- Add helper scripts (bash, Python) in `/scripts`

---

## 🙌 Team

| Name          | Role           | Area                                                         |
| ------------- | -------------- | ------------------------------------------------------------ |
| Muhammad Saim | Leader         | Project management and bot movement design                   |
| Mubeen Sheikh | Support Member | Procurement, logistics, and hardware setup                   |
| Hafsa Ahsan   | Lead Developer | Primary & Secondary Display, module integration coordination |
| Zainab Bibi   | Lead Developer | Primary & Secondary Display, module integration coordination |

---

## 📧 Contact

For queries or contributions, feel free to open an [issue](https://github.com/AssistiveRobot/Assistive-Bot-FYDP/) or contact one of the team members.

---

## 📜 License

This project is an academic Final Year Design Project (FYDP) and is **not currently open-sourced under any license**.

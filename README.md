<div align="center">
  
  <img src="static/images/logo.png" alt="AI Security Labs Logo" width="100" />
  
  <h1>AI Security Labs</h1>

  <p>An advanced, interactive educational platform focused on AI system vulnerabilities, attack vectors, and offensive security methodologies.<br><b>[Adversarial Prompt Injection, Data Poisoning, Model Stealing, Agent Hijacking, etc.]</b></p>

  <a href="https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Falekhakumarswain%2FAI-SECURITY-LABS">
    <img src="https://vercel.com/button" alt="Deploy with Vercel">
  </a>

  <br>
  <br>

  <a href="#-overview"><b>Course Overview</b></a> | <a href="#-features"><b>Hands-on Labs</b></a> | <a href="https://github.com/alekhakumarswain/AI-SECURITY-LABS"><b>GitHub Repository</b></a>

  <br>
  <br>
  
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Vercel-Deployed-black?logo=vercel&style=flat-square" alt="Vercel">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">

  <br>
  <br>
  
  <!-- Showcase Image -->
  <img src="static/images/hero.png" width="800" alt="Platform Architecture Overview">

</div>

---

## 🚀 Overview

**AI Security Labs** is a comprehensive learning platform designed to teach the fundamentals and advanced concepts of AI security. The application is built using a modern **Python FastAPI** backend, rendering beautiful **Vanilla CSS** templates through **Jinja2**. All course data is modularly structured using YAML files, making it incredibly easy to expand the curriculum.

## ✨ Features

- **Extensive Course Curriculum**: Dive deep into topics like:
  - Agent & Autonomous System Attacks (Tool Injection, SSRF, Excessive Agency)
  - Adversarial Attacks & Prompt Injection
  - Data Poisoning & Supply Chain Compromise
  - Model Evasion & Model Stealing
  - AI System Quality Testing & Red Teaming
- **Modular Architecture**: Courses are dynamically generated from rich YAML definitions. Adding a new module is as simple as dropping a new `.yaml` file.
- **Interactive UI/UX**: Sleek, dark-mode focused aesthetic built specifically for security enthusiasts.
- **Server-Side Rendering Context**: Optimized for blazing-fast content delivery.
- **Vercel Ready**: Pre-configured `vercel.json` for immediate edge deployment.

## 🛠️ Tech Stack

*   **Backend framework**: [FastAPI](https://fastapi.tiangolo.com/)
*   **Templating Engine**: [Jinja2](https://jinja.palletsprojects.com/)
*   **Data Serialization**: [PyYAML](https://pyyaml.org/)
*   **Server**: [Uvicorn](https://www.uvicorn.org/)
*   **Frontend**: HTML5, Vanilla CSS3 (Custom Design System)

## 📦 Getting Started Locally

### Prerequisites

Ensure you have Python 3.9+ installed on your system. 

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/alekhakumarswain/AI-SECURITY-LABS.git
   cd AI-SECURITY-LABS
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

## 🌐 Deployment (Vercel)

This application is fully prepared for serverless deployment on [Vercel](https://vercel.com/). You can use the "Deploy with Vercel" button at the top of this documentation to instantly clone and deploy the app!

If you prefer using the [Vercel CLI](https://vercel.com/docs/cli):
```bash
vercel
```

## 📂 Project Structure

```
.
├── app.py                     # Main FastAPI application
├── requirements.txt           # Python dependencies
├── vercel.json                # Vercel deployment configuration
├── details/                   # Course Data (YAML files)
│   ├── adversarial_attacks.yaml
│   ├── ai_agent_attacks.yaml
│   ├── data_poisoning.yaml
│   └── ...
├── templates/                 # Jinja2 HTML Templates
│   ├── index.html             # Landing Page
│   ├── learn.html             # Course Curriculum Page
│   └── labs.html              # Hands-On Lab Terminal UI
└── static/                    # Static Assets (CSS, Fonts, Images)
    ├── images/
    └── fonts/
```

## ⚖️ Disclaimer

The information provided within AI Security Labs is for **educational and research purposes only**. Do not use these techniques to attack systems you do not have explicit permission to test.

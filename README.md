<div align="center">
  <img src="static/images/logo.png" alt="AI Security Labs Logo" width="120" />
  <h1>AI Security Labs</h1>
  <p>An advanced, interactive educational platform focused on AI system vulnerabilities, attack vectors, and offensive security methodologies.</p>
</div>

---

## 🚀 Overview

**AI Security Labs** is a comprehensive learning platform designed to teach the fundamentals and advanced concepts of AI security. It covers a wide range of critical topics, from Adversarial prompt injection attacks to Multi-Modal Vision-Language exploits. 

The application is built using a modern **Python FastAPI** backend, rendering beautiful **Vanilla CSS** templates through **Jinja2**. All course data is modularly structured using YAML files, making it incredibly easy to expand the curriculum.

## ✨ Features

- **Extensive Course Curriculum**: Dive deep into topics like:
  - Agent & Autonomous System Attacks (Tool Injection, SSRF, Excessive Agency)
  - Adversarial Attacks & Prompt Injection
  - Data Poisoning & Supply Chain Compromise
  - Model Evasion & Model Stealing
  - AI System Quality Testing & Red Teaming
- **Modular Architecture**: Courses are dynamically generated from rich YAML definitions. Adding a new module is as simple as dropping a new `.yaml` file.
- **Interactive UI/UX**: Sleek, dark-mode focused, glass-morphism aesthetic built specifically for security enthusiasts.
- **Server-Side Rendering Context**: Optimized for blazing fast content delivery.
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

1. Clone this repository (or download the source code):
   ```bash
   git clone <repository-url>
   cd LLMSecurity
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   python app.py
   ```
   *Alternatively, using uvicorn directly:*
   ```bash
   uvicorn app:app --reload
   ```

4. Open your browser and navigate to:
   **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

## 🌐 Deployment (Vercel)

This application is fully prepared for serverless deployment on [Vercel](https://vercel.com/).

### Method 1: Using GitHub
1. Push this repository to GitHub.
2. Go to your Vercel Dashboard and click **"Add New..." > "Project"**.
3. Import your GitHub repository. Vercel will automatically detect the Python environment and build the application.

### Method 2: Using the Vercel CLI
If you have the [Vercel CLI](https://vercel.com/docs/cli) installed globally:
```bash
vercel
```
Follow the interactive prompts to deploy the project instantly.

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

# Contributing to AI Security Labs

First off, thank you for considering contributing to **AI Security Labs**! Open-source communities thrive on passionate developers, researchers, and security practitioners like you. 

## How can I contribute?

### 1. Reporting Bugs and Issues
If you find a bug in the code or a typo in a course document, please submit an issue on GitHub. 
* Use a descriptive title and include as much detail as possible.
* If it relates to a specific course module, please mention the `.yaml` filename.

### 2. Suggesting Enhancements
We are always looking for ways to expand our course curriculum or improve our frontend application.
* Have a new AI attack vector you want added?
* Found a better way to structure the CSS?
* Let us know by opening an issue labeled `enhancement`.

### 3. Adding or Updating Course Curriculum
The courses are entirely modularized via `.yaml` files in the `details/` directory. 
* To add a new piece of content, refer to an existing YAML file (like `adversarial_attacks.yaml`) to understand the schema (`attack_types`, `mitigations`, etc.).
* Submit a PR with your newly created or heavily edited `.yaml` content.

### 4. Code Contributions
1. **Fork the Repository**: Create your own fork and clone it linearly locally.
2. **Branch**: Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. **Commit**: Commit your changes (`git commit -m 'Add some AmazingFeature'`). Ensure your Python code is well documented.
4. **Push**: Push to your branch (`git push origin feature/AmazingFeature`).
5. **Open a Pull Request**: Explain your changes and wait for a review!

## Code Formatting and Guidelines

- Python backend code (`app.py`, etc.) should adhere to standard PEP 8 naming conventions.
- YAML files should use 2-space indentation and completely avoid hidden characters like tabs, as PyYAML will break.
- For frontend UI changes in `templates/`, keep the components clean using raw vanilla CSS.

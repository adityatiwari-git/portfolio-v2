# Aditya Tiwari Portfolio — V2

A modern personal portfolio website showcasing my projects, skills, internships, and journey across **Bioinformatics, Software Engineering, AI, and Full-Stack Development**.

## 🚀 Features

- Responsive single-page design
- Modern dark UI
- Smooth animations and transitions
- Skills, experience, learning direction, and project showcase
- Resume download
- Direct project GitHub links
- Social/contact links
- Accessible focus states and reduced-motion support

## 🛠️ Built With

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- AOS (Animate On Scroll)

## 📂 Project Structure

```text
portfolio-v2/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── script.js
└── assets/
    ├── profile.jpg
    └── resume.pdf
```

## 🌐 Live Demo

https://adityatiwari-git.github.io/portfolio-v2/

The site is deployed as a static GitHub Pages portfolio.

## 📬 Contact

- GitHub: https://github.com/adityatiwari-git
- LinkedIn: https://www.linkedin.com/in/er-aditya-tiwari/
- Email: tiwariaditya28925@gmail.com

---

**Portfolio V2** — a refreshed version of my personal portfolio focused on clearer project presentation and a stronger recruiter experience.

Designed and developed by **Aditya Tiwari**.

## 🤖 Scheduled Project Maintenance

This repository has its own GitHub Actions maintenance workflow. It is **repository-local**, so it uses GitHub's built-in `GITHUB_TOKEN` instead of a personal access token or cross-repository secret.

### What the `.github/` folder is for

- `.github/workflows/daily-maintenance.yml` — runs the scheduled maintenance workflow.
- `.github/maintenance/schedule.json` — stores this repository's assigned dates and task names.
- `.github/maintenance/run_task.py` — contains the simple, predefined task logic.

The workflow runs at varied scheduled times defined in this repository's maintenance schedule and can also be started manually from the Actions tab.

Assigned October 2026 dates:
- 2026-10-09
- 2026-10-18
- 2026-10-26

> **No meaningful change = no commit and no pull request.**

The workflow does not use Claude, OpenAI, or another external AI coding service.

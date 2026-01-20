# Anoop's Portfolio

A dynamic portfolio website for Anoop, a BCA student and web developer, built with Flask.

## Features

- **Introduction/About Me**: Personal introduction and career goals.
- **Educational Details**: BCA course information.
- **Technical Skills**: Showcase of programming languages and tools.
- **Projects**: Display of recent projects with descriptions and technologies.
- **Certifications/Internships**: Placeholder for certifications and internships.
- **Contact Information**: Email and social media links.
- **Resume Download**: Link to download resume PDF.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Templates**: Jinja2
- **Styling**: Custom CSS with glassmorphism effects

## Project Structure

```
anoop_portfolio/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── templates/
│   └── index.html         # Main template
└── static/
    ├── css/
    │   └── style.css      # Stylesheet
    ├── js/
    │   └── script.js      # JavaScript
    ├── images/
    │   └── 1.png          # Profile image (placeholder)
    └── resume.pdf         # Resume PDF (placeholder)
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/anoop_portfolio.git
   cd anoop_portfolio
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/`

## Customization

- Update personal information in `app.py` under the `portfolio_data` dictionary.
- Replace placeholder files:
  - `static/images/1.png` with actual profile image.
  - `static/resume.pdf` with actual resume PDF.
- Modify styles in `static/css/style.css`.
- Add more sections or features as needed.

## Deployment

This Flask app can be deployed to platforms like Heroku, AWS, or DigitalOcean. Ensure to set `debug=False` in production.

## License

This project is open source and available under the [MIT License](LICENSE).

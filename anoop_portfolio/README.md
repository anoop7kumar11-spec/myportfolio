<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/b0b94f98-5472-4c6c-8afe-a8969faadd4c" />
<img width="1914" height="901" alt="image" src="https://github.com/user-attachments/assets/76b55dd1-6ec0-45b3-977f-608984aca43f" />
<img width="1898" height="890" alt="image" src="https://github.com/user-attachments/assets/b69435da-7306-47f6-97a7-884ef05f27fb" />
<img width="1919" height="952" alt="image" src="https://github.com/user-attachments/assets/02c31cbd-a5c5-4d26-b939-206b78245931" />
<img width="1910" height="952" alt="image" src="https://github.com/user-attachments/assets/fdf65bd0-2145-48f6-8f58-945163a22388" />




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


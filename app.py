from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Data for the portfolio
    portfolio_data = {
        'name': 'Anoop',
        'title': 'BCA Student & Web Developer',
        'introduction': 'Hello! I\'m Anoop, a final year BCA student based in India. I enjoy creating things that live on the internet. My interest in web development started back in 2023 when I decided to try editing custom Tumblr themes — turns out hacking together HTML & CSS is pretty fun!',
        'education': {
            'course': 'Bachelor of Computer Applications (BCA)',
            'institution': 'Your University Name',
            'year': 'Final Year (2026)',
            'specialization': 'Computer Science'
        },
        'skills': [
            {'name': 'HTML5', 'icon': 'fab fa-html5', 'color': '#e34c26'},
            {'name': 'CSS3', 'icon': 'fab fa-css3-alt', 'color': '#264de4'},
            {'name': 'JavaScript', 'icon': 'fab fa-js', 'color': '#f0db4f'},
            {'name': 'React', 'icon': 'fab fa-react', 'color': '#61dbfb'},
            {'name': 'Java', 'icon': 'fab fa-java', 'color': '#5382a1'},
            {'name': 'Git', 'icon': 'fab fa-git-alt', 'color': '#f1502f'}
        ],
        'projects': [
            {
                'title': 'E-Commerce Dashboard',
                'description': 'A comprehensive admin dashboard for managing inventory, viewing sales analytics, and tracking user data.',
                'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80',
                'tags': ['HTML', 'CSS Grid', 'JS']
            },
            {
                'title': 'Weather App',
                'description': 'Real-time weather application using OpenWeather API. Features geolocation and 5-day forecasting.',
                'image': 'https://images.unsplash.com/photo-1592210454359-9043f067919b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80',
                'tags': ['API', 'Async/Await']
            },
            {
                'title': 'Student Management System',
                'description': 'A full CRUD application for universities to manage student records securely with login authentication.',
                'image': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-1.2.1&auto=format&fit=crop&w=1302&q=80',
                'tags': ['Java', 'SQL', 'Web']
            }
        ],
        'certifications': [
            {'name': 'Placeholder Certification 1', 'issuer': 'Issuer Name', 'year': '2024'},
            {'name': 'Placeholder Certification 2', 'issuer': 'Issuer Name', 'year': '2025'}
        ],
        'contact': {
            'email': 'anoop@example.com',
            'github': 'https://github.com/anoop',
            'linkedin': 'https://linkedin.com/in/anoop',
            'twitter': 'https://twitter.com/anoop',
            'instagram': 'https://instagram.com/anoop'
        },
        'stats': [
            {'number': '10+', 'label': 'Projects'},
            {'number': '3+', 'label': 'Years Code'},
            {'number': '20+', 'label': 'Repos'}
        ]
    }
    return render_template('index.html', data=portfolio_data)

@app.route('/download_resume')
def download_resume():
    return send_from_directory('static', 'resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

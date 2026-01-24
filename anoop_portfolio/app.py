from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Data for the portfolio
    portfolio_data = {
        'name': 'Anoop Kumar',
        'title': 'Web Developer | BCA Scholar',
        'introduction': 'Detail-oriented BCA student proficient in building user-friendly and visually appealing web solutions. Fluent in English and Hindi.',
        'education': [
            {
                'course': 'Bachelor of Computer Applications (BCA)',
                'institution': 'Trinity College Jalandhar',
                'year': '2026',
                'specialization': 'Computer Science',
                'image': '/static/images/tt.jpg'
            },
            {
                'course': 'Higher Secondary Education',
                'institution': 'D.s.s.d. Sr. Sec. School',
                'year': 'Completed',
                'specialization': '',
                'image': '/static/images/dssd.jpeg'
            }
        ],
        'skills': {
            'Web Dev': [
                {'name': 'HTML', 'icon': 'fab fa-html5', 'color': '#e34c26'},
                {'name': 'CSS', 'icon': 'fab fa-css3-alt', 'color': '#264de4'},
                {'name': 'JavaScript', 'icon': 'fab fa-js', 'color': '#f0db4f'}
            ],
            'Programming': [
                {'name': 'Python', 'icon': 'fab fa-python', 'color': '#3776ab'},
                {'name': 'Java', 'icon': 'fab fa-java', 'color': '#5382a1'},
                {'name': 'C++', 'icon': 'fas fa-code', 'color': '#00599c'}
            ],
            'Data & Tools': [
                {'name': 'SQL', 'icon': 'fas fa-database', 'color': '#336791'},
                {'name': 'MySQL', 'icon': 'fas fa-server', 'color': '#4479a1'},
                {'name': 'Data Structures', 'icon': 'fas fa-sitemap', 'color': '#ff6b35'},
                {'name': 'Algorithms', 'icon': 'fas fa-cogs', 'color': '#ff6b35'},
                {'name': 'MS Office', 'icon': 'fas fa-file-alt', 'color': '#d83b01'}
            ],
            'Design': [
                {'name': 'Graphic Designing', 'icon': 'fas fa-palette', 'color': '#ff4081'}
            ]
        },
        'projects': [
            {
                'title': 'Gaming Console E-commerce Website',
                'description': 'A fully functional e-commerce platform for gaming consoles featuring product listings, shopping cart functionality, animated videos, and order management system.',
                'image': '/static/images/ps.png',
                'tags': ['HTML', 'CSS']
            }
        ],
        'certifications': [
            {'name': 'Swayam Introduction to Cyber Security', 'issuer': 'Swayam', 'year': '2024'},
            {'name': 'NIIT Career Essentials', 'issuer': 'NIIT', 'year': '2023'}
        ],
        'contact': {
            'email': 'anoop7kumar11@gmail.com',
            'phone': '',  # Placeholder, as phone not specified
            'github': 'https://github.com/anoop7kumar11-spec',
            'linkedin': 'https://linkedin.com/in/anoopkumar',
            'twitter': 'https://twitter.com/anoopkumar',
            'instagram': 'https://instagram.com/anoopkumar'
        },
        'stats': [
            {'number': '5+', 'label': 'Projects'},
            {'number': '2+', 'label': 'Years Code'},
            {'number': '10+', 'label': 'Skills'}
        ]
    }
    return render_template('index.html', data=portfolio_data)

@app.route('/download_resume')
def download_resume():
    return send_from_directory('static', 'resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

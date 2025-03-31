import os
import logging
from flask import Flask, render_template

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def index():
    # Project data
    projects = [
        {
            "title": "E-Commerce Platform",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg",
            "description": "A full-featured online shopping platform built with React and Node.js, featuring cart functionality, payment processing, and user accounts.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Weather Dashboard",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
            "description": "Interactive weather application displaying forecast data with dynamic visualizations using D3.js and the OpenWeather API.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Portfolio Generator",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg",
            "description": "Node.js application that generates personalized portfolio websites based on user input and customizable templates.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Task Management System",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg",
            "description": "Kanban-style task management application with drag-and-drop functionality, built with React and a Express.js backend.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Recipe Finder",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
            "description": "Web application that helps users discover recipes based on available ingredients, dietary restrictions, and meal preferences.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Fitness Tracker",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg",
            "description": "Application to track workout routines, exercise progress, and fitness goals with data visualization using D3.js.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Social Media Dashboard",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg",
            "description": "Consolidated dashboard for managing multiple social media accounts with analytics and scheduled posting features.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Budget Planner",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
            "description": "Financial planning tool with expense tracking, budget creation, and visual reports using Chart.js.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Real Estate Listings",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg",
            "description": "Property listing application with search filters, interactive maps, and property comparison features.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Learning Management System",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg",
            "description": "Educational platform for course creation, student enrollment, and progress tracking with interactive lessons.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Travel Planner",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
            "description": "Trip planning application with itinerary creation, destination information, and budget management features.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Blog Platform",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg",
            "description": "Content management system for bloggers with markdown support, category management, and SEO optimization tools.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Music Discovery App",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg",
            "description": "Application to discover new music based on preferences, listening history, and social recommendations.",
            "link": "https://github.com/jonathanpeters"
        },
        {
            "title": "Event Booking System",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
            "description": "Platform for creating, finding, and registering for events with calendar integration and payment processing.",
            "link": "https://github.com/jonathanpeters"
        }
    ]
    
    # Skills data with percentages
    skills = [
        {"name": "HTML", "percentage": 95, "icon": "fab fa-html5"},
        {"name": "CSS", "percentage": 90, "icon": "fab fa-css3-alt"},
        {"name": "JavaScript", "percentage": 85, "icon": "fab fa-js"},
        {"name": "React", "percentage": 80, "icon": "fab fa-react"},
        {"name": "Node.js", "percentage": 75, "icon": "fab fa-node-js"},
        {"name": "Express.js", "percentage": 70, "icon": "fab fa-node-js"},
        {"name": "D3.js", "percentage": 65, "icon": "fas fa-chart-bar"},
        {"name": "Bootstrap", "percentage": 85, "icon": "fab fa-bootstrap"},
        {"name": "Tailwind CSS", "percentage": 80, "icon": "fab fa-css3"},
        {"name": "Python", "percentage": 70, "icon": "fab fa-python"}
    ]
    
    # Tools data
    tools = [
        {"name": "HTML", "icon": "fab fa-html5"},
        {"name": "CSS", "icon": "fab fa-css3-alt"},
        {"name": "JavaScript", "icon": "fab fa-js"},
        {"name": "React", "icon": "fab fa-react"},
        {"name": "Node.js", "icon": "fab fa-node-js"},
        {"name": "Express.js", "icon": "fab fa-node-js"},
        {"name": "D3.js", "icon": "fas fa-chart-bar"},
        {"name": "Bootstrap", "icon": "fab fa-bootstrap"},
        {"name": "Tailwind CSS", "icon": "fab fa-css3"},
        {"name": "Python", "icon": "fab fa-python"},
        {"name": "GitHub", "icon": "fab fa-github"},
        {"name": "Replit", "icon": "fas fa-code"},
        {"name": "VS Code", "icon": "fas fa-code"}
    ]
    
    # Social media links
    social_links = [
        {"platform": "WhatsApp", "icon": "fab fa-whatsapp", "link": "https://wa.me/1234567890"},
        {"platform": "Facebook", "icon": "fab fa-facebook-f", "link": "https://facebook.com/jonathanpeters"},
        {"platform": "Twitter", "icon": "fab fa-twitter", "link": "https://twitter.com/jonathanpeters"},
        {"platform": "LinkedIn", "icon": "fab fa-linkedin-in", "link": "https://linkedin.com/in/jonathanpeters"},
        {"platform": "Instagram", "icon": "fab fa-instagram", "link": "https://instagram.com/jonathanpeters"},
        {"platform": "GitHub", "icon": "fab fa-github", "link": "https://github.com/jonathanpeters"},
        {"platform": "Replit", "icon": "fas fa-code", "link": "https://replit.com/@jonathanpeters"}
    ]
    
    return render_template('index.html', 
                          projects=projects, 
                          skills=skills, 
                          tools=tools, 
                          social_links=social_links)

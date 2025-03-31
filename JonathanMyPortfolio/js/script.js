document.addEventListener('DOMContentLoaded', function() {
    // Project data
    const projects = [
        {
            "title": "Crypto Tracker App",
            "image": "cryptotracker.png",
            "projectImg": "cryptotracker.png",
            "description": "An app that allows yu to buy & sell crypto",
            "link": "https://qms85.github.io/CryptoTrackerPro/"
        },
        {
            "title": "Digital Divide Records",
            "image": "javascript",
            "projectImg": "digitaldividerecords.png",
            "description": "A South African House Music Record Label",
            "link": "https://digitaldividerecords-pty-ltd.github.io/DigitalDivideRecords/"
        },
        {
            "title": "Drag Me",
            "image": "nodejs",
            "projectImg": "dragme.png",
            "description": "A div element, that you can drag around the screen",
            "link": "https://qms85.github.io/DragMeAroundTheScreen/"
        },
        {
            "title": "Entrepreneurship",
            "image": "react",
            "projectImg": "entrepreneurship.png",
            "description": "A guide to Entrepreneurship, using Replit .",
            "link": "https://entrepreneurship-withreplit.streamlit.app/"
        },
        {
            "title": "GitHub Profile Search",
            "image": "javascript",
            "projectImg": "githubprofilesearch.png",
            "description": "A Web app that searches for Github profiles,enter username & enter",
            "link": "https://qms85.github.io/Github-User-Search/"
        },
        {
            "title": "GKroon Investment Calculator",
            "image": "nodejs",
            "projectImg": "gkrooninvestmentcalculator.png",
            "description": "An investment calculator, in $USD",
            "link": "https://gkroon-web.github.io/Investment-Calculator/"
        },
        {
            "title": "GKroon Password Generator",
            "image": "react",
            "projectImg": "gkroonpasswordgenerator.png",
            "description": "This app generates passwords up to 24 characters",
            "link": "https://qms85.github.io/Password-Generator/"
        },
        {
            "title": "GKroon",
            "image": "javascript",
            "projectImg": "gkroonwebsite.png",
            "description": "A business website for GKroon",
            "link": "https://g-kroon.github.io/GKroon/"
        },
        {
            "title": "Music Player",
            "image": "nodejs",
            "projectImg": "musicplayer.png",
            "description": "A mp3 music player. Press Play & enjoy the groove",
            "link": "https://qms85.github.io/MusicPlayer/"
        },
        {
            "title": "Meme Generator",
            "image": "react",
            "projectImg": "memegenerator.png",
            "description": "Upload your images, add text & download your new meme",
            "link": "https://qms85.github.io/MemeGenerator/"
        },
        {
            "title": "Replit Capabilities Guide",
            "image": "javascript",
            "projectImg": "replitcapabilitiesguide.png",
            "description": "A comprehensive guide to Repit.",
            "link": "https://qms85.github.io/ReplitCapabilitiesGuide/"
        },
        {
            "title": "Rectangular Run",
            "image": "nodejs",
            "projectImg": "rectangularrun.png",
            "description": "A simple javascript game, inspired by the classic Dino Run game. Only this version uses rectangles",
            "link": "https://gkroon-web.github.io/RectangleRun/"
        },
        {
            "title": "Sample Artist EPK",
            "image": "react",
            "projectImg": "sampleartistepk.png",
            "description": "A sample artist electronic press kit (EPK)",
            "link": "https://digitaldividerecords-pty-ltd.github.io/SampleArtistEPK/"
        },
        {
            "title": "Calculator",
            "image": "react",
            "projectImg": "calculator.png",
            "description": "A simple calculator",
            "link": "https://qms85.github.io/GitHubCalculator/"
        }
    ];
    
    // Skills data with percentages
    const skills = [
        {"name": "HTML", "percentage": 95, "icon": "devicon-html5-plain colored"},
        {"name": "CSS", "percentage": 90, "icon": "devicon-css3-plain colored"},
        {"name": "JavaScript", "percentage": 85, "icon": "devicon-javascript-plain colored"},
        {"name": "React", "percentage": 80, "icon": "devicon-react-original colored"},
        {"name": "Node.js", "percentage": 45, "icon": "devicon-nodejs-plain colored"},
        {"name": "Express.js", "percentage": 45, "icon": "devicon-express-original colored"},
        {"name": "D3.js", "percentage": 70, "icon": "devicon-d3js-plain colored"},
        {"name": "Bootstrap", "percentage": 70, "icon": "devicon-bootstrap-plain colored"},
        {"name": "Tailwind CSS", "percentage": 70, "icon": "devicon-tailwindcss-plain colored"},
        {"name": "Python", "percentage": 45, "icon": "devicon-python-plain colored"}
    ];
    
    // Tools data
    const tools = [
        {"name": "HTML", "icon": "devicon-html5-plain colored"},
        {"name": "CSS", "icon": "devicon-css3-plain colored"},
        {"name": "JavaScript", "icon": "devicon-javascript-plain colored"},
        {"name": "React", "icon": "devicon-react-original colored"},
        {"name": "Node.js", "icon": "devicon-nodejs-plain colored"},
        {"name": "Express.js", "icon": "devicon-express-original colored"},
        {"name": "D3.js", "icon": "devicon-d3js-plain colored"},
        {"name": "Bootstrap", "icon": "devicon-bootstrap-plain colored"},
        {"name": "Tailwind CSS", "icon": "devicon-tailwindcss-plain colored"},
        {"name": "Python", "icon": "devicon-python-plain colored"},
        {"name": "GitHub", "icon": "devicon-github-original colored"},
        {"name": "Replit", "icon": "devicon-replit-original colored"},
        {"name": "VS Code", "icon": "devicon-vscode-plain colored"}
    ];
    
    // Social media links
    const socialLinks = [
        {"platform": "WhatsApp", "icon": "fab fa-whatsapp", "link": "https://wa.me/+2766119925"},
        {"platform": "Facebook", "icon": "fab fa-facebook-f", "link": "https://facebook.com/2jonathanpeters"},
        {"platform": "Twitter", "icon": "fab fa-twitter", "link": "https://twitter.com/DJJonnas85"},
        {"platform": "LinkedIn", "icon": "fab fa-linkedin-in", "link": "https://linkedin.com/in/2jonathanpeters"},
        {"platform": "Instagram", "icon": "fab fa-instagram", "link": "https://instagram.com/jonathanpeters"},
        {"platform": "GitHub", "icon": "fab fa-github", "link": "https://github.com/QMS85"},
        {"platform": "Replit", "icon": "devicon-replit-plain", "link": "https://replit.com/DJJonnas85"}
    ];

    // Rendering functions
    function renderProjects() {
        const projectsContainer = document.getElementById('projects-container');
        if (!projectsContainer) return;

        let projectsHTML = '';
        
        projects.forEach(project => {
            let iconClass = '';
            
            // Map image names to Devicon classes
            switch(project.image) {
                case 'react':
                    iconClass = 'devicon-react-original colored';
                    break;
                case 'javascript':
                    iconClass = 'devicon-javascript-plain colored';
                    break;
                case 'nodejs':
                    iconClass = 'devicon-nodejs-plain colored';
                    break;
                default:
                    iconClass = 'devicon-devicon-plain colored';
            }
            
            const projectImage = project.projectImg ? 
                `<img src="${project.projectImg}" alt="${project.title}" class="project-image">` : 
                `<i class="${iconClass}"></i>`;
            
            projectsHTML += `
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            ${projectImage}
                            <h3>${project.title}</h3>
                        </div>
                        <div class="flip-card-back">
                            <h3>${project.title}</h3>
                            <p class="typing-text-container">
                                <span class="typing-text">${project.description}</span>
                            </p>
                            <a href="${project.link}" class="btn view-project-btn" target="_blank">View Project</a>
                        </div>
                    </div>
                </div>
            `;
        });
        
        projectsContainer.innerHTML = projectsHTML;
    }

    function renderSkills() {
        const skillsContainer = document.getElementById('skills-container');
        if (!skillsContainer) return;

        let skillsHTML = '';
        
        skills.forEach(skill => {
            skillsHTML += `
                <div class="skill-item">
                    <div class="skill-info">
                        <div class="skill-name">
                            <i class="${skill.icon}"></i>
                            <span>${skill.name}</span>
                        </div>
                        <div class="skill-percentage">${skill.percentage}%</div>
                    </div>
                    <div class="skill-bar">
                        <div class="skill-progress" style="width: ${skill.percentage}%"></div>
                    </div>
                </div>
            `;
        });
        
        skillsContainer.innerHTML = skillsHTML;
    }

    function renderTools() {
        const toolsContainer = document.getElementById('tools-container');
        if (!toolsContainer) return;

        let toolsHTML = '';
        
        tools.forEach(tool => {
            toolsHTML += `
                <div class="tool-item">
                    <i class="${tool.icon}"></i>
                    <span>${tool.name}</span>
                </div>
            `;
        });
        
        toolsContainer.innerHTML = toolsHTML;
    }

    function renderSocialLinks() {
        const socialLinksContainer = document.getElementById('social-links-container');
        if (!socialLinksContainer) return;

        let socialLinksHTML = '';
        
        socialLinks.forEach(social => {
            socialLinksHTML += `
                <a href="${social.link}" target="_blank" title="${social.platform}">
                    <i class="${social.icon}"></i>
                </a>
            `;
        });
        
        socialLinksContainer.innerHTML = socialLinksHTML;
    }

    // Initialize animations for elements when they come into view
    const animateOnScroll = () => {
        const elements = document.querySelectorAll('.section-header, .projects-grid, .skills-content, .tools-grid, .about-content, .contact-content');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 100) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    };
    
    // Set initial styles for animation
    const initAnimations = () => {
        const elements = document.querySelectorAll('.section-header, .projects-grid, .skills-content, .tools-grid, .about-content, .contact-content');
        
        elements.forEach(element => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(20px)';
            element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        });
    };
    
    // Animate progress bars when skills section is in view
    const animateSkillBars = () => {
        const skillsSection = document.getElementById('skills');
        if (!skillsSection) return;
        
        const skillBars = document.querySelectorAll('.skill-progress');
        const sectionPosition = skillsSection.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        
        if (sectionPosition < windowHeight - 100) {
            skillBars.forEach(bar => {
                const width = bar.style.width;
                bar.style.width = '0';
                setTimeout(() => {
                    bar.style.width = width;
                }, 100);
            });
        }
    };
    
    // Smooth scrolling for navigation links
    const smoothScroll = () => {
        const links = document.querySelectorAll('a[href^="#"]');
        
        links.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            });
        });
    };
    
    // EmailJS initialization and form submission handling
    const handleFormSubmission = () => {
        const contactForm = document.getElementById('contact-form');
        const emailStatus = document.getElementById('email-status');
        if (!contactForm) return;
        
        // Initialize EmailJS with your user ID
        // Replace 'YOUR_EMAILJS_USER_ID' with your actual EmailJS user ID/public key
        emailjs.init('k8FMxcW3OlbaRfu2u');
        
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Disable submit button and show loading state
            const submitBtn = document.getElementById('submit-btn');
            const originalBtnText = submitBtn.textContent;
            submitBtn.disabled = true;
            submitBtn.textContent = 'Sending...';
            
            // Send email using EmailJS
            // Replace 'YOUR_EMAILJS_SERVICE_ID' and 'YOUR_EMAILJS_TEMPLATE_ID' with your actual values
            emailjs.sendForm('service_y8eilob', 'template_0fbrelq', this)
                .then(function(response) {
                    // Show success message
                    emailStatus.textContent = 'Thank you! Your message has been sent successfully.';
                    emailStatus.className = 'email-status success';
                    
                    // Reset form
                    contactForm.reset();
                    
                    // Hide success message after 5 seconds
                    setTimeout(() => {
                        emailStatus.style.display = 'none';
                    }, 5000);
                    
                    console.log('SUCCESS!', response.status, response.text);
                }, function(error) {
                    // Show error message
                    emailStatus.textContent = 'Oops! Something went wrong. Please try again later.';
                    emailStatus.className = 'email-status error';
                    
                    console.log('FAILED...', error);
                })
                .finally(() => {
                    // Re-enable submit button
                    submitBtn.disabled = false;
                    submitBtn.textContent = originalBtnText;
                });
        });
    };
    
    // Add active state to navigation links based on scroll position with micro-interactions
    const setActiveNavLink = () => {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('nav ul li a');
        const header = document.querySelector('header');
        
        // Store previous section for transition effects
        let previousSection = '';
        let scrollingTimeout;
        
        window.addEventListener('scroll', () => {
            let current = '';
            const scrollTop = window.pageYOffset;
            
            // Clear the timeout on scroll
            clearTimeout(scrollingTimeout);
            
            // Add scrolling class to header for potential scroll-based effects
            header.classList.add('scrolling');
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                
                if (scrollTop >= (sectionTop - 200)) {
                    current = section.getAttribute('id');
                }
            });
            
            // Only update if we have a change in section
            if (current !== previousSection) {
                // Remove active class from all links first
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    // Remove any transition classes
                    link.classList.remove('fadeIn', 'bounce');
                });
                
                // Find the active link
                const activeLink = Array.from(navLinks).find(link => 
                    link.getAttribute('href') === `#${current}`
                );
                
                // If we have an active link, add classes with animation
                if (activeLink) {
                    activeLink.classList.add('active');
                    
                    // Add a quick animation effect
                    activeLink.classList.add('bounce');
                    setTimeout(() => {
                        activeLink.classList.remove('bounce');
                    }, 500);
                }
                
                // Update previous section
                previousSection = current;
            }
            
            // Remove scrolling class after scrolling stops
            scrollingTimeout = setTimeout(() => {
                header.classList.remove('scrolling');
            }, 150);
        });
        
        // Add click event for smooth scrolling and animation
        navLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                // Remove active class and animations from all links
                navLinks.forEach(l => {
                    l.classList.remove('active', 'fadeIn', 'bounce');
                });
                
                // Add active class and animation to clicked link
                this.classList.add('active', 'fadeIn');
                
                // Find the target section
                const targetId = this.getAttribute('href').substring(1);
                const targetSection = document.getElementById(targetId);
                
                if (targetSection) {
                    e.preventDefault();
                    
                    // Smooth scroll to section
                    window.scrollTo({
                        top: targetSection.offsetTop - 100,
                        behavior: 'smooth'
                    });
                    
                    // Update URL without page reload
                    history.pushState(null, null, `#${targetId}`);
                    
                    // Update previousSection
                    previousSection = targetId;
                }
            });
        });
    };
    
    // Enhance flip cards for touch devices
    const enhanceFlipCards = () => {
        const flipCards = document.querySelectorAll('.flip-card');
        
        flipCards.forEach(card => {
            // For touch devices
            card.addEventListener('touchstart', function() {
                this.querySelector('.flip-card-inner').style.transform = 'rotateY(180deg)';
            });
            
            // Return to front after delay
            card.addEventListener('mouseleave', function() {
                setTimeout(() => {
                    this.querySelector('.flip-card-inner').style.transform = 'rotateY(0deg)';
                }, 1000);
            });
        });
    };
    
    // Add CSS class to style active navigation link
    const styleActiveNavLinks = () => {
        const style = document.createElement('style');
        style.textContent = `
            nav ul li a.active {
                color: var(--primary-light);
            }
            nav ul li a.active::after {
                width: 100%;
            }
        `;
        document.head.appendChild(style);
    };
    
    // Handle CV download notification
    const handleCVDownload = () => {
        const downloadBtn = document.querySelector('.download-cv-btn');
        const notification = document.getElementById('cv-notification');
        
        if (!downloadBtn || !notification) return;
        
        downloadBtn.addEventListener('click', () => {
            // Show the notification
            notification.classList.add('show');
            
            // Hide the notification after 3 seconds
            setTimeout(() => {
                notification.classList.remove('show');
            }, 3000);
        });
    };
    
    // Initialize particles animation
    const initParticles = () => {
        // Check if particles.js is loaded
        if (typeof particlesJS !== 'undefined') {
            // Particle configuration for both header and footer
            const particleConfig = {
                "particles": {
                    "number": {
                        "value": 50,
                        "density": {
                            "enable": true,
                            "value_area": 800
                        }
                    },
                    "color": {
                        "value": ["#FF4500", "#32CD32", "#FF0000"] // Orange, Lime-Green, Red
                    },
                    "shape": {
                        "type": "circle",
                        "stroke": {
                            "width": 0,
                            "color": "#000000"
                        },
                        "polygon": {
                            "nb_sides": 5
                        }
                    },
                    "opacity": {
                        "value": 0.5,
                        "random": true,
                        "anim": {
                            "enable": true,
                            "speed": 1,
                            "opacity_min": 0.1,
                            "sync": false
                        }
                    },
                    "size": {
                        "value": 3,
                        "random": true,
                        "anim": {
                            "enable": true,
                            "speed": 2,
                            "size_min": 0.1,
                            "sync": false
                        }
                    },
                    "line_linked": {
                        "enable": true,
                        "distance": 150,
                        "color": "#32CD32",
                        "opacity": 0.4,
                        "width": 1
                    },
                    "move": {
                        "enable": true,
                        "speed": 2,
                        "direction": "none",
                        "random": true,
                        "straight": false,
                        "out_mode": "bounce",
                        "bounce": false,
                        "attract": {
                            "enable": true,
                            "rotateX": 600,
                            "rotateY": 1200
                        }
                    }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": {
                        "onhover": {
                            "enable": true,
                            "mode": "repulse"
                        },
                        "onclick": {
                            "enable": false,
                            "mode": "push"
                        },
                        "resize": true
                    },
                    "modes": {
                        "grab": {
                            "distance": 400,
                            "line_linked": {
                                "opacity": 1
                            }
                        },
                        "bubble": {
                            "distance": 400,
                            "size": 40,
                            "duration": 2,
                            "opacity": 8,
                            "speed": 3
                        },
                        "repulse": {
                            "distance": 100,
                            "duration": 0.4
                        },
                        "push": {
                            "particles_nb": 4
                        },
                        "remove": {
                            "particles_nb": 2
                        }
                    }
                },
                "retina_detect": true
            };
            
            // Initialize particles for header
            particlesJS('particles-js', particleConfig);
            
            // Initialize particles for footer
            particlesJS('footer-particles-js', particleConfig);
        } else {
            console.error('particles.js not loaded');
        }
    };
    
    // Initialize all functionality
    const init = () => {
        // Render content from data
        renderProjects();
        renderSkills();
        renderTools();
        renderSocialLinks();
        
        // Initialize animations and interactions
        initAnimations();
        animateOnScroll(); // Initial check on page load
        smoothScroll();
        handleFormSubmission();
        setActiveNavLink();
        styleActiveNavLinks();
        enhanceFlipCards();
        handleCVDownload();
        initParticles(); // Initialize particles
        
        // Listen for scroll events
        window.addEventListener('scroll', () => {
            animateOnScroll();
            animateSkillBars();
        });
        
        // Handle window resize events
        window.addEventListener('resize', () => {
            animateOnScroll();
        });
    };
    
    // Initialize everything
    init();
});
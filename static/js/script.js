document.addEventListener('DOMContentLoaded', function() {
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
    
    // Form submission handling
    const handleFormSubmission = () => {
        const contactForm = document.querySelector('.contact-form form');
        if (!contactForm) return;
        
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
            
            // In a real-world scenario, you would send this data to a server
            console.log('Form submission:', { name, email, message });
            
            // Show success message
            alert('Thank you for your message! I will get back to you soon.');
            
            // Reset form
            contactForm.reset();
        });
    };
    
    // Initialize all functionality
    initAnimations();
    animateOnScroll(); // Initial check on page load
    smoothScroll();
    handleFormSubmission();
    
    // Listen for scroll events
    window.addEventListener('scroll', () => {
        animateOnScroll();
        animateSkillBars();
    });
    
    // Handle window resize events
    window.addEventListener('resize', () => {
        animateOnScroll();
    });
    
    // Add active state to navigation links based on scroll position
    const setActiveNavLink = () => {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('nav ul li a');
        
        window.addEventListener('scroll', () => {
            let current = '';
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                
                if (pageYOffset >= (sectionTop - 200)) {
                    current = section.getAttribute('id');
                }
            });
            
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${current}`) {
                    link.classList.add('active');
                }
            });
        });
    };
    
    setActiveNavLink();
    
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
    
    enhanceFlipCards();
    
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
    
    styleActiveNavLinks();
});

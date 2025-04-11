"use client";

import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import NavigationBar from './components/NavigationBar';
import HeroSection from './components/HeroSection';
import AboutSection from './components/AboutSection';
import SkillsSection from './components/SkillsSection';
import ProjectsSection from './components/ProjectsSection';
import EducationSection from './components/EducationSection';
import ContactSection from './components/ContactSection';
import Footer from './components/Footer';
import { useTheme } from './Contexts/ThemeContext';
import { RESUME_DATA } from './data/resume-data';
import ExperienceSection from './components/ExperienceSection';

export default function Portfolio() {
  const { theme } = useTheme();
  const [activeSection, setActiveSection] = useState('home');
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Simulate loading to ensure smooth animations
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 1000);

    // Add scroll event listener for setting active section
    const handleScroll = () => {
      const sections = document.querySelectorAll('section[id]');
      const scrollPosition = window.scrollY + 100;

      sections.forEach((section) => {
        const sectionTop = (section as HTMLElement).offsetTop;
        const sectionHeight = (section as HTMLElement).offsetHeight;
        const sectionId = section.getAttribute('id') || '';

        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
          setActiveSection(sectionId);
        }
      });
    };

    window.addEventListener('scroll', handleScroll);
    return () => {
      clearTimeout(timer);
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  if (isLoading) {
    return (
      <div className="fixed inset-0 flex items-center justify-center bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800">
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="flex flex-col items-center"
        >
          <motion.img
            src="./ucefLogo.png"
            alt="Logo"
            className="w-20 h-20"
            initial={{ opacity: 0, scale: 0.5 }}
            animate={{ 
              opacity: 1,
              scale: 1,
              rotate: [0, 10, -10, 10, 0],
              y: [0, -10, 0]
            }}
            transition={{ 
              duration: 2.5,
              repeat: Infinity,
              repeatType: "reverse",
              ease: [0.25, 0.1, 0.25, 1]
            }}
          />
          <motion.p 
            className="-mt-4 text-gray-700 dark:text-gray-300 text-lg font-medium"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5 }}
          >
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">
              Loading Portfolio...
            </span>
          </motion.p>
        </motion.div>
      </div>
    );
  }

  const fadeInUp = {
    hidden: { opacity: 0, y: 20 },
    visible: { 
      opacity: 1, 
      y: 0,
      transition: {
        duration: 0.6,
        ease: "easeOut"
      }
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-background-light dark:bg-background-dark text-text-light dark:text-text-dark overflow-x-hidden">
      <NavigationBar activeSection={activeSection} />

      <motion.main 
        className="flex-grow"
        initial="hidden"
        animate="visible"
        variants={{
          visible: {
            transition: {
              staggerChildren: 0.1
            }
          }
        }}
      >
        <motion.section id="home" variants={fadeInUp}>
          <HeroSection data={RESUME_DATA as any} />
        </motion.section>
        
        <motion.section id="about" variants={fadeInUp}>
          <AboutSection data={RESUME_DATA} />
        </motion.section>
        
        <motion.section id="skills" variants={fadeInUp}>
          <SkillsSection skills={[...RESUME_DATA.skills]} />
        </motion.section>
        
        <motion.section id="experience" variants={fadeInUp}>
          <ExperienceSection experience={RESUME_DATA.experience} />
        </motion.section>
        
        <motion.section id="projects" variants={fadeInUp}>
          <ProjectsSection 
            projects={RESUME_DATA.projects.map(project => ({
              ...project,
              techStack: [...project.techStack]
            }))}
          />
        </motion.section>
        
        <motion.section id="education" variants={fadeInUp}>
          <EducationSection education={[...RESUME_DATA.education]} />
        </motion.section>
        
        <motion.section id="contact" variants={fadeInUp}>
          <ContactSection 
            contact={{
              ...RESUME_DATA.contact,
              social: [...RESUME_DATA.contact.social]
            }} 
            location={RESUME_DATA.location}
          />
        </motion.section>
      </motion.main>
      
      <Footer socialLinks={[...RESUME_DATA.contact.social]} />
    </div>
  );
}
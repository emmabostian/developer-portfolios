"use client";

import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { ArrowDownIcon, DownloadIcon, GithubIcon, LinkedinIcon, MailIcon } from 'lucide-react';


interface HeroProps {
  data: {
    name: string;
    about: string;
    avatarUrl: string;
    contact: {
      email: string;
      social: {
        name: string;
        url: string;
        icon: any;
      }[];
    };
  };
}

// Simple typewriter effect
const useTypewriter = (text: string, speed: number = 100) => {
  const [displayText, setDisplayText] = useState('');
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isDone, setIsDone] = useState(false);

  useEffect(() => {
    if (currentIndex < text.length) {
      const timeout = setTimeout(() => {
        setDisplayText(prev => prev + text[currentIndex]);
        setCurrentIndex(prev => prev + 1);
      }, speed);
      
      return () => clearTimeout(timeout);
    } else {
      setIsDone(true);
    }
  }, [currentIndex, speed, text]);

  return { displayText, isDone };
};

const HeroSection: React.FC<HeroProps> = ({ data }) => {
  const { displayText, isDone } = useTypewriter(data.about, 30);
  
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
        delayChildren: 0.3,
      }
    }
  };
  
  const itemVariants = {
    hidden: { y: 20, opacity: 0 },
    visible: {
      y: 0,
      opacity: 1,
      transition: { 
        type: "spring",
        stiffness: 100
      }
    }
  };
  
  return (
    <div className="min-h-screen flex items-center justify-center px-4 sm:px-6 md:px-12 py-20 md:py-32 relative overflow-hidden">
      {/* Background gradient */}
      <div className="absolute inset-0 bg-gradient-to-br from-primary/5 to-secondary/5 dark:from-primary/10 dark:to-secondary/10 -z-20" />
      
      {/* Animated particles - Add pointer-events-none to prevent blocking clicks */}
      <div className="absolute inset-0 -z-10 pointer-events-none">
        {Array.from({ length: 20 }).map((_, i) => (
          <motion.div
            key={i}
            className="absolute bg-primary-light/20 dark:bg-primary/30 rounded-full pointer-events-none"
            style={{
              width: Math.random() * 8 + 4,
              height: Math.random() * 8 + 4,
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
            }}
            animate={{
              y: [0, Math.random() * 30 - 15],
              x: [0, Math.random() * 30 - 15],
              opacity: [0.2, 0.5, 0.2],
            }}
            transition={{
              duration: Math.random() * 5 + 5,
              repeat: Infinity,
              repeatType: "reverse",
            }}
          />
        ))}
      </div>
      
      <div className="container mx-auto max-w-6xl relative z-10">
        <div className="flex flex-col md:flex-row items-center justify-between gap-12">
          {/* Left content */}
          <motion.div 
            className="w-full md:w-7/12 text-center md:text-left"
            variants={containerVariants}
            initial="hidden"
            animate="visible"
          >
            <motion.h1 
              className="text-4xl md:text-5xl lg:text-6xl font-bold mb-4"
              variants={itemVariants}
            >
              Hello, I&apos;m <span className="bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary inline-block">{data.name}</span>
            </motion.h1>
            
            <motion.h2 
              className="text-xl md:text-2xl lg:text-3xl font-medium mb-6 text-gray-600 dark:text-gray-300"
              variants={itemVariants}
            >
              Software Developer
            </motion.h2>
            
            <motion.div 
              className="mb-8 text-base md:text-lg text-gray-600 dark:text-gray-300 max-w-xl"
              variants={itemVariants}
            >
              <p className="min-h-[100px]">
                {displayText}
                {!isDone && <span className="inline-block w-1 h-6 ml-1 bg-primary animate-pulse"></span>}
              </p>
            </motion.div>
            
            <motion.div 
              className="flex flex-wrap gap-4 justify-center md:justify-start"
              variants={itemVariants}
            >
              <motion.a
                href={`mailto:${data.contact.email}`}
                className="px-6 py-3 bg-primary hover:bg-primary-dark text-white rounded-lg shadow-lg shadow-primary/20 hover:shadow-primary/30 transition-all duration-300 flex items-center gap-2"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                <MailIcon className="w-4 h-4" />
                Contact Me
              </motion.a>
              
              <motion.a
                href="/resume.pdf"
                target="_blank"
                rel="noopener noreferrer"
                className="px-6 py-3 border border-gray-300 dark:border-gray-600 hover:border-primary hover:text-primary dark:hover:border-primary-light dark:hover:text-primary-light rounded-lg transition-all duration-300 flex items-center gap-2"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                <DownloadIcon className="w-4 h-4" />
                Resume
              </motion.a>
            </motion.div>
            
            <motion.div 
              className="mt-8 flex gap-4 justify-center md:justify-start"
              variants={itemVariants}
            >
              {data.contact.social.map((social, index) => (
                <motion.a
                  key={index}
                  href={social.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="p-2 rounded-full bg-surface-light dark:bg-surface-dark hover:text-primary dark:hover:text-primary-light transition-colors duration-300"
                  whileHover={{ scale: 1.2 }}
                  whileTap={{ scale: 0.9 }}
                >
                  <social.icon className="w-5 h-5" />
                </motion.a>
              ))}
            </motion.div>
          </motion.div>
          
          {/* Right content - Avatar */}
          <motion.div 
            className="w-full md:w-5/12"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            <div className="relative mx-auto w-64 h-64 md:w-80 md:h-80">
              <div className="absolute inset-0 rounded-full bg-gradient-to-r from-primary to-secondary opacity-20 blur-xl animate-pulse" />
              <motion.div 
                className="relative w-full h-full rounded-full p-2 bg-gradient-to-br from-primary to-secondary"
                animate={{
                  boxShadow: [
                    '0 0 20px rgba(59, 130, 246, 0.3)',
                    '0 0 30px rgba(59, 130, 246, 0.5)',
                    '0 0 20px rgba(59, 130, 246, 0.3)',
                  ],
                }}
                transition={{
                  duration: 3,
                  repeat: Infinity,
                  repeatType: 'reverse',
                }}
              >
                <div className="w-full h-full rounded-full overflow-hidden bg-white dark:bg-background-dark p-1">
                  <img 
                    src={data.avatarUrl} 
                    alt={data.name} 
                    className="w-full h-full rounded-full object-cover"
                  />
                </div>
              </motion.div>
            </div>
          </motion.div>
        </div>
      </div>
      
      {/* Scroll down indicator */}
      <motion.div 
        className="absolute bottom-4 transform -translate-x-1/2 flex flex-col items-center"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 1, duration: 0.5 }}
      >
        <motion.span 
          className="text-sm mb-2 opacity-60"
          animate={{ y: [0, 5, 0] }}
          transition={{ duration: 1.5, repeat: Infinity }}
        >
          Scroll Down
        </motion.span>
        <motion.div
          className="bg-primary dark:bg-primary-light rounded-full p-1"
          animate={{ y: [0, 8, 0] }}
          transition={{ duration: 1.5, repeat: Infinity }}
        >
          <ArrowDownIcon className="w-4 h-4 text-white dark:text-background-dark" />
        </motion.div>
      </motion.div>
    </div>
  );
};

export default HeroSection;
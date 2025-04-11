"use client";

import { motion } from 'framer-motion';
import { CodeIcon, BookOpenIcon, BrainCircuitIcon, GraduationCapIcon } from 'lucide-react';

interface AboutProps {
  data: {
    summary: string;
    name: string;
  };
}

const AboutSection: React.FC<AboutProps> = ({ data }) => {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
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

  const qualities = [
    {
      icon: <CodeIcon className="w-6 h-6" />,
      title: "Problem Solver",
      description: "Approaching complex coding challenges with analytical thinking and persistence."
    },
    {
      icon: <BookOpenIcon className="w-6 h-6" />,
      title: "Continuous Learner",
      description: "Passionate about staying updated with the latest technologies and best practices."
    },
    {
      icon: <BrainCircuitIcon className="w-6 h-6" />,
      title: "Creative Thinker",
      description: "Finding innovative solutions by thinking outside the box."
    },
    {
      icon: <GraduationCapIcon className="w-6 h-6" />,
      title: "Academic Focus",
      description: "Pursuing a Master's Degree in IT Architecture in the 42 network."
    }
  ];

  return (
    <div className="py-20 px-4 sm:px-6 md:px-12 relative overflow-hidden" id="about">
      {/* Background shape */}
      <div className="absolute right-0 top-0 w-96 h-96 bg-primary/5 dark:bg-primary/10 rounded-full -translate-y-1/2 translate-x-1/2 blur-3xl -z-10" />
      <div className="absolute left-0 bottom-0 w-96 h-96 bg-secondary/5 dark:bg-secondary/10 rounded-full translate-y-1/2 -translate-x-1/2 blur-3xl -z-10" />
      
      <div className="container mx-auto max-w-6xl">
        <motion.div
          className="text-center mb-16"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 0.5 }}
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">About Me</h2>
          <div className="w-20 h-1 bg-gradient-to-r from-primary to-secondary mx-auto rounded-full" />
        </motion.div>

        <div className="flex flex-col lg:flex-row gap-12 items-center">
          {/* Left side - Image */}
          <motion.div 
            className="w-full lg:w-5/12"
            initial={{ opacity: 0, x: -50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-100px" }}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-br from-primary to-secondary opacity-20 rounded-lg transform rotate-3 scale-105" />
              <div className="absolute inset-0 bg-white dark:bg-gray-800 rounded-lg transform -rotate-3 scale-105" />
              <div className="relative bg-surface-light dark:bg-surface-dark p-6 rounded-lg shadow-xl">
                <h3 className="text-2xl font-semibold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">Who I Am</h3>
                <p className="text-gray-600 dark:text-gray-300 leading-relaxed mb-4">
                  {data.summary}
                </p>
                <div className="pt-4 border-t border-gray-200 dark:border-gray-700">
                  <p className="font-medium text-gray-700 dark:text-gray-200">
                    Currently pursuing my passion for programming in the 42 network, working toward a Master's Degree in IT Architecture.
                  </p>
                </div>
              </div>
            </div>
          </motion.div>

          {/* Right side - Qualities */}
          <motion.div 
            className="w-full lg:w-7/12"
            variants={containerVariants}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, margin: "-100px" }}
          >
            <h3 className="text-2xl font-semibold mb-6 text-center lg:text-left">My Qualities</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {qualities.map((quality, index) => (
                <motion.div 
                  key={index}
                  className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300 group"
                  variants={itemVariants}
                  whileHover={{ y: -5 }}
                >
                  <div className="mb-4 inline-flex p-3 bg-primary/10 dark:bg-primary/20 rounded-lg text-primary dark:text-primary-light group-hover:bg-primary/20 dark:group-hover:bg-primary/30 transition-colors duration-300">
                    {quality.icon}
                  </div>
                  <h4 className="text-xl font-semibold mb-2">{quality.title}</h4>
                  <p className="text-gray-600 dark:text-gray-300">
                    {quality.description}
                  </p>
                </motion.div>
              ))}
            </div>

            <motion.div 
              className="mt-8 text-center lg:text-left"
              variants={itemVariants}
            >
              <p className="text-lg text-gray-600 dark:text-gray-300">
                I am <span className="font-semibold text-primary dark:text-primary-light">passionate about solving problems</span> through code and building applications that provide genuine value.
              </p>
            </motion.div>
          </motion.div>
        </div>
      </div>
    </div>
  );
};

export default AboutSection;
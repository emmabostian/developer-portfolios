"use client";

import { motion } from 'framer-motion';
import { GraduationCapIcon, CalendarIcon, BookOpenIcon } from 'lucide-react';

interface Education {
  school: string;
  degree: string;
  start: string;
  end: string;
}

interface EducationSectionProps {
  education: Education[];
}

const EducationSection: React.FC<EducationSectionProps> = ({ education }) => {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2,
      },
    },
  };

  const itemVariants = {
    hidden: { x: -50, opacity: 0 },
    visible: {
      x: 0,
      opacity: 1,
      transition: {
        type: "spring",
        stiffness: 100,
        damping: 12,
      },
    },
  };

  return (
    <div className="py-20 px-4 sm:px-6 md:px-12 bg-surface-light dark:bg-surface-dark overflow-hidden" id="education">
      <div className="container mx-auto max-w-6xl relative">
        <motion.div
          className="text-center mb-16"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 0.5 }}
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Education Journey</h2>
          <div className="w-20 h-1 bg-gradient-to-r from-primary to-secondary mx-auto rounded-full" />
          <p className="mt-4 text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
            My academic background and educational qualifications that have shaped my skills and knowledge.
          </p>
        </motion.div>

        {/* Education Timeline */}
        <div className="relative">
          {/* Timeline line */}
          <div className="absolute left-4 md:left-1/2 top-0 bottom-0 w-1 bg-gradient-to-b from-primary to-secondary rounded-full transform -translate-x-1/2 md:translate-x-0"></div>

          <motion.div
            className="space-y-12"
            variants={containerVariants}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, margin: "-100px" }}
          >
            {education.map((edu, index) => (
              <motion.div 
                key={index}
                className={`relative flex items-center ${
                  index % 2 === 0 ? 'md:flex-row' : 'md:flex-row-reverse'
                }`}
                variants={itemVariants}
              >
                {/* Timeline point */}
                <div className="absolute left-4 md:left-1/2 w-8 h-8 bg-white dark:bg-gray-800 rounded-full border-4 border-primary dark:border-primary-light transform -translate-x-1/2 flex items-center justify-center z-10">
                  <GraduationCapIcon className="w-4 h-4 text-primary dark:text-primary-light" />
                </div>

                {/* Content */}
                <div className={`w-full md:w-5/12 ${
                  index % 2 === 0 ? 'md:pr-16 md:text-right' : 'md:pl-16'
                }`}>
                  <motion.div 
                    className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg"
                    whileHover={{ y: -5, boxShadow: "0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)" }}
                  >
                    <h3 className="text-xl font-bold text-gray-800 dark:text-white mb-1">{edu.school}</h3>
                    <p className="text-primary dark:text-primary-light font-medium mb-3">{edu.degree}</p>
                    <div className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400 mb-4 justify-start md:justify-end">
                      <CalendarIcon className="w-4 h-4" />
                      <span>{edu.start} - {edu.end}</span>
                    </div>
                    
                    {index === 1 && (
                      <div className="mt-4 bg-primary/10 dark:bg-primary/20 p-3 rounded-lg">
                        <div className="flex items-start gap-2">
                          <BookOpenIcon className="w-5 h-5 text-primary dark:text-primary-light mt-1" />
                          <p className="text-sm text-gray-700 dark:text-gray-300">
                            Part of the prestigious 42 Network, known for its project-based, peer-to-peer learning methodology.
                          </p>
                        </div>
                      </div>
                    )}
                  </motion.div>
                </div>
              </motion.div>
            ))}
          </motion.div>
        </div>

        {/* Education Quote */}
        <motion.div
          className="mt-16 text-center"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5, delay: 0.5 }}
        >
          <blockquote className="text-xl italic text-gray-700 dark:text-gray-300 max-w-3xl mx-auto">
            "Education is the passport to the future, for tomorrow belongs to those who prepare for it today."
          </blockquote>
          <p className="mt-2 text-gray-600 dark:text-gray-400">― Malcolm X</p>
        </motion.div>
      </div>
    </div>
  );
};

export default EducationSection;
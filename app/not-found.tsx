"use client";

import Link from 'next/link';
import { motion } from 'framer-motion';
import { HomeIcon } from 'lucide-react';

export default function NotFound() {
  return (
    <div className="h-screen w-full bg-gray-900 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-gray-900 via-gray-900 to-black flex items-center justify-center relative overflow-hidden text-white">
      {/* Stars background */}
      <div className="absolute inset-0">
        {Array.from({ length: 100 }).map((_, i) => {
          const size = Math.random() * 2 + 1;
          const opacity = Math.random() * 0.5 + 0.5;
          const animationDuration = Math.random() * 5 + 3;
          
          return (
            <motion.div
              key={i}
              className="absolute bg-white rounded-full z-0"
              style={{
                width: size,
                height: size,
                top: `${Math.random() * 100}%`,
                left: `${Math.random() * 100}%`,
                opacity
              }}
              animate={{
                opacity: [opacity, opacity * 0.5, opacity]
              }}
              transition={{
                duration: animationDuration,
                repeat: Infinity,
                repeatType: "reverse"
              }}
            />
          );
        })}
      </div>
      
      {/* Content */}
      <div className="text-center z-10 px-6 max-w-2xl">
        <motion.div
          initial={{ scale: 0.8, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ duration: 0.5 }}
          className="mb-8"
        >
          <h1 className="text-9xl font-bold text-transparent bg-clip-text bg-gradient-to-br from-purple-400 to-blue-600">
            404
          </h1>
        </motion.div>
        
        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.2, duration: 0.5 }}
        >
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            Lost in Space
          </h2>
          
          <p className="text-gray-300 text-lg mb-8">
            The page you are looking for might have been moved, deleted, or perhaps never existed in this universe.
          </p>
          
          <div className="flex justify-center">
            <motion.div
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              <Link 
                href="/"
                className="bg-gradient-to-r from-purple-500 to-blue-500 text-white px-6 py-3 rounded-full flex items-center space-x-2 shadow-lg transition-all duration-300 hover:shadow-purple-500/25"
              >
                <HomeIcon className="w-5 h-5" />
                <span>Return Home</span>
              </Link>
            </motion.div>
          </div>
        </motion.div>
        
        {/* Floating Astronaut */}
        <motion.div
          className="absolute w-32 h-32 opacity-80"
          style={{ rotate: 15 }}
          animate={{
            y: [0, -15, 0],
            x: [0, 10, 0],
            rotate: [15, 20, 15]
          }}
          transition={{
            duration: 4,
            repeat: Infinity,
            repeatType: "reverse"
          }}
        >
          <svg viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2C7.59 2 4 5.59 4 10C4 13.91 6.72 17.14 10.39 17.85C10.25 18.23 10 18.93 10 19.5C10 20.88 11.12 22 12.5 22C13.88 22 15 20.88 15 19.5C15 18.93 14.75 18.23 14.61 17.85C18.28 17.14 21 13.91 21 10C21 5.59 17.41 2 13 2H12ZM12 4C15.33 4 18 6.67 18 10C18 13.33 15.33 16 12 16C8.67 16 6 13.33 6 10C6 6.67 8.67 4 12 4ZM7 7.5C6.17 7.5 5.5 8.17 5.5 9C5.5 9.83 6.17 10.5 7 10.5C7.83 10.5 8.5 9.83 8.5 9C8.5 8.17 7.83 7.5 7 7.5ZM17 7.5C16.17 7.5 15.5 8.17 15.5 9C15.5 9.83 16.17 10.5 17 10.5C17.83 10.5 18.5 9.83 18.5 9C18.5 8.17 17.83 7.5 17 7.5Z" />
          </svg>
        </motion.div>
      </div>
    </div>
  );
} 
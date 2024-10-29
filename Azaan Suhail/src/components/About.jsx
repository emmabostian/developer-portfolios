import React, { useRef } from "react";
import { Icon } from "@iconify/react";
import { motion, useInView } from "framer-motion";

const About = () => {
  const technologies = [
    { icon: "skill-icons:react-dark", label: "React" },
    { icon: "skill-icons:tailwindcss-light", label: "Tailwind CSS" },
    { icon: "vscode-icons:file-type-node", label: "Node.js" },
    { icon: "simple-icons:express", label: "Express" },
    { icon: "skill-icons:javascript", label: "JavaScript" },
    { icon: "logos:mysql", label: "MySQL" },
    { icon: "devicon:mongodb-wordmark", label: "MongoDB" },
    { icon: "skill-icons:html", label: "HTML" },
    { icon: "skill-icons:css", label: "CSS" },
    { icon: "devicon:bootstrap", label: "Bootstrap" },
    { icon: "logos:material-ui", label: "Material UI" },
    { icon: "fa6-brands:shoelace", label: "Shoelace" },
    { icon: "simple-icons:shadcnui", label: "ShadCN UI" },
    { icon: "devicon:postman", label: "Postman" },
    { icon: "devicon-plain:reactrouter", label: "React Router" },
    { icon: "skill-icons:threejs-light", label: "Three.js" },
    { icon: "skill-icons:figma-light", label: "Figma" },
    { icon: "devicon:git", label: "Git" },
    { icon: "skill-icons:github-light", label: "GitHub" },
    { icon: "mdi:language-c", label: "C" },
    { icon: "devicon:java-wordmark", label: "Java" },
    { icon: "skill-icons:python-dark", label: "Python" },
    { icon: "logos:pycharm", label: "PyCharm" },
    { icon: "logos:intellij-idea", label: "IntelliJ" },
    { icon: "vscode-icons:file-type-vscode", label: "VS Code" },
    { icon: "logos:numpy", label: "NumPy" },
    { icon: "logos:matplotlib-icon", label: "Matplotlib" },
    { icon: "skill-icons:scikitlearn-light", label: "Scikit-learn" }
  ];

  return (
    <div className="m-2 mb-0 bg-[#E9F1F2] flex flex-col gap-2 pt-3">
      <div className="about px-[2em] flex flex-col">
        <h1 className="text-3xl font-semibold font-robotoCondensed">
          A Bit About Me
        </h1>
        <p className="m-2 mt-0">
          I’m Azaan Suhail, a final-year Computer Science undergraduate
          passionate about web development and problem-solving. With experience
          in MERN full-stack development, I enjoy building dynamic and
          responsive applications. I'm always open to collaborating on
          innovative projects and bringing creative ideas to life. Additionally,
          I'm a Data Structures and Algorithms (DSA) enthusiast who loves the
          thrill of solving complex problems. Let’s connect and create something
          amazing together!
        </p>
      </div>

      <div className="tool-technologies px-[2em] flex flex-col">
        <h1 className="text-3xl font-semibold pb-[2px] font-robotoCondensed">
          Tools and technologies
        </h1>
        <p className="px-[14px]">
          I use a variety of tools and technologies to build responsive,
          efficient, and scalable web applications. From coding languages to
          development frameworks, these are the key components I rely on to
          create great user experiences.
        </p>

        <motion.div className="iconsdiv flex gap-[1vw] flex-wrap justify-evenly pt-1">
          {technologies.map((tech, index) => {

            const ref = useRef(null);
            const isInView = useInView(ref, {
              triggerOnce: false, 
            });

            return (
              <motion.div
                key={index}
                ref={ref}
                initial={{ opacity: 0, y: 50 }}
                animate={
                  isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 50 }
                }
                transition={{ duration: .3, delay: index * 0.05 }} 
                className="flex gap-[1em] justify-center items-center"
              >
                <Icon icon={tech.icon} width="36" height="64" />
                <h1 className="text-[1em]">{tech.label}</h1>
              </motion.div>
            );
          })}
        </motion.div>
      </div>

      <div className="coding Profile ml-1 pb-3">
        <h1 className="text-3xl font-semibold px-[2rem] font-robotoCondensed">
          Coding Profiles
        </h1>
        <h1 className="px-[2.5rem] pt-2">
          Solved <b>700+</b> DSA problems across all coding platforms.
        </h1>
        <div className="button pl-[4rem] pt-4 ">
          <a
            href="https://codolio.com/profile/Azaan%20Suhail"
            target="_blank"
            rel="noopener noreferrer"
          >
            <button
              type="button"
              className="text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2"
            >
              All Coding Profiles
            </button>
          </a>
          <a
            href="https://leetcode.com/u/AzaanSuhail/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <button
              type="button"
              className="text-black bg-gradient-to-r from-teal-200 to-lime-200 hover:bg-gradient-to-l hover:from-teal-200 hover:to-lime-200 focus:ring-4 focus:outline-none focus:ring-lime-200 dark:focus:ring-teal-700 font-bold rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2"
            >
              LeetCode
            </button>
          </a>
        </div>
      </div>
    </div>
  );
};

export default About;

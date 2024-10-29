import React from "react";
import programmerImg from "../assets/Programmer_Img.png";
import programmer2 from "../assets/Programmer2.jpg";
import instagramIcon from "../assets/instagram.png";
import linkedinIcon from "../assets/linkedin.png";
import githubIcon from "../assets/github.png";
import image from "../assets/cartoon_img.png";
import Typical from "react-typical";

const Home = () => {
  return (
    <div className="flex flex-col lg:flex-row-reverse items-center justify-center w-full h-full lg:px-10">
      <div className="image w-full lg:w-1/2 flex justify-center lg:justify-start">
        <img
          src={programmer2}
          alt="image"
          className="w-[90%] lg:w-[80%] max-w-[400px] lg:max-w-[600px]"
        />
      </div>

      <div className="main flex flex-col items-center lg:items-start w-full lg:w-1/2 px-5 lg:px-10">
        <div className="pl-0 lg:pl-[10vw] flex justify-center lg:justify-start">
          <img
            src={image}
            alt="Programmer"
            className="w-[30vw] lg:w-[8vw] max-w-[200px]"
          />
        </div>

        <div className="Software-heading text-center lg:text-left mt-4 lg:mt-6">
          <h1 className="text-[6vw] lg:text-[3vw] font-poppins">
            Hi, I am Azaan Suhail&nbsp;
          </h1>

          <div className="min-h-[3vw] lg:min-h-[1.5vw]">
            <Typical
              steps={[
                "MERN Stack Developer",
                3000,
                "Full Stack Developer",
                3000,
                "A.I & Machine Learning Visionary",
                3000,
                "DSA Enthusiast",
                3000,
                "Learner",
                3000,
                "Coding Enthusiast",
                300
              ]}
              loop={Infinity}
              wrapper="p"
              className="inline-block text-[#64fcd9] text-[6vw] lg:text-[2vw] font-semibold"
            />
          </div>
        </div>

        <div className="icons flex gap-[2vw] mt-4 justify-center lg:justify-start">
          <a
            href="https://github.com/AzaanSuhail"
            target="_blank"
            rel="noopener noreferrer"
          >
            <button>
              <img
                src={githubIcon}
                alt="Github"
                className="w-[8vw] lg:w-[2.5vw] max-w-[50px]"
              />
            </button>
          </a>

          <a
            href="https://www.linkedin.com/in/azaan-suhail-272230239/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <button>
              <img
                src={linkedinIcon}
                alt="LinkedIn"
                className="w-[8vw] lg:w-[2.5vw] max-w-[50px]"
              />
            </button>
          </a>

          <a
            href="https://www.instagram.com/azaansuhail/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <button>
              <img
                src={instagramIcon}
                alt="Instagram"
                className="w-[8vw] lg:w-[2.5vw] max-w-[50px]"
              />
            </button>
          </a>
        </div>

        <div className="Resume mt-4 flex justify-center lg:justify-start">
          <a
            href="https://drive.google.com/file/d/1k2gDdiirtereXS8YtYHD5tiIp43U7s8j/view?usp=sharing"
            target="_blank"
          >
            <button className="bg-[#64FCD9] font-bold px-8 py-2 lg:px-[2em] lg:py-[.4em] border rounded-md">
              Resume
            </button>
          </a>
        </div>
      </div>
    </div>
  );
};

export default Home;

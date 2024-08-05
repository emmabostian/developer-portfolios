import React, { useState } from "react";
import Navbar from "./components/Navbar";
import animation from "./components/rocket.json";
import Lottie from "lottie-react";
import Name from "./components/name";
import Resume from "./components/resume";
import SocialMedia from "./components/socials";
import About from "./components/about";
import Skills from "./components/skills";
import ContactForm from "./components/contact";

function App() {
  const [activeComponent, setActiveComponent] = useState("home");

  const handleButtonClick = (buttonName) => {
    setActiveComponent(buttonName.toLowerCase());
  };


  return (
    <div>
      <Navbar onButtonClick={handleButtonClick} className="pb-6 sm:pb-12 md:pb-16"/>
      {activeComponent === "home" && (
        <div className="lg:flex justify-center items-center flex-row flex-wrap sm:mt-12 md:mt-0">
          <div className="lg:w-1/2 sm:w-full md:w-full pl-10 sm:pl-10 md:pl-14 ">
            <Name className="mt-4 sm:mt-8 md:mt-12" />
          </div>
          <div className="lg:w-1/2 sm:w-full md:w-full hidden lg:block">  
            <Lottie 
              className="max-w-xs mx-auto"
              loop={true} 
              animationData={animation} 
            />
          </div>
          <Resume/>
          <SocialMedia/>
        </div>
      )}
      {activeComponent === "about" && <About/>}
      {activeComponent === "skills" && <Skills/>}
      {activeComponent === "contact" && <ContactForm/>}
    </div>
  );
}

export default App;
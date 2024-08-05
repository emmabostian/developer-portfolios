import React from "react";
import "./Navbar.css";

const Navbar = ({ onButtonClick }) => {
  return (
    <div className="flex justify-center items-center h-24 max-w-[1240px] mx-auto px-4 text-white mt-0">
      <ul className="flex flex-row flex-wrap justify-center gap-1 md:gap-2 lg:gap-4">
        <li className="p-2 md:p-4 font-normal text-xm md:text-xm lg:text-xl font-serif hover: transition duration-300 ease-in-out ">
          <button onClick={() => onButtonClick("Home")} className="nav-link">
            Home
          </button>
        </li>
        <li className="p-2 md:p-4 font-normal text-xm md:text-xm lg:text-xl font-serif hover: transition duration-300 ease-in-out">
          <button onClick={() => onButtonClick("about")} className="nav-link">
            About
          </button>
        </li>
        <li className="p-2 md:p-4 font-normal text-xm md:text-xm lg:text-xl font-serif hover: transition duration-300 ease-in-out">
          <button onClick={() => onButtonClick("Skills")} className="nav-link">
            Skills
          </button>
        </li>
        <li className="p-2 md:p-4 font-normal text-xm md:text-xm lg:text-xl font-serif hover: transition duration-300 ease-in-out">
          <button onClick={() => onButtonClick("Contact")} className="nav-link">
            Contact
          </button>
        </li>
      </ul>
    </div>
  );
};

export default Navbar;
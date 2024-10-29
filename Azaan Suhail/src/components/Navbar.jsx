import React, { useState } from "react";
import { Sling as Hamburger } from "hamburger-react";
import { Link } from "react-scroll"; 
const Navbar = () => {
  const [isOpen, setOpen] = useState(false);

  return (
    <div className="flex justify-between items-center w-full lg:h-[60px] sm:h-[42px] md:h-[55px] bg-black text-white px-4 relative">
      <div className="name hidden md:block">
        <h1 className="font-majorMono text-[2vw] lg:pl-28 md:pl-15">
          Azaan Suhail
        </h1>
      </div>

      <div className="block md:hidden ml-auto relative">
        <Hamburger className="sm" toggled={isOpen} toggle={setOpen} color="#64FCD9" />
        {/* <Hamburger
          style={{ "width": "10px", "height": "15px" }} 
          toggled={isOpen}
          toggle={setOpen}
          color="#64FCD9"
        /> */}

        <div
          className={`buttons absolute right-0 z-10 bg-black mt-1 rounded-md shadow-lg ${
            isOpen ? "flex" : "hidden"
          } flex-col gap-[0.5em] p-2 min-w-[95px]`}
          style={{ top: "100%", right: "0" }}
        >
          <Link to="home" smooth={true} duration={500}>
            <button className="btn btn-home bg-[#64FCD9] text-black font-bold px-2 py-0.5 border-black rounded-md text-xs">
              Home
            </button>
          </Link>
          <Link to="about" smooth={true} duration={500}>
            <button className="btn btn-about hover:bg-[#64FCD9] bg-white text-black font-normal hover:font-semibold px-2 py-0.5 border-black rounded-md text-xs">
              About
            </button>
          </Link>
          <Link to="projects" smooth={true} duration={500}>
            <button className="btn btn-project hover:bg-[#64FCD9] bg-white text-black font-normal hover:font-semibold px-2 py-0.5 border-black rounded-md text-xs">
              Projects
            </button>
          </Link>
          <Link to="experience" smooth={true} duration={500}>
            <button className="btn btn-experience hover:bg-[#64FCD9] bg-white text-black font-normal hover:font-semibold px-2 py-0.5 border-black rounded-md text-xs">
              Experience
            </button>
          </Link>
          <Link to="contact" smooth={true} duration={500}>
            <button className="btn btn-contact hover:bg-[#64FCD9] bg-white text-black font-normal hover:font-semibold px-2 py-0.5 border-black rounded-md text-xs">
              Contact Me
            </button>
          </Link>
        </div>
      </div>

      <div className="hidden md:flex gap-[1em] font-poppins">
        <Link to="home" smooth={true} duration={500}>
          <button className="btn btn-home bg-[#64FCD9] text-black font-bold px-4 py-2 border-black rounded-md">
            Home
          </button>
        </Link>
        <Link to="about" smooth={true} duration={500}>
          <button className="btn btn-about hover:bg-[#64FCD9] bg-white text-black font-normal hover:font-semibold px-4 py-2 border-black rounded-md">
            About
          </button>
        </Link>
        <Link to="projects" smooth={true} duration={500}>
          <button className="btn btn-project hover:bg-[#64FCD9] bg-white text-black font-normal hover:font-semibold px-4 py-2 border-black rounded-md">
            Projects
          </button>
        </Link>
        <Link to="experience" smooth={true} duration={500}>
          <button className="btn btn-experience hover:bg-[#64FCD9] bg-white text-black font-normal hover:font-semibold px-4 py-2 border-black rounded-md">
            Experience
          </button>
        </Link>
        <Link to="contact" smooth={true} duration={500}>
          <button className="btn btn-contact hover:bg-[#64FCD9] bg-white text-black font-normal hover:font-semibold px-4 py-2 border-black rounded-md">
            Contact Me
          </button>
        </Link>
      </div>

      <div className="name md:hidden absolute left-1/2 transform -translate-x-1/2">
        <h1 className="font-majorMono text-[5vw]">Azaan Suhail</h1>
      </div>
    </div>
  );
};

export default Navbar;

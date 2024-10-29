import React from "react";
import { TaggedContentCard } from "react-ui-cards";

const Project = () => {
  return (
    <>
      <h1 className="text-3xl font-extrabold px-[1.4em] font-robotoCondensed md:relative md:top-2 lg:relative lg:top-2">
        Projects
      </h1>

      <div className="main-div flex flex-wrap justify-around gap-[1px] relative right-8 sm:gap-3 sm:w-full ">
        {/* Card 1 */}
        <div
          className="card text-white p-2 rounded-lg"
          style={{ width: "220px", height: "350px", paddingBottom: "23rem" }}
        >
          <TaggedContentCard
            style={{ backgroundColor: "black", color: "white", height: "100%" }}
            title={<span className="text-[#64fcd8] font-bold">Chat Loop</span>}
            description="Built a full-stack MERN messaging app with real-time Socket.io communication, online status, pop sound alerts, JWT authentication, bcrypt-secured passwords, React, Tailwind CSS, daisyUI, Zustand for state, Express/MongoDB for data handling, and efficient backend operations."
            tags={[
              <button
                className="bg-[#64fcd9] text-black px-3 py-1 rounded-md hover:font-semibold mb-0" // Removed margin-bottom
                onClick={() =>
                  window.open(
                    "https://github.com/AzaanSuhail/Chat_Loop",
                    "_blank"
                  )
                }
              >
                GitHub
              </button>,
              <button
                className="bg-[#64fcd9] text-black px-3 py-1 rounded-md hover:font-semibold mb-0" // Removed margin-bottom
                onClick={() =>
                  window.open("https://loop-chat-azaan.onrender.com", "_blank")
                }
              >
                LiveLink
              </button>
            ]}
          />
        </div>

        {/* Card 2 */}
        <div
          className="card text-white p-2 rounded-lg"
          style={{ width: "220px", height: "350px", paddingBottom: "23rem" }}
        >
          <TaggedContentCard
            style={{ backgroundColor: "black", color: "white", height: "100%" }}
            title={<span className="text-[#64fcd9] font-bold">ShieldOP</span>}
            description="Developed a secure password manager using the MERN stack with CRUD functionality, securely storing encrypted passwords in MongoDB. Integrated Tailwind CSS, animated Lord Icons, uuid for unique IDs, and React Toast for real-time notifications and user-friendly interface"
            tags={[
              <button
                className="bg-[#64fcd9] text-black px-3 py-1 rounded-md hover:font-semibold mb-0" // Removed margin-bottom
                onClick={() =>
                  window.open(
                    "https://github.com/AzaanSuhail/ShieldOP-My-Own-Password-Manager",
                    "_blank"
                  )
                }
              >
                GitHub
              </button>,
              <button
                className="bg-[#64fcd9] text-black px-3 py-1 rounded-md hover:font-semibold mb-0" // Removed margin-bottom
                onClick={() =>
                  window.open(
                    "https://dochub.com/azaan-suhail/gzdnE7NwJxBva21KQyW3BJ/shieldop-png",
                    "_blank"
                  )
                }
              >
                LiveUI
              </button>
            ]}
          />
        </div>

        {/* //TOdo : third card */}
        <div
          className="card text-white p-2 rounded-lg"
          style={{ width: "220px", height: "350px", paddingBottom: "23rem" }}
        >
          <TaggedContentCard
            style={{ backgroundColor: "black", color: "white", height: "100%" }}
            title={
              <span className="text-[#64fcd9] font-bold">Commits Hub</span>
            }
            description="Commits Hub is a dynamic MERN app for exploring GitHub profiles and managing repositories. Users can search profiles, sort repositories by recency, stars, or forks, and like profiles, with secure OAuth access to top repositories in JavaScript, Python, and more languages"
            tags={[
              <button
                className="bg-[#64fcd9] text-black px-3 py-1 rounded-md hover:font-semibold mb-0" // Removed margin-bottom
                onClick={() =>
                  window.open(
                    "https://github.com/AzaanSuhail/Commits-Hub/tree/main",
                    "_blank"
                  )
                }
              >
                GitHub
              </button>,
              <button
                className="bg-[#64fcd9] text-black px-3 py-1 rounded-md hover:font-semibold mb-0" // Removed margin-bottom
                onClick={() =>
                  window.open(
                    "https://commit-hub.onrender.com/",
                    "_blank"
                  )
                }
              >
                LiveLink
              </button>
            ]}
          />
        </div>

        {/* Card 3 */}
        <div
          className="card text-white p-2 rounded-lg"
          style={{ width: "220px", height: "350px", paddingBottom: "23rem" }}
        >
          <TaggedContentCard
            style={{ backgroundColor: "black", color: "white", height: "100%" }}
            title={
              <span className="text-[#64fcd9] font-bold ">
                AI Desktop Voice Assistant
              </span>
            }
            description="AI Desktop Voice Assistant: Developed a voice-activated assistant that recognizes and executes commands, including opening websites (Google, Stack Overflow), retrieving Wikipedia summaries, announcing the current time, and launching local applications. "
            tags={[
              <button
                className="bg-[#64fcd9] text-black px-3 py-1 rounded-md hover:font-semibold mb-0" // Removed margin-bottom
                onClick={() =>
                  window.open(
                    "https://github.com/AzaanSuhail/AI-Desktop-Voice-Assistant",
                    "_blank"
                  )
                }
              >
                GitHub
              </button>,
              <button
                className="bg-[#64fcd9] text-black px-3 py-1 rounded-md hover:font-semibold mb-0" // Removed margin-bottom
                onClick={() =>
                  window.open("https://example.com/live3", "_blank")
                }
              >
                Live
              </button>
            ]}
          />
        </div>

        {/* Card 4 */}
        <div
          className="card text-white p-2 rounded-lg"
          style={{ width: "220px", height: "350px", paddingBottom: "23rem" }}
        >
          <TaggedContentCard
            style={{ backgroundColor: "black", color: "white", height: "100%" }}
            title={
              <span className="text-[#64fcd9] font-bold">
                Real time Weather App
              </span>
            }
            description="Developed a real-time weather application that provides users with instant weather updates, including current temperature, conditions (e.g., sunny, rainy), and humidity levels. The app fetches data from a reliable weather API, ensuring accurate and up-to-date information. "
            tags={[
              <button
                className="bg-[#64fcd9] text-black px-3 py-1 rounded-md hover:font-semibold mb-0" // Removed margin-bottom
                onClick={() =>
                  window.open(
                    "https://github.com/AzaanSuhail/My-Weather-App",
                    "_blank"
                  )
                }
              >
                GitHub
              </button>,
              <button
                className="bg-[#64fcd9] text-black px-3 py-1 rounded-md hover:font-semibold mb-0" // Removed margin-bottom
                onClick={() =>
                  window.open(
                    "https://github.com/AzaanSuhail/My-Weather-App",
                    "_blank"
                  )
                }
              >
                LiveUI
              </button>
            ]}
          />
        </div>
      </div>
    </>
  );
};

export default Project;

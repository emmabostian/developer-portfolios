import React from "react";
import MastodonLogo from "./images/mastodon.png";
import InstagramLogo from "./images/insta.png";
import TwitterLogo from "./images/x.png";
import LinkedInLogo from "./images/linkedin.png";
import GithubLogo from "./images/github.png";
import PinterestLogo from "./images/pinterest.png";

const SocialMedia = () => {
  return (
    <div className="flex justify-center mb-10 mt-10">
      <div className="lg:grid lg:grid-cols-6 lg:justify-items-end gap-0.5 md:gap-1 lg:gap-2 xl:gap-2">
        <button
          className="text-white font-bold py-2 px-4 rounded hover:scale-110 transition duration-300"
          onClick={() => window.open("https://mastodon.social/@captain_obvious", "_blank")}
        >
          <img src={MastodonLogo} alt="Mastodon Logo" className="w-6 h-6 sm:w-8 sm:h-8 md:w-10 md:h-10 lg:w-8 lg:h-8 xl:w-8 xl:h-8" />
        </button>
        <button
          className="text-white font-bold py-2 px-4 rounded hover:scale-110 transition duration-300"
          onClick={() => window.open("https://instagram.com/thegraffiti.mind/", "_blank")}
        >
          <img src={InstagramLogo} alt="Instagram Logo" className="w-6 h-6 sm:w-8 sm:h-8 md:w-10 md:h-10 lg:w-8 lg:h-8 xl:w-8 xl:h-8" />
        </button>
        <button
          className="text-white font-bold py-2 px-4 rounded hover:scale-110 transition duration-300"
          onClick={() => window.open("https://x.com/not_average_x", "_blank")}
        >
          <img src={TwitterLogo} alt="Twitter Logo" className="w-6 h-6 sm:w-8 sm:h-8 md:w-10 md:h-10 lg:w-8 lg:h-8 xl:w-8 xl:h-8" />
        </button>
        <button
          className="text-white font-bold py-2 px-4 rounded hover:scale-110 transition duration-300"
          onClick={() => window.open("https://www.linkedin.com/in/ananya-biswas-kiit/", "_blank")}
        >
          <img src={LinkedInLogo} alt="LinkedIn Logo" className="w-6 h-6 sm:w-8 sm:h-8 md:w-10 md:h-10 lg:w-8 lg:h-8 xl:w-8 xl:h-8" />
        </button>
        <button
          className="text-white font-bold py-2 px-4 rounded hover:scale-110 transition duration-300"
          onClick={() => window.open("https://github.com/ananyab1909", "_blank")}
        >
          <img src={GithubLogo} alt="Github Logo" className="w-6 h-6 sm:w-8 sm:h-8 md:w-10 md:h-10 lg:w-8 lg:h-8 xl:w-8 xl:h-8" />
        </button>
        <button
          className="text-white font-bold py-2 px-4 rounded hover:scale-110 transition duration-300"
          onClick={() => window.open("https://in.pinterest.com/bananya1909/", "_blank")}
        >
          <img src={PinterestLogo} alt="Pinterest Logo" className="w-6 h-6 sm:w-8 sm:h-8 md:w-10 md:h-10 lg:w-8 lg:h-8 xl:w-8 xl:h-8" />
        </button>
      </div>
    </div>
  );
};

export default SocialMedia;
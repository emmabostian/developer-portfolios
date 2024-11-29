import React from "react";
import AOS from "aos";
import "aos/dist/aos.css";
import styled from "styled-components";
import ParticlesComponent from "../partcles";

const HomeContainer = styled.div`
  height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

const Name = styled.h1`
  font-size: 10rem;
  font-weight: bold;
  color: #3ccf91;
  text-align: center;

  letter-spacing: 2px;
  font-family: "Londrina Shadow";

  @media (max-width: 600px) {
    font-size: 3rem;
  }

  @media (min-width: 600px) and (max-width: 1000px) {
    font-size: 5rem;
  }
`;

const SkillText = styled.h2`
  font-size: 5rem;
  color: #3ccf91;
  font-weight: bold;
  text-align: center;
  font-family: "Londrina Shadow";
  letter-spacing: 2px;

  @media (max-width: 600px) {
    font-size: 3rem;
  }

  @media (min-width: 600px) and (max-width: 1000px) {
    font-size: 4rem;
  }
`;

const AboutText = styled.h2`
  color: white;
  font-size: 5rem;
  text-align: center;
  letter-spacing: 2px;
  font-family: "Londrina Shadow";

  @media (max-width: 600px) {
    font-size: 2rem;
  }

  @media (min-width: 600px) and (max-width: 1000px) {
    font-size: 3rem;
  }
`;

const MainContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  row-gap: 1rem;
`;

const Home = () => {
  AOS.init();

  return (
    <>
      <HomeContainer id="home">
        <ParticlesComponent id="particles" />
        <MainContainer>
          <Name
            data-aos="fade-up"
            data-aos-duration="1500"
            data-aos-delay="800"
          >
            Vignesh Pugazhenthi
          </Name>
          <AboutText
            data-aos="fade-up"
            data-aos-duration="1500"
            data-aos-delay="1200"
          >
            Full Stack Developer who likes building stuff for
          </AboutText>
          <SkillText
            data-aos="fade-up"
            data-aos-duration="1500"
            data-aos-delay="1500"
          >
            Web
          </SkillText>
        </MainContainer>
      </HomeContainer>
    </>
  );
};

export default Home;

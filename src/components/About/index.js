import React from "react";
import {
  AboutContainer,
  LeftContainer,
  RightContainer,
  Title,
  Text,
  Highlight,
  SubTitle,
  SkillContainer,
  SkillList,
  SkillListItem,
  SkillImage,
  SkillName,
  ExperienceTitle,
  Experience,
  ExperienceHeading,
  ExperienceText,
  ExperienceText2,
} from "./style";

const About = () => {
  return (
    <>
      <AboutContainer id="about">
        <LeftContainer>
          <Title
            data-aos="zoom-in"
            data-aos-duration="1500"
            data-aos-delay="300"
          >
            About
          </Title>
          <Text
            data-aos="zoom-in-right"
            data-aos-duration="1500"
            data-aos-delay="600"
          >
            I am a passionate <Highlight>software developer</Highlight>{" "}
            specializing in the <Highlight>MERN stack</Highlight>, with a strong
            emphasis on <Highlight>frontend development</Highlight>.I am
            dedicated to continuously learning and refining my skills to create
            engaging digital experiences that meet both user needs and business
            objectives.
          </Text>
          <ExperienceTitle
            data-aos="zoom-in-right"
            data-aos-duration="1000"
            data-aos-delay="800"
          >
            Experience
          </ExperienceTitle>
          <Experience
            data-aos="zoom-in-left"
            data-aos-duration="1000"
            data-aos-delay="1000"
          >
            <ExperienceHeading>Frontend Engineer Intern</ExperienceHeading>
            <ExperienceText>CodTech IT Solution</ExperienceText>
            <ExperienceText2>March 2024 – Present</ExperienceText2>
          </Experience>
          <Experience
            data-aos="zoom-in-left"
            data-aos-duration="1000"
            data-aos-delay="1100"
          >
            <ExperienceHeading>
              MERN Stack Development Program
            </ExperienceHeading>
            <ExperienceText>NxTWave Academy</ExperienceText>
            <ExperienceText2>Aug 2023 – October 2024 </ExperienceText2>
          </Experience>
        </LeftContainer>
        <RightContainer>
          <SubTitle
            data-aos="zoom-in"
            data-aos-duration="1500"
            data-aos-delay="100"
          >
            Skills
          </SubTitle>
          <SkillContainer>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="200"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/tgsCK0QC/python.png" />
              </SkillListItem>
              <SkillName>Python</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="300"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/x1hWJ48c/js.png" />
              </SkillListItem>
              <SkillName>JavaScript</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="500"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/L6YsrGcs/physics.png" />
              </SkillListItem>
              <SkillName>React</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="400"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/t4FFHsK7/html-5.png" />
              </SkillListItem>
              <SkillName>Html5</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="500"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/tCcHHT30/css-3.png" />
              </SkillListItem>
              <SkillName>Css3</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="600"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/wTw4CGd7/nodejs.png" />
              </SkillListItem>
              <SkillName>NodeJS</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="700"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/GtP33sCh/Express.png" />
              </SkillListItem>
              <SkillName>ExpressJS</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="800"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/g0GVGvbr/MongoDB.png" />
              </SkillListItem>
              <SkillName>MongoDB</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="900"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/Qx09cv2N/SQLite.png" />
              </SkillListItem>
              <SkillName>Sqlite</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="1000"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/cLWW4J9r/MySQL.png" />
              </SkillListItem>
              <SkillName>MySQL</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="1100"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/sDyHMZzd/Redux.png" />
              </SkillListItem>
              <SkillName>Redux</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="1200"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/rpcwbjXZ/Git.png" />
              </SkillListItem>
              <SkillName>Git</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="1300"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/CLz7BC22/GitHub.png" />
              </SkillListItem>
              <SkillName>GitHub</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="1500"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/m2mrqC2T/Bootstrap.png" />
              </SkillListItem>
              <SkillName>Bootstrap</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="1600"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/26WsdR31/Sass.png" />
              </SkillListItem>
              <SkillName>Sass</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="1700"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/d0Pm7bMH/Tailwind-CSS.png" />
              </SkillListItem>
              <SkillName>TailWind</SkillName>
            </SkillList>
            <SkillList
              data-aos="fade-down"
              data-aos-duration="1000"
              data-aos-delay="1800"
            >
              <SkillListItem>
                <SkillImage src="https://i.postimg.cc/9XKb9877/Figma.png" />
              </SkillListItem>
              <SkillName>Figma</SkillName>
            </SkillList>
          </SkillContainer>
        </RightContainer>
      </AboutContainer>
    </>
  );
};

export default About;

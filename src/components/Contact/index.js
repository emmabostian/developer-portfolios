import React from "react";
import styled from "styled-components";
import { IoDocumentTextSharp } from "react-icons/io5";
import { FaGithub } from "react-icons/fa";

const ContactContainer = styled.div`
  height: 100vh;
  /* background-color: black; */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

const Title = styled.h1`
  color: white;
  font-size: 8rem;
  text-align: center;
  margin-bottom: 1rem;

  @media (max-width: 768px) {
    font-size: 4rem;
  }
`;

const Text = styled.p`
  color: #8f9094;
  font-size: 2rem;
  text-align: center;

  @media (max-width: 768px) {
    font-size: 1.8rem;
  }
`;

const LinkContainer = styled.div`
  display: flex;
  align-items: center;
  margin-top: 5rem;
  column-gap: 2rem;

  @media (max-width: 768px) {
    column-gap: 1rem;
  }
`;

const LinkItem = styled.div`
  display: flex;
  align-items: center;
  column-gap: 1rem;
`;

const GithubIcon = styled(FaGithub)`
  color: #3ccf91;
  font-size: 2.5rem;

  @media (max-width: 768px) {
    font-size: 1.5rem;
  }
`;

const ResumeIcon = styled(IoDocumentTextSharp)`
  color: #3ccf91;
  font-size: 2.5rem;

  @media (max-width: 768px) {
    font-size: 1.5rem;
  }
`;

const SubText = styled.p`
  color: #ffffff;
  font-size: 2rem;

  @media (max-width: 768px) {
    font-size: 1.5rem;
  }
`;

const Footer = styled.div`
  background-color: black;
  width: 100%;
  padding-bottom: 2rem;
`;

const FooterText = styled(Text)`
  color: #8f9094;
  font-size: 1.5rem;

  @media (max-width: 500px) {
    font-size: 1rem;
  }
`;

const Highlight = styled.span`
  color: #3ccf91;
`;

const Contact = () => {
  return (
    <>
      <ContactContainer id="contact">
        <Title>Keep In Touch.</Title>
        <Text>
          Feel free to get in touch and talk more about your projects.
        </Text>
        <Text>seyoonpuvi@gmail.com</Text>

        <LinkContainer>
          <LinkItem>
            <GithubIcon />
            <SubText
              as="a"
              href="https://github.com/seyoonPuvi"
              target="_blank"
            >
              Github
            </SubText>
          </LinkItem>
          <LinkItem>
            <ResumeIcon />
            <SubText
              as="a"
              href="https://drive.google.com/file/d/1hwwHAGyvbGsliqXoHujYgnRhJ3tjlHlb/view?usp=sharing"
              target="_blank"
              download
            >
              Resume
            </SubText>
          </LinkItem>
        </LinkContainer>
      </ContactContainer>
      <Footer>
        <FooterText>
          Designed and Developed by <Highlight>Vignesh Pugazhenthi</Highlight>.
        </FooterText>
      </Footer>
    </>
  );
};

export default Contact;

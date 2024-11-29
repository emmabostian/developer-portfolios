import styled from "styled-components";

export const AboutContainer = styled.div`
  display: flex;
  overflow: hidden;
  @media (max-width: 768px) {
    flex-direction: column;
    width: 100%;
  }
`;

export const LeftContainer = styled.div`
  display: flex;
  flex-direction: column;
  padding: 5rem 2rem;

  @media (min-width: 768px) {
    width: 49%;
  }
`;

export const RightContainer = styled.div`
  background-color: rgb(237, 242, 248);
  display: flex;
  flex-direction: column;
  row-gap: 3rem;
  padding: 5rem 2rem;

  @media (min-width: 768px) {
    width: 50%;
  }
`;

export const Title = styled.h1`
  font-size: 12rem;
  color: #ffffff;
  font-family: "Catamaran", sans-serif;
  letter-spacing: 2px;

  @media (min-width: 768px) and (max-width: 1200px) {
    font-size: 8rem;
  }

  @media (max-width: 768px) {
    font-size: 5rem;
    text-align: center;
  }
`;

export const Text = styled.p`
  font-size: 2rem;
  color: #8f9094;
  line-height: 1.5;
`;

export const Highlight = styled.span`
  color: #3ccf91;
  font-weight: bold;
  text-transform: capitalize;
`;

export const SubTitle = styled(Title)`
  color: black;
  letter-spacing: 1px;
`;

export const SkillContainer = styled.ul`
  padding-inline-start: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 2rem 2rem;
`;

export const SkillList = styled.li`
  list-style: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  row-gap: 1rem;
`;

export const SkillListItem = styled.div`
  background-color: #ffffff;
  border-radius: 50%;
  height: 90px;
  width: 90px;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const SkillImage = styled.img`
  height: 50%;
  object-fit: contain;
  width: 50%;
`;

export const SkillName = styled.p`
  color: #6b7688;
  font-size: 1.8rem;
`;

export const ExperienceTitle = styled.h1`
  font-size: 4rem;
  color: white;
  font-family: "Oswald";
  font-weight: bold;
  letter-spacing: 2px;
  margin-top: 10rem;
`;

export const Experience = styled.div`
  display: flex;
  flex-direction: column;
  row-gap: 1rem;
  margin-top: 3rem;
`;

export const ExperienceHeading = styled.h2`
  color: #3ccf91;
  font-weight: bold;
  text-transform: capitalize;
  font-size: 2rem;
`;

export const ExperienceText = styled.p`
  font-size: 1.6rem;
  color: #8f9094;
`;

export const ExperienceText2 = styled(ExperienceText)`
  font-size: 1.2rem;
`;

import styled from "styled-components";

export const ProjectContainer = styled.div`
  min-height: 100vh;
  display: flex;
  flex-direction: row;
  overflow: hidden;

  @media (max-width: 768px) {
    flex-direction: column-reverse;
  }
`;

export const RightContainer = styled.div`
  display: flex;
  flex-direction: column;
  row-gap: 1rem;
  padding: 5rem 2rem;

  @media (min-width: 768px) {
    width: 50%;
    min-height: 100vh;
    row-gap: 5rem;
  }
`;

export const LeftContainer = styled.div`
  background-color: rgb(237, 242, 248);
  display: flex;
  flex-direction: column;
  row-gap: 3rem;
  padding: 5rem 1rem;
  @media (min-width: 768px) {
    width: 50%;
    min-height: 100vh;
  }
`;
export const ProjectInfoDetailsContainer = styled(LeftContainer)`
  width: 98%;
  row-gap: 1rem;
  padding: 2rem 1rem;
  @media (min-width: 768px) {
    height: 100vh;
    overflow-y: scroll;
  }

  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
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

export const CloseButton = styled.button`
  border: none;
  outline: none;
  font-size: 2rem;
  align-self: flex-end;
  background-color: rgb(237, 242, 248);
  cursor: pointer;
  &:hover {
    background-color: rgb(0, 0, 0);
  }
`;

export const ProjectTitle = styled.h1`
  font-size: 8rem;
  color: #000000;
  font-family: "Catamaran", sans-serif;
  letter-spacing: 2px;

  @media (max-width: 768px) {
    font-size: 3rem;
  }
`;

export const ProjectInfoOverview = styled.p`
  font-size: 2.5rem;
  font-family: "Oswald";
  letter-spacing: 1px;
  white-space: normal;
  word-break: normal;
  overflow-wrap: anywhere;
  line-height: 1.2;
  color: #000000;
  margin-bottom: 1rem;

  @media (max-width: 768px) {
    font-size: 2rem;
  }
`;

export const ProjectHighlights = styled.ul`
  display: flex;
  flex-direction: column;
  padding-inline-start: 0;
  row-gap: 1rem;
  margin-top: 4rem;
`;

export const ProjectHighlight = styled.li`
  display: flex;
  align-items: center;
  column-gap: 0.5rem;
  background-color: black;
  padding: 1rem 2rem;
  border-radius: 1rem;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
`;

export const HighlightName = styled.p`
  font-size: 1.8rem;
  color: #8f9094;
  font-weight: bold;
  font-family: "Catamaran", sans-serif;
`;

export const ProjectLinkContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-around;
  margin-top: 1rem;
`;

export const ProjectLive = styled.button`
  color: #000000;
  padding: 1rem 2rem;
  text-align: center;
  border-radius: 8px;
  border: 1px solid white;
  font-weight: bold;
  cursor: pointer;
  font-size: 2rem;
  font-family: "Catamaran", sans-serif;
  background-color: #ffffff;
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;

  &:hover {
    background-color: black;
    color: white;
  }
`;

export const GithubLink = styled(ProjectLive)``;

export const Heading = styled.h1`
  font-size: 10rem;
  font-family: "Oswald";
  letter-spacing: 1px;
  white-space: normal;
  word-break: normal;
  overflow-wrap: anywhere;
  line-height: 1.2;
  color: #8f9094;

  transition: all 0.45s ease-out;

  @media (min-width: 768px) and (max-width: 1200px) {
    font-size: 8rem;
  }

  @media (max-width: 768px) {
    font-size: 2.5rem;
    text-align: center;
  }
`;

export const ProjectTabContainer = styled.ul`
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  padding-inline-start: 0;
  gap: 1.5rem;
  margin-top: 5rem;
`;

export const ProjectTab = styled.li`
  list-style: none;
`;

export const TabButton = styled.button`
  background-color: ${(props) =>
    props.isActive === true ? "black" : "rgb(237, 242, 248)"};
  border: 1px solid black;
  outline: none;
  border-radius: 1.2rem;
  padding: 1rem;
  color: ${(props) => (props.isActive === false ? "black" : "white")};
  font-weight: bolder;
  cursor: pointer;
  transition: all 0.45s ease-out;

  width: 12rem;
`;

export const ProjectCardContainer = styled.ul`
  padding-inline-start: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  gap: 2rem 2rem;
  flex-wrap: wrap;
  margin-top: 5rem;
  position: relative;
  overflow: hidden;
`;

export const ProjectName = styled.h1`
  font-size: 2rem;
  color: #801515;
  font-family: "Catamaran", serif;
  font-weight: bold;
`;

export const ProjectCard = styled.li`
  background-color: rgb(237, 242, 248);
  list-style: none;
  padding: 2rem 1rem;
  border-radius: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  row-gap: 1.5rem;
  width: 20rem;
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  transition: all 0.45s ease-out;
  cursor: pointer;
  position: relative;

  &:hover {
    transform: scale(1.1);
    background-color: #ff3822;
  }

  &:hover ${ProjectName} {
    color: white;
  }
`;

export const ProjectImageCard = styled.img`
  height: 18rem;
  width: 100%;
  object-fit: contain;
  object-position: center;
  border-radius: 1rem;
`;

export const LoaderContainer = styled.div`
  height: 50rem;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const ProjectInfo = styled.div`
  text-align: center;
  display: flex;
  flex-direction: column;
`;

export const ProjectDesc = styled.p`
  font-size: 1.2rem;
  font-family: "Catamaran", seif;
  color: black;
  font-weight: bold;
`;

export const NoProject = styled.div`
  height: 50rem;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const Heading2 = styled(Heading)`
  color: black;
  text-align: center;
`;

import { React, useState, useEffect } from "react";
import { Grid } from "react-loader-spinner";
import { projectsList, TabList } from "../../utils/constant";
import {
  ProjectContainer,
  RightContainer,
  LeftContainer,
  ProjectInfoDetailsContainer,
  Title,
  CloseButton,
  ProjectTitle,
  ProjectInfoOverview,
  ProjectHighlights,
  ProjectHighlight,
  HighlightName,
  ProjectLinkContainer,
  ProjectLive,
  GithubLink,
  Heading,
  ProjectTabContainer,
  ProjectTab,
  TabButton,
  ProjectCardContainer,
  ProjectName,
  ProjectCard,
  ProjectImageCard,
  LoaderContainer,
  ProjectInfo,
  ProjectDesc,
  NoProject,
  Heading2,
} from "./style";

const Project = () => {
  const [projectInfo, setTab] = useState({
    activeTab: "webdesign",
    isLoading: true,
    ToDisplay: [],
  });
  const [projectInfoView, setProjectInfoView] = useState({
    showProjectInfoView: false,
    projectDetails: null,
  });

  useEffect(() => {
    const { activeTab } = projectInfo;
    const activeProjects = projectsList[activeTab];

    setTab((prev) => ({
      ...prev,
      activeTab,
      isLoading: false,
      ToDisplay: activeProjects,
    }));
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [projectInfo.activeTab, projectInfo.isLoading]);

  const onClickTab = (id) => {
    setTab((prev) => ({ ...prev, activeTab: id, isLoading: true }));
  };

  const onClickProject = (project) => {
    setProjectInfoView({
      showProjectInfoView: true,
      projectDetails: project,
    });
    const container = document.getElementById("leftContainer"); // Use the correct selector
    if (container) {
      container.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  };

  const onRenderLoader = () => (
    <LoaderContainer data-testid="loader">
      <Grid type="ThreeDots" color="white" height="50" width="50" />
    </LoaderContainer>
  );

  const onRenderProjectDetailsView = () => (
    <ProjectInfoDetailsContainer>
      <CloseButton
        onClick={() =>
          setProjectInfoView({
            showProjectInfoView: false,
            projectDetails: null,
          })
        }
      >
        ❌
      </CloseButton>
      <ProjectTitle>{projectInfoView.projectDetails.title}</ProjectTitle>
      <ProjectInfoOverview>
        {projectInfoView.projectDetails.projectOverview}
      </ProjectInfoOverview>
      <ProjectHighlights>
        <ProjectInfoOverview>Features:</ProjectInfoOverview>
        {projectInfoView.projectDetails.projectHighlights.map((each, index) => (
          <ProjectHighlight key={`${each} ${index}`}>
            <HighlightName>{each}</HighlightName>
          </ProjectHighlight>
        ))}
      </ProjectHighlights>

      <ProjectHighlights>
        <ProjectInfoOverview>Tech Stack:</ProjectInfoOverview>
        {projectInfoView.projectDetails.projectTechStack.map((each, index) => (
          <ProjectHighlight key={`${each} ${index}`}>
            <HighlightName>{each}</HighlightName>
          </ProjectHighlight>
        ))}
      </ProjectHighlights>
      <ProjectLinkContainer>
        <ProjectLive
          as="a"
          href={projectInfoView.projectDetails.link}
          target="_blank"
        >
          live🔎
        </ProjectLive>
        <GithubLink
          as="a"
          href={projectInfoView.projectDetails.githubLink}
          target="_blank"
        >
          Github🐱‍🏍
        </GithubLink>
      </ProjectLinkContainer>
    </ProjectInfoDetailsContainer>
  );

  const onRenderView = () => {
    if (projectInfo.isLoading) {
      return onRenderLoader();
    } else {
      if (projectInfo.ToDisplay.length !== 0) {
        return (
          <ProjectCardContainer>
            {projectInfo.ToDisplay.map((each) => (
              <ProjectCard
                data-aos="zoom-in"
                data-aos-duration="1500"
                data-aos-delay="300"
                onClick={() => onClickProject(each)}
              >
                <ProjectImageCard src={each.imageUrl} alt="image" />
                <ProjectInfo>
                  <ProjectName>{each.title}</ProjectName>
                  <ProjectDesc>{each.desc}</ProjectDesc>
                </ProjectInfo>
              </ProjectCard>
            ))}
          </ProjectCardContainer>
        );
      }
      return (
        <NoProject>
          <Heading2>Project Will Be Updated Soon</Heading2>
        </NoProject>
      );
    }
  };

  return (
    <ProjectContainer id="project">
      <LeftContainer id="leftContainer">
        {projectInfoView.showProjectInfoView ? (
          onRenderProjectDetailsView()
        ) : (
          <>
            <ProjectTabContainer>
              {TabList.map((each) => (
                <ProjectTab key={each.id}>
                  <TabButton
                    type="button"
                    onClick={() => onClickTab(each.id)}
                    isActive={projectInfo.activeTab === each.id}
                  >
                    {each.displayName}
                  </TabButton>
                </ProjectTab>
              ))}
            </ProjectTabContainer>
            {onRenderView()}{" "}
          </>
        )}
      </LeftContainer>
      <RightContainer>
        <Title data-aos="zoom-in" data-aos-duration="1500" data-aos-delay="300">
          PROJECTS
        </Title>
        <Heading
          data-aos="zoom-in-right"
          data-aos-duration="1500"
          data-aos-delay="600"
        >
          Here are some of my selected projects worth sharing.
        </Heading>
      </RightContainer>
    </ProjectContainer>
  );
};

export default Project;

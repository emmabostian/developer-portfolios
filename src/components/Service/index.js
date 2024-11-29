import React from "react";
import AOS from "aos";
import "aos/dist/aos.css";
import {
  ServiceContainer,
  LeftContainer,
  Title,
  Heading,
  ServiceCardContainer,
  ServiceCard,
  Image,
  CardHeading,
  CardDesc,
  CardListContainer,
  CardListItem,
  CardItemText,
} from "./style";
const Service = () => {
  AOS.init();
  return (
    <ServiceContainer id="service">
      <LeftContainer>
        <Title data-aos="zoom-in" data-aos-duration="1500" data-aos-delay="300">
          SERVICES
        </Title>
        <Heading
          data-aos="zoom-in-right"
          data-aos-duration="1500"
          data-aos-delay="600"
        >
          Code that solves problems,one product at a time
        </Heading>
      </LeftContainer>
      <ServiceCardContainer>
        <ServiceCard
          data-aos="fade-down"
          data-aos-easing="linear"
          data-aos-duration="1000"
        >
          <Image src="https://cdn.sanity.io/images/y1prohws/production/1ee2839d9f4f3d19a08d9160d4b464a3dcedfb25-70x65.svg" />
          <CardHeading>What I can do for you</CardHeading>
          <CardDesc>
            Deliver faster, better products that your users will love. Here are
            the services I provide
          </CardDesc>
          <CardListContainer>
            <CardListItem>
              <CardItemText>Design Strategy</CardItemText>
            </CardListItem>
            <CardListItem>
              <CardItemText>Front-end Development</CardItemText>
            </CardListItem>
            <CardListItem>
              <CardItemText>Back-end Development</CardItemText>
            </CardListItem>
            <CardListItem>
              <CardItemText>Fullstack Development</CardItemText>
            </CardListItem>
          </CardListContainer>
        </ServiceCard>
        <ServiceCard
          data-aos="fade-down"
          data-aos-easing="linear"
          data-aos-duration="1000"
        >
          <Image src="https://cdn.sanity.io/images/y1prohws/production/167e91631a7731d5a4301f798b8444131b08dad1-69x68.svg" />
          <CardHeading>What you can expect</CardHeading>
          <CardDesc>
            I design products that go beyond aesthetics—they're shippable and
            usable
          </CardDesc>
          <CardListContainer>
            <CardListItem>
              <CardItemText>Clean and Functional</CardItemText>
            </CardListItem>
            <CardListItem>
              <CardItemText>Device and User Friendly</CardItemText>
            </CardListItem>
            <CardListItem>
              <CardItemText>Efficient and Maintainable</CardItemText>
            </CardListItem>
          </CardListContainer>
        </ServiceCard>
      </ServiceCardContainer>
    </ServiceContainer>
  );
};

export default Service;

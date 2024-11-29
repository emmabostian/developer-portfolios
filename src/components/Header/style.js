import { styled, keyframes } from "styled-components";
import { GiHamburgerMenu } from "react-icons/gi";
import { AiOutlineClose } from "react-icons/ai";

// Keyframes for animations
const slideIn = keyframes`
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
`;

const slideOut = keyframes`
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(-100%);
  }
`;

export const NavbarContainer = styled.div`
  display: flex;
  height: 5rem;
  justify-content: center;
  align-items: center;
  padding: 1rem 0;
  width: 100%;
`;

export const Navbar = styled.div`
  width: 90%;
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

export const NavLogo = styled.h1`
  font-weight: bold;
  font-style: italic;
  color: #3ccf91;
  font-size: 5rem;
  font-family: "Londrina Shadow", sans-serif;
  cursor: pointer;
  transition: all 0.25s ease-in-out;

  &:hover {
    transform: scale(1.3);
  }

  @media (max-width: 600px) {
    font-size: 3rem;
  }
`;

export const NavItemsContainer = styled.ul`
  display: flex;
  align-items: center;
  column-gap: 2.5rem;
  padding-inline-start: 0;

  @media (max-width: 768px) {
    display: none;
  }
`;

export const NavItems = styled.a`
  list-style-type: none;
  text-decoration: none;
  color: white;
  font-size: 2rem;
  font-weight: bold;
  letter-spacing: 2px;
  font-family: "Londrina Shadow";
  cursor: pointer;
  transition: all 0.25s ease-in-out;

  &:hover {
    transform: scale(1.3);
  }
`;

export const HamburgerMenu = styled(GiHamburgerMenu)`
  font-size: 2rem;
  color: white;
  display: none;

  @media (max-width: 768px) {
    display: block;
    font-size: 3rem;
    z-index: 1001;
  }
`;

export const CloseIcon = styled(AiOutlineClose)`
  font-size: 2rem;
  color: white;
  display: none;
  z-index: 1000;

  position: fixed;
  top: 2rem;
  right: 2rem;

  @media (max-width: 768px) {
    display: block;
    font-size: 3rem;
  }
`;

export const MobNavContainer = styled.ul`
  height: 100%;
  width: 100vw;
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0;
  left: 0;
  align-items: stretch;
  padding-inline-start: 0;
  z-index: 100;
  background-color: rgba(0, 0, 0, 0.8);
`;

export const MobNavItems = styled.li`
  list-style-type: none;
  height: 20%;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: ${(props) => props.color};

  &.slide-in {
    animation: ${slideIn} ${(props) => props.duration} linear
      ${(props) => props.delay} both;
  }

  &.slide-out {
    animation: ${slideOut} ${(props) => props.duration} linear
      ${(props) => props.closeDelay} both;
  }
`;

export const MobNavLink = styled.a`
  text-decoration: none;
  color: white;
  font-size: 2rem;
  font-family: "Spicy Rice", serif;
  letter-spacing: 2px;
  transition: all 0.25s ease-in-out;
  cursor: pointer;

  &:hover {
    transform: scale(1.3);
  }
`;

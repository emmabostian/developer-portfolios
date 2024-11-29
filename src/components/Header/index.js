import { React, useState } from "react";
import AOS from "aos";
import "aos/dist/aos.css";
import {
  NavbarContainer,
  Navbar,
  NavLogo,
  NavItemsContainer,
  NavItems,
  HamburgerMenu,
  CloseIcon,
  MobNavContainer,
  MobNavItems,
  MobNavLink,
} from "./style";

const Header = () => {
  AOS.init();
  const [showMobNav, setShowMobNav] = useState(false);
  const [isClosing, setIsClosing] = useState(false);

  const onClickNavBtn = () => {
    if (showMobNav) {
      // Start closing animation
      setIsClosing(true);
      // Delay hiding the navigation until the animation finishes
      setTimeout(() => {
        setShowMobNav(false);
        setIsClosing(false); // Reset closing state
      }, 1400); // Match the animation duration
    } else {
      setShowMobNav(true);
    }
  };

  const onRenderMobileNav = () => (
    <MobNavContainer>
      <MobNavItems
        color="black"
        className={!isClosing ? "slide-in" : "slide-out"}
        duration="0.4s"
        delay="0.2s"
        closeDelay="1s"
        onClick={onClickNavBtn}
      >
        <MobNavLink href="#home">Home</MobNavLink>
      </MobNavItems>
      <MobNavItems
        color="#257180"
        className={!isClosing ? "slide-in" : "slide-out"}
        duration="0.4s"
        delay="0.4s"
        closeDelay="0.8s"
        onClick={onClickNavBtn}
      >
        <MobNavLink href="#service">Service</MobNavLink>
      </MobNavItems>
      <MobNavItems
        color="#912100 "
        className={!isClosing ? "slide-in" : "slide-out"}
        duration="0.4s"
        delay="0.6s"
        closeDelay="0.6s"
        onClick={onClickNavBtn}
      >
        <MobNavLink href="#project">Project</MobNavLink>
      </MobNavItems>
      <MobNavItems
        color="#FD8B51"
        className={!isClosing ? "slide-in" : "slide-out"}
        duration="0.4s"
        delay="0.8s"
        closeDelay="0.4s"
        onClick={onClickNavBtn}
      >
        <MobNavLink href="#about">About</MobNavLink>
      </MobNavItems>
      <MobNavItems
        color="#CB6040"
        className={!isClosing ? "slide-in" : "slide-out"}
        duration="0.4s"
        delay="1s"
        closeDelay="0.2s"
        onClick={onClickNavBtn}
      >
        <MobNavLink href="#contact">Contact</MobNavLink>
      </MobNavItems>
    </MobNavContainer>
  );

  return (
    <>
      <NavbarContainer>
        <Navbar>
          <NavLogo>{`<VK/>`}</NavLogo>
          <NavItemsContainer>
            <NavItems as="a" href="#Home">
              Home
            </NavItems>
            <NavItems as="a" href="#service">
              Service
            </NavItems>
            <NavItems as="a" href="#project">
              Project
            </NavItems>
            <NavItems as="a" href="#about">
              About
            </NavItems>
            <NavItems as="a" href="#contact">
              Contact
            </NavItems>
          </NavItemsContainer>
          {showMobNav ? (
            <CloseIcon onClick={onClickNavBtn} />
          ) : (
            <HamburgerMenu onClick={onClickNavBtn} />
          )}
        </Navbar>
      </NavbarContainer>
      {showMobNav && onRenderMobileNav()}
    </>
  );
};

export default Header;

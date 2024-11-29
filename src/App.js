import React from "react";
import Home from "./components/Home";
import Service from "./components/Service";
import Header from "./components/Header";
import Project from "./components/Project";
import About from "./components/About";
import Contact from "./components/Contact";
import "./App.css";

const App = () => {
  return (
    <>
      <Header />
      <Home />
      <Service />
      <Project />
      <About />
      <Contact />
    </>
  );
};

export default App;

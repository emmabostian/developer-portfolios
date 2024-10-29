import {
  Navbar,
  Home,
  About,
  Project,
  Experience,
  Contact,
  Footer
} from "./components/index";

function App() {
  return (
    <>
      <Navbar />
      <div id="home">
        <Home />
      </div>
      <div id="about">
        <About />
      </div>
      <div id="projects">
        {" "}
        <Project />
      </div>
      <div id="experience">
        <Experience />
      </div>
      <div id="contact">
        <Contact />
      </div>

      <Footer />
    </>
  );
}

export default App;

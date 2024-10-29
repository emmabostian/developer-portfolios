import React from "react";
import { Stepper, Step, StepLabel, Typography, Box } from "@mui/material";

const Experience = () => {
  const steps = [
    "Started Internship",
    "Learned Full Stack",
    "Completed Internship"
  ];

  return (
    <Box sx={{ margin: "2em" }}>
      <Typography
        variant="h4"
        component="div"
        gutterBottom
        sx={{ color: "black", fontWeight: "bold" }}
        className="font-robotoCondensed"
      >
        My Experience
      </Typography>

      <Stepper
        activeStep={steps.length}
        alternativeLabel
        sx={{ marginBottom: "2em" }}
      >
        {steps.map((label, index) => (
          <Step key={index}>
            <StepLabel
              StepIconProps={{
                sx: {
                  "&.Mui-active": { color: "#64FCD9" }, // Active step icon color
                  "&.Mui-completed": { color: "#2196F3" } // Completed step icon color
                }
              }}
            >
              <Typography
                sx={{ color: index === steps.length ? "#64FCD9" : "#6C757D" }}
              >
                {label}
              </Typography>
            </StepLabel>
          </Step>
        ))}
      </Stepper>

      <Box
        sx={{
          backgroundColor: "#F0F4F8",
          padding: "1.5em",
          borderRadius: "8px"
        }}
      >
        <Typography
          variant="h6"
          sx={{ color: "#2196F3", fontWeight: "bold", marginBottom: "1em" }}
        >
          Full Stack Developer Intern - Geeks for Geeks
        </Typography>
        <Typography variant="body1" sx={{ color: "#555" }}>
          <ul>
            <li>
              Led the development of dynamic web applications using{" "}
              <strong>React</strong>, <strong>Tailwind CSS</strong>,{" "}
              <strong>JavaScript</strong>, and <strong>Node.js</strong>,
              contributing to enhanced user experiences.
            </li>
            <li>
              Designed and implemented <strong>RESTful APIs</strong>, ensuring
              seamless frontend-backend communication with a focus on
              performance and scalability.
            </li>
            <li>
              Optimized <strong>MongoDB queries</strong> to handle large
              datasets and improve database performance, gaining hands-on
              experience with database scalability.
            </li>
            <li>
              Tackled errors and issues by developing strategies for{" "}
              <strong>error handling</strong> and improving problem-solving
              skills.
            </li>
            <li>
              Utilized <strong>Git</strong> and <strong>GitHub</strong> for
              version control, actively participated in code reviews, enhancing
              code quality.
            </li>
            <li>
              Wrote clean, modular, and maintainable code with a focus on
              scalability and project sustainability.
            </li>
            <li>
              Gained experience in full-stack development from frontend UI
              components to backend logic and database management.
            </li>
          </ul>
        </Typography>
      </Box>
    </Box>
  );
};

export default Experience;

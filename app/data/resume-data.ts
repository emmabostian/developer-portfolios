import { GitHubIcon, LinkedInIcon, XIcon } from "../components/icons";

export const RESUME_DATA = {
  name: "Youssef Sahih",
  location: "Morocco",

  about:
    "Motivated software developer with a strong track record of successfully completing various projects. Proficient in various programming languages and technologies, including C, C++, and web development technologies (HTML, CSS, JavaScript). Skilled in areas such as file handling, multithreading, game development, virtualization, and networking. Strong problem-solving abilities and a solid understanding of software development principles. Committed to continuous learning and delivering high-quality solutions. Ready to contribute expertise to new challenges.",
  summary:
    "As a software Developer with a background in computer systems, algorithms, and data structures, I have two years of experience in IT and two years of English studies under my belt. I am currently furthering my education in the 42 network for a Master Digital IT Architect degree. Coding and problem-solving through code are my passions, and I am excited to collaborate with talented programmers and expand my knowledge even more!",
  avatarUrl: "./ysahih.png",

  contact: {
    email: "ucefsahih@gmail.com",
    tel: "+212708978739",
    social: [
      {
        name: "GitHub",
        url: "https://github.com/ysahih",
        icon: GitHubIcon,
      },
      {
        name: "LinkedIn",
        url: "https://www.linkedin.com/in/youssef-sahih/",
        icon: LinkedInIcon,
      },
      {
        name: "X",
        url: "https://x.com/uc3f02",
        icon: XIcon,
      },
    ],
  },
  education: [
    {
      school: "Université Chouaïb Doukkali",
      degree: "Associate's Degree in English Studies.",
      start: "2020",
      end: "2022",
    },
    {
      school: "1337 - (42 network)",
      degree: "Master's Degree in IT Architecture.",
      start: "2022",
      end: "present",
    },
  ],
  skills: [
    "C",
    "C++",
    "Html",
    "Tailwind Css",
    "JavaScript",
    "TypeScript",
    "React",
    "Redux",
    "Node.js/Next.js",
    "Docker",
    "Git",
    "Jira",
    "Agile/Scrum",
  ],

  projects: [
    {
      title: "Pongy",
      techStack: ["Next.js", "React", "TypeScript"],
      description:
        "Pong contest website with real-time multiplayer games, chat, and security",
      link: {
        label: "github.com/ysahih",
        href: "https://github.com/ysahih/PingPong",
      },
    },
    {
      title: "Wordle-Game clone",
      techStack: ["Html", "Css", "JavaScript"],
      description: "a simple clone of the famous wordle game",

      link: {
        label: "github.com",
        href: "https://github.com/ysahih/blog",
      },
    },
    {
      title: "Inception",
      techStack: ["Docker", "Nginx", "mariaDb", "Wordpress"],
      description:
        "Created a Docker-based multi-container infrastructure with Nginx, WordPress, and MariaDB for a web application.",
      link: {
        label: "github.com",
        href: "https://github.com/ysahih/inception",
      },
    },
    {
      title: "IRC",
      techStack: ["C++", "Socket Programming"],
      description:
        "Internet Relay Chat server (Communication protocol on the Internet)",
      link: {
        label: "github.com",
        href: "https://github.com/ysahih/IRC",
      },
    },
    {
      title: "cub3D",
      techStack: ["C", "Graphics"],
      description:
        "My first RayCaster with miniLibX. This project is inspired by the world-famous Wolfenstein 3D game.",
      link: {
        label: "github.com",
        href: "https://github.com/ysahih/cub3D",
      },
    },
    {
      title: "sash",
      techStack: ["C", "Software Design and Architecture"],
      description: "simple implementation of Unix Shell with C",
      link: {
        label: "github.com",
        href: "https://github.com/ysahih/Sash",
      },
    },
  ],

  experience: [
    {
      company: "Im'enSe",
      position: "Frontend Developer",
      logo: 'https://media.licdn.com/dms/image/v2/C4E0BAQGwBEMaD6MB4Q/company-logo_200_200/company-logo_200_200/0/1670258446221?e=1749686400&v=beta&t=ke4p83O45mws8hx8rE5qkaD8KH5-aI1hPa6gesmqx_U',
      location: "Tangier, Morocco",
      startDate: "Aug 2024",
      endDate: "Present",
      description:
        "Working on front-end development projects for clients in the QHSE sector, focusing on secure, scalable web applications.",
      skills: [
        "React",
        "TypeScript",
        "Redux",
        "Node.js",
        "Jira",
        "Agile",
        "Git",
        "CI/CD",
        "REST APIs",
      ],
      achievements: [
        "Collaborated with cross-functional teams to deliver projects on time",
        "Contributed to the development of a secure authentication system",
        "Conducted code reviews and provided constructive feedback to peers",
        "Participated in the design and architecture of a new web application",
        "Worked closely with UX/UI designers to implement user-friendly interfaces",
        "Contributed to the development of a reusable component library",
        "Participated in the migration of a legacy application to a modern tech stack",
        "Worked on a project that reduced page load time by 50%",
        "Participated in the development of a web application that supports multiple languages",
        "Worked on a project that improved accessibility for users with disabilities",
        "Worked on a project that improved SEO performance by 30%",
        "Participated in the development of a web application that integrates with third-party APIs",
        "Worked on a project that improved data visualization for users",
      ],
    },
  ],
} as const;

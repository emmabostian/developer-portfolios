import React, { useState } from "react";
import emailjs from "emailjs-com";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import contactImage from "../assets/Person_on_mobile.png";

const Contact = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: ""
  });
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    emailjs
      .send(
        "service_lhww1qf",
        "template_6s66uop",
        formData,
        "8oXWSBFxwQOGI2la3"
      )
      .then((response) => {
        console.log("SUCCESS!", response.status, response.text);
        setSuccess(true);
        setError(false);
        setFormData({ name: "", email: "", message: "" }); 
        toast.success("Message sent successfully!"); 
      })
      .catch((err) => {
        console.error("FAILED...", err);
        setError(true);
        setSuccess(false);
        toast.error("Failed to send message. Please try again!"); 
      });
  };

  return (
    <div className="flex flex-col lg:flex-row m-4 p-6 bg-[#E9F1F2] rounded-lg shadow-lg">
      <div className="flex-1 p-4">
        <h2 className="text-3xl font-bold mb-4 text-center">Contact Me</h2>
        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <div>
            <label className="block font-medium mb-2">Name:</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              className="border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-[#64FCD9] placeholder-gray-400"
              placeholder="Enter your name"
            />
          </div>
          <div>
            <label className="block font-medium mb-2">Email:</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              className="border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-[#64FCD9] placeholder-gray-400"
              placeholder="Enter your email"
            />
          </div>
          <div>
            <label className="block font-medium mb-2">Message:</label>
            <textarea
              name="message"
              value={formData.message}
              onChange={handleChange}
              required
              className="border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-[#64FCD9] placeholder-gray-400"
              placeholder="Enter your message"
              rows="4"
            />
          </div>
          <button
            type="submit"
            className="bg-[#64FCD9] text-black font-bold px-4 py-2 rounded-md hover:bg-[#50e6cc] transition duration-300"
          >
            Send
          </button>
        </form>
       <ToastContainer
position="top-right"
autoClose={5000}
hideProgressBar={false}
newestOnTop={false}
closeOnClick
rtl={false}
pauseOnFocusLoss
draggable
pauseOnHover
theme="dark"
/>
      </div>
      <div className="flex-1 flex items-center justify-center mt-4 lg:mt-0">
        <img
          src={contactImage}
          alt="Contact"
          className="w-full h-auto rounded-lg"
        />
      </div>
    </div>
  );
};

export default Contact;

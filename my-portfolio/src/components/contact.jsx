import React, { useState } from 'react';
import emailjs from 'emailjs-com';

const ContactForm = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [sending, setSending] = useState(false);
  const [sent, setSent] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = (event) => {
    event.preventDefault();
    setSending(true);

    const templateParams = {
      name: name,
      email: email,
      message: message
    };

    emailjs.send('service_8xg5dhb', 'template_epzjowd', templateParams, 'jgXIK96_CuQKdiheZ')
     .then((response) => {
        console.log('Email sent successfully!', response);
        setSending(false);
        setSent(true);
        setName('');
        setEmail('');
        setMessage('')
      })
     .catch((error) => {
        console.error('Error sending email:', error);
        setSending(false);
        setError(error);
      });
  };

  return (
    <div className="py-20 overflow-y-auto max-h-screen md:max-h-full">
      <div className="flex items-center justify-center mb-10">
        <h2 className="text-2xl font-light text-white">Heyo, lets connect</h2>
      </div>
      
      <form onSubmit={handleSubmit} className="max-w-md mx-auto p-10 rounded-md shadow-md">
        <div className="mb-5">
          <label htmlFor="name" className="block text-white">Name:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(event) => setName(event.target.value)}
            className="w-full lg:w-full md:w-3/4 sm:w-2/3 xs:w-full text-black p-2 rounded-md"
          />
        </div>
        <div className="mb-5">
          <label htmlFor="email" className="block text-white">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
            className="w-full lg:w-full md:w-3/4 sm:w-2/3 xs:w-full text-black p-2 rounded-md"
          />
        </div>
        <div className="mb-5">
          <label htmlFor="message" className="block text-white">Your Message:</label>
          <textarea
            id="message"
            value={message}
            onChange={(event) => setMessage(event.target.value)}
            className="w-full lg:w-full md:w-3/4 sm:w-2/3 xs:w-full text-black p-2 rounded-md"
          />
        </div>
        {sending? (
          <button type="submit" disabled className="w-full lg:w-full md:w-1/2 sm:w-2/3 xs:w-full text-white p-2 bg-[#191825] rounded-md hover:bg-white hover:text-black border border-gray-300">
            Sending...
          </button>
        ) : (
          <button type="submit" className="w-full lg:w-full md:w-1/2 sm:w-2/3 xs:w-full text-white p-2 bg-[#191825] rounded-md hover:bg-white hover:text-black border border-gray-300">
            Send
          </button>
        )}
        {sent? (
          <p className="text-green-500">Email sent successfully!</p>
        ) : (
          error && (
            <p className="text-red-500">Error sending email: {error.message}</p>
          )
        )}
      </form>
    </div>
  );
};

export default ContactForm;
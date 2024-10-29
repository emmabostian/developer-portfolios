/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        majorMono: ['Major Mono Display', 'monospace'],
        poppins: ['Poppins', 'sans-serif'],
        robotoCondensed: ['"Roboto Condensed"', 'sans-serif']
      }
    }
  },
  plugins: []
}

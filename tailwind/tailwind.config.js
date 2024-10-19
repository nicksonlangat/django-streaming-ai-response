/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../**/templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        base: ['Hanken Grotesk', 'sans-serif'], // Set Hanken Grotesk as the default sans font
      },
    },
  },
  plugins: [],
}

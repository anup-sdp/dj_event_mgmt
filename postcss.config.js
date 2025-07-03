// js
module.exports = {
  plugins: [
    require('@tailwindcss/postcss')({
      content: [
        "./templates/**/*.html",
        "./**/templates/**/*.html", 
        "./**/*.py"
      ]
    }),
  ],
}

// ^ check for tailwindcss classes in files
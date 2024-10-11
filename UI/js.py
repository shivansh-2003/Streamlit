import streamlit as st
import streamlit.components.v1 as components

# Updated HTML content to animate the text color
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>The aurora (only CSS)</title>
  <style>
  @import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;800&display=swap");

  :root {
    --bg: #ffffff;  /* White background */
    --clr-1: #00c2ff;
    --clr-2: #33ff8c;
    --clr-3: #ffc640;
    --clr-4: #e54cff;
    --blur: 1rem;
    --fs: clamp(3rem, 8vw, 7rem);
    --ls: clamp(-1.75px, -0.25vw, -3.5px);
  }

  body {
    min-height: 100vh;
    display: grid;
    place-items: center;
    background-color: var(--bg);  /* Updated background color */
    color: #000;  /* Text color to black */
    font-family: "Inter", "DM Sans", Arial, sans-serif;
  }

  *,
  *::before,
  *::after {
    font-family: inherit;
    box-sizing: border-box;
  }

  .content {
    text-align: center;
  }

  .title {
    font-size: var(--fs);
    font-weight: 800;
    letter-spacing: var(--ls);
    position: relative;
    overflow: hidden;
    background: linear-gradient(90deg, var(--clr-1), var(--clr-2), var(--clr-3), var(--clr-4));
    background-size: 200%;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    animation: animateText 5s linear infinite;
    margin: 0;
  }

  @keyframes animateText {
    0% {
      background-position: 0%;
    }
    100% {
      background-position: 200%;
    }
  }
  </style>
</head>
<body>
  <div class="content">
    <h1 class="title">AI Travel Agent</h1>
  </div>
</body>
</html>
"""

# Display the HTML content with animated text in Streamlit
components.html(html_content, height=300, scrolling=False)

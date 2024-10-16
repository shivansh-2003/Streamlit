import streamlit as st
import time  # Import the time module

# Set the page configuration
st.set_page_config(page_title="Parallax Flipping Cards", layout="wide")

# Simulate loading images from an API
def load_images_from_api():
    images = []
    for i in range(1, 7):  # Simulate 6 images
        images.append(f'https://example.com/image{i}.jpg')  # Replace with actual API call
        time.sleep(2)  # Simulate delay in loading images
    return images

# Initialize placeholders for images
cols = st.columns(4)
image_placeholders = [col.empty() for col in cols]

# Load and display images as they come in
images = load_images_from_api()

for i, image_url in enumerate(images):
    column_index = i % 4  # Determine the correct column
    image_placeholders[column_index].image(image_url)
    if column_index == 3 and i < len(images) - 1:
        # Create a new row if there are more images
        cols = st.columns(4)
        image_placeholders = [col.empty() for col in cols]

# Add custom CSS
st.markdown("""
    <style>
    *{
      margin: 0;
      padding: 0;
      -webkit-box-sizing: border-box;
              box-sizing: border-box;
    }

    h1{
      font-size: 2.5rem;
      font-family: 'Montserrat';
      font-weight: normal;
      color: #444;
      text-align: center;
      margin: 2rem 0;
    }

    .wrapper{
      width: 90%;
      margin: 0 auto;
      max-width: 80rem;
    }

    .cols{
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      -ms-flex-wrap: wrap;
          flex-wrap: wrap;
      -webkit-box-pack: center;
          -ms-flex-pack: center;
              justify-content: center;
    }

    .col{
      width: calc(25% - 2rem);
      margin: 1rem;
      cursor: pointer;
    }

    .container{
      -webkit-transform-style: preserve-3d;
              transform-style: preserve-3d;
      -webkit-perspective: 1000px;
              perspective: 1000px;
    }

    .front,
    .back{
      background-size: cover;
      box-shadow: 0 4px 8px 0 rgba(0,0,0,0.25);
      border-radius: 10px;
      background-position: center;
      -webkit-transition: -webkit-transform .7s cubic-bezier(0.4, 0.2, 0.2, 1);
      transition: -webkit-transform .7s cubic-bezier(0.4, 0.2, 0.2, 1);
      -o-transition: transform .7s cubic-bezier(0.4, 0.2, 0.2, 1);
      transition: transform .7s cubic-bezier(0.4, 0.2, 0.2, 1);
      transition: transform .7s cubic-bezier(0.4, 0.2, 0.2, 1), -webkit-transform .7s cubic-bezier(0.4, 0.2, 0.2, 1);
      -webkit-backface-visibility: hidden;
              backface-visibility: hidden;
      text-align: center;
      min-height: 280px;
      height: auto;
      border-radius: 10px;
      color: #fff;
      font-size: 1.5rem;
    }

    .back{
      background: #cedce7;
      background: -webkit-linear-gradient(45deg,  #cedce7 0%,#596a72 100%);
      background: -o-linear-gradient(45deg,  #cedce7 0%,#596a72 100%);
      background: linear-gradient(45deg,  #cedce7 0%,#596a72 100%);
    }

    .front:after{
      position: absolute;
      top: 0;
      left: 0;
      z-index: 1;
      width: 100%;
      height: 100%;
      content: '';
      display: block;
      opacity: .6;
      background-color: #000;
      -webkit-backface-visibility: hidden;
              backface-visibility: hidden;
      border-radius: 10px;
    }
    .container:hover .front,
    .container:hover .back{
        -webkit-transition: -webkit-transform .7s cubic-bezier(0.4, 0.2, 0.2, 1);
        transition: -webkit-transform .7s cubic-bezier(0.4, 0.2, 0.2, 1);
        -o-transition: transform .7s cubic-bezier(0.4, 0.2, 0.2, 1);
        transition: transform .7s cubic-bezier(0.4, 0.2, 0.2, 1);
        transition: transform .7s cubic-bezier(0.4, 0.2, 0.2, 1), -webkit-transform .7s cubic-bezier(0.4, 0.2, 0.2, 1);
    }

    .back{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
    }

    .inner{
        -webkit-transform: translateY(-50%) translateZ(60px) scale(0.94);
                transform: translateY(-50%) translateZ(60px) scale(0.94);
        top: 50%;
        position: absolute;
        left: 0;
        width: 100%;
        padding: 2rem;
        -webkit-box-sizing: border-box;
                box-sizing: border-box;
        outline: 1px solid transparent;
        -webkit-perspective: inherit;
                perspective: inherit;
        z-index: 2;
    }

    .container .back{
        -webkit-transform: rotateY(180deg);
                transform: rotateY(180deg);
        -webkit-transform-style: preserve-3d;
                transform-style: preserve-3d;
    }

    .container .front{
        -webkit-transform: rotateY(0deg);
                transform: rotateY(0deg);
        -webkit-transform-style: preserve-3d;
                transform-style: preserve-3d;
    }

    .container:hover .back{
      -webkit-transform: rotateY(0deg);
              transform: rotateY(0deg);
      -webkit-transform-style: preserve-3d;
              transform-style: preserve-3d;
    }

    .container:hover .front{
      -webkit-transform: rotateY(-180deg);
              transform: rotateY(-180deg);
      -webkit-transform-style: preserve-3d;
              transform-style: preserve-3d;
    }

    .front .inner p{
      font-size: 2rem;
      margin-bottom: 2rem;
      position: relative;
    }

    .front .inner p:after{
      content: '';
      width: 4rem;
      height: 2px;
      position: absolute;
      background: #C6D4DF;
      display: block;
      left: 0;
      right: 0;
      margin: 0 auto;
      bottom: -.75rem;
    }

    .front .inner span{
      color: rgba(255,255,255,0.7);
      font-family: 'Montserrat';
      font-weight: 300;
    }

    @media screen and (max-width: 64rem){
      .col{
        width: calc(33.333333% - 2rem);
      }
    }

    @media screen and (max-width: 48rem){
      .col{
        width: calc(50% - 2rem);
      }
    }

    @media screen and (max-width: 32rem){
      .col{
        width: 100%;
        margin: 0 0 2rem 0;
      }
    }
    </style>
    """, unsafe_allow_html=True)

# Render HTML with flipping cards
st.markdown("""
<div class="wrapper">
  <h1>Parallax Flipping Cards</h1>
  <div class="cols">
      <div class="col" ontouchstart="this.classList.toggle('hover');">
        <div class="container">
          <div class="front" style="background-image: url(https://unsplash.it/500/500/)">
            <div class="inner">
              <p>Diligord</p>
              <span>Lorem ipsum</span>
            </div>
          </div>
          <div class="back">
            <div class="inner">
              <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Alias cum repellat velit quae suscipit c.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="col" ontouchstart="this.classList.toggle('hover');">
        <div class="container">
          <div class="front" style="background-image: url(https://unsplash.it/501/501/)">
            <div class="inner">
              <p>Rocogged</p>
              <span>Lorem ipsum</span>
            </div>
          </div>
          <div class="back">
            <div class="inner">
              <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Alias cum repellat velit quae suscipit c.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="col" ontouchstart="this.classList.toggle('hover');">
        <div class="container">
          <div class="front" style="background-image: url(https://unsplash.it/502/502/)">
            <div class="inner">
              <p>Strizzes</p>
              <span>Lorem ipsum</span>
            </div>
          </div>
          <div class="back">
            <div class="inner">
              <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Alias cum repellat velit quae suscipit c.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="col" ontouchstart="this.classList.toggle('hover');">
        <div class="container">
          <div class="front" style="background-image: url(https://unsplash.it/503/503/)">
            <div class="inner">
              <p>Clossyo</p>
              <span>Lorem ipsum</span>
            </div>
          </div>
          <div class="back">
            <div class="inner">
              <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Alias cum repellat velit quae suscipit c.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="col" ontouchstart="this.classList.toggle('hover');">
        <div class="container">
          <div class="front" style="background-image: url(https://unsplash.it/504/504/)">
            <div class="inner">
              <p>Rendann</p>
              <span>Lorem ipsum</span>
            </div>
          </div>
          <div class="back">
            <div class="inner">
              <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Alias cum repellat velit quae suscipit c.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="col" ontouchstart="this.classList.toggle('hover');">
        <div class="container">
          <div class="front" style="background-image: url(https://unsplash.it/505/505/)">
            <div class="inner">
              <p>Reflupper</p>
              <span>Lorem ipsum</span>
            </div>
          </div>
          <div class="back">
            <div class="inner">
              <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Alias cum repellat velit quae suscipit c.</p>
            </div>
          </div>
        </div>
      </div>
  </div>
</div>
""", unsafe_allow_html=True)

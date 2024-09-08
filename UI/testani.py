import streamlit as st

# Custom CSS for blinking text
st.markdown("""
    <style>
    .blinking {
        animation: blinker 1.5s linear infinite;
        color: red;
        font-size: 30px;
    }
    @keyframes blinker {
        50% {
            opacity: 0;
        }
    }
    </style>
    <div class="blinking">This text is blinking!</div>
""", unsafe_allow_html=True)


# Custom CSS for typing effect
st.markdown("""
    <style>
    .typewriter h1 {
        overflow: hidden;
        border-right: .15em solid orange; /* The cursor */
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: .15em;
        animation:
          typing 3.5s steps(40, end),
          blink-caret .75s step-end infinite;
    }
    /* The typing effect */
    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }
    /* The cursor effect */
    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: orange; }
    }
    </style>
    <div class="typewriter"><h1>Typing Animation in Streamlit!</h1></div>
""", unsafe_allow_html=True)

# Custom CSS for fading text
st.markdown("""
    <style>
    .fade-text {
        animation: fadeinout 4s infinite;
        font-size: 30px;
        color: green;
    }
    @keyframes fadeinout {
        0%, 100% { opacity: 0; }
        50% { opacity: 1; }
    }
    </style>
    <div class="fade-text">This text fades in and out!</div>
""", unsafe_allow_html=True)


# Custom CSS for bouncing text
st.markdown("""
    <style>
    .bounce {
        animation: bounce 2s infinite;
        color: blue;
        font-size: 30px;
    }
    @keyframes bounce {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-20px);
        }
    }
    </style>
    <div class="bounce">Bouncing Text Animation!</div>
""", unsafe_allow_html=True)

# Custom CSS for color-changing text
st.markdown("""
    <style>
    .color-change {
        animation: colorchange 3s infinite;
        font-size: 30px;
    }
    @keyframes colorchange {
        0% { color: red; }
        33% { color: green; }
        66% { color: blue; }
        100% { color: yellow; }
    }
    </style>
    <div class="color-change">This text changes color!</div>
""", unsafe_allow_html=True)


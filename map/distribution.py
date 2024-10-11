import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.stats import norm, binom, poisson, expon, f, t

# Set Streamlit layout
st.title("Visualizing Probability Distributions with Plotly")

# Sidebar for distribution selection
distribution = st.sidebar.selectbox(
    "Select a distribution",
    ["Normal", "Binomial", "Poisson", "Exponential", "F-Distribution", "T-Distribution"]
)


# Function to plot distributions
def plot_distribution(x, y, title):
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines', line=dict(color='blue'))])
    fig.update_layout(
        title=title,
        xaxis_title="X",
        yaxis_title="Probability Density",
        height=600,
        width=800
    )
    st.plotly_chart(fig, use_container_width=True)


# Parameters for different distributions
x_values = np.linspace(-10, 10, 500)

# Normal Distribution
if distribution == "Normal":
    mean = st.sidebar.slider("Mean", -5.0, 5.0, 0.0)
    std_dev = st.sidebar.slider("Standard Deviation", 0.1, 5.0, 1.0)

    st.subheader("Normal Distribution")
    st.markdown("""
    **Theory**: The normal distribution is a continuous probability distribution characterized by a bell-shaped curve. It is defined by two parameters: the mean (μ) and the standard deviation (σ).

    **Formula**:  
    $$f(x | \mu, \sigma^2) = \\frac{1}{\sigma \sqrt{2\pi}} e^{ -\\frac{(x - \mu)^2}{2 \sigma^2}}$$

    - **Mean (μ)**: The center of the distribution.
    - **Standard Deviation (σ)**: The spread of the distribution.
    """)

    # Normal Distribution
    y_values = norm.pdf(x_values, mean, std_dev)
    plot_distribution(x_values, y_values, "Normal Distribution (mean={}, std_dev={})".format(mean, std_dev))

# Binomial Distribution
elif distribution == "Binomial":
    n = st.sidebar.slider("Number of Trials", 1, 100, 10)
    p = st.sidebar.slider("Probability of Success", 0.0, 1.0, 0.5)

    st.subheader("Binomial Distribution")
    st.markdown("""
    **Theory**: The binomial distribution represents the number of successes in a fixed number of independent Bernoulli trials (i.e., yes/no experiments), with probability `p` of success.

    **Formula**:  
    $$P(X = k) = \\binom{n}{k} p^k (1 - p)^{n - k}$$

    - **n**: Number of trials.
    - **p**: Probability of success.
    """)

    # Binomial Distribution
    x_values = np.arange(0, n + 1)
    y_values = binom.pmf(x_values, n, p)
    plot_distribution(x_values, y_values, "Binomial Distribution (n={}, p={})".format(n, p))

# Poisson Distribution
elif distribution == "Poisson":
    lam = st.sidebar.slider("Lambda (Rate)", 1, 20, 5)

    st.subheader("Poisson Distribution")
    st.markdown("""
    **Theory**: The Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space, with the average rate `λ`.

    **Formula**:  
    $$P(X = k) = \\frac{\lambda^k e^{-\lambda}}{k!}$$

    - **λ**: The average rate of events in the interval.
    """)

    # Poisson Distribution
    x_values = np.arange(0, 30)
    y_values = poisson.pmf(x_values, lam)
    plot_distribution(x_values, y_values, "Poisson Distribution (λ={})".format(lam))

# Exponential Distribution
elif distribution == "Exponential":
    scale = st.sidebar.slider("Scale (1/Lambda)", 0.1, 5.0, 1.0)

    st.subheader("Exponential Distribution")
    st.markdown("""
    **Theory**: The exponential distribution describes the time between events in a Poisson process, i.e., events occurring continuously and independently at a constant average rate.

    **Formula**:  
    $$f(x|\lambda) = \lambda e^{-\lambda x}, \quad x \geq 0$$

    - **λ**: The rate parameter (inverse of the mean or scale).
    """)

    # Exponential Distribution
    x_values = np.linspace(0, 10, 500)
    y_values = expon.pdf(x_values, scale=scale)
    plot_distribution(x_values, y_values, "Exponential Distribution (scale={})".format(scale))

# F-Distribution
elif distribution == "F-Distribution":
    dfn = st.sidebar.slider("Degrees of Freedom (numerator)", 1, 100, 10)
    dfd = st.sidebar.slider("Degrees of Freedom (denominator)", 1, 100, 10)

    st.subheader("F-Distribution")
    st.markdown("""
    **Theory**: The F-distribution is used primarily in analysis of variance (ANOVA) and tests involving the ratio of variances. It is defined by two degrees of freedom: one for the numerator and one for the denominator.

    **Formula**:  
    $$f(x|d_1, d_2) = \\frac{(d_1 x)^{d_1/2} d_2^{d_2/2}}{B(d_1/2, d_2/2)} \\cdot \\frac{1}{(d_1 x + d_2)^{(d_1 + d_2)/2}}$$

    - **d₁**: Degrees of freedom for the numerator.
    - **d₂**: Degrees of freedom for the denominator.
    """)

    # F-Distribution
    x_values = np.linspace(0, 5, 500)
    y_values = f.pdf(x_values, dfn, dfd)
    plot_distribution(x_values, y_values, "F-Distribution (dfn={}, dfd={})".format(dfn, dfd))

# T-Distribution
elif distribution == "T-Distribution":
    df = st.sidebar.slider("Degrees of Freedom", 1, 100, 10)

    st.subheader("T-Distribution")
    st.markdown("""
    **Theory**: The t-distribution is used in hypothesis testing for small sample sizes, especially when the population standard deviation is unknown. It approaches the normal distribution as degrees of freedom increase.

    **Formula**:  
    $$f(x|v) = \\frac{\\Gamma((v+1)/2)}{\\sqrt{v\pi} \\Gamma(v/2)} \\cdot \\left(1 + \\frac{x^2}{v}\\right)^{-(v+1)/2}$$

    - **v**: Degrees of freedom.
    """)

    # T-Distribution
    y_values = t.pdf(x_values, df)
    plot_distribution(x_values, y_values, "T-Distribution (df={})".format(df))
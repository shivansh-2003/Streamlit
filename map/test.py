import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Title for the app
st.title("Interactive 3D Bar Plot with Plotly")

# Sample data
x_data = np.array([1, 2, 3, 4, 5])  # x-axis data
y_data = np.array([1, 2, 3, 4, 5])  # y-axis data
z_data = np.random.randint(1, 10, size=(5, 5))  # Random heights (z-axis)

# Create a figure for 3D scatter plot
fig = go.Figure()

# Add "bars" to the 3D plot using scatter3d with markers
for i in range(len(x_data)):
    for j in range(len(y_data)):
        # Simulate bars by creating lines (scatter markers) with varying z-heights
        fig.add_trace(go.Scatter3d(
            x=[x_data[i], x_data[i]],  # X-coordinates
            y=[y_data[j], y_data[j]],  # Y-coordinates
            z=[0, z_data[i, j]],       # From ground (z=0) to the bar height (z_data)
            mode='lines',
            line=dict(color='green', width=10),  # Width of the bar
        ))

# Update layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        zaxis_title="Z Axis",
        camera_eye=dict(x=1.87, y=0.88, z=0.64)  # Camera position
    ),
    title="3D Bar Plot with Plotly",
    height=600,
)

# Display the interactive 3D plot in Streamlit
st.plotly_chart(fig, use_container_width=True)
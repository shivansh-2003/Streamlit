import streamlit as st

# HTML and JavaScript for the 3D bar plot using Three.js
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>3D Bar Plot</title>
    <style>
        body {
            margin: 0;
        }
        canvas {
            display: block;
        }
    </style>
</head>
<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Scene setup
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        var renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Create bars (cuboids)
        var data = [3, 5, 8, 2, 7]; // Data for bar heights
        var barWidth = 1;           // Width of each bar
        var barSpacing = 1.5;       // Spacing between bars

        for (var i = 0; i < data.length; i++) {
            var geometry = new THREE.BoxGeometry(barWidth, data[i], barWidth);
            var material = new THREE.MeshBasicMaterial({color: 0x0077ff});
            var bar = new THREE.Mesh(geometry, material);

            // Position bars on the x-axis with spacing
            bar.position.x = i * barSpacing;
            bar.position.y = data[i] / 2;  // Center the bar height-wise
            scene.add(bar);
        }

        // Add lighting
        var ambientLight = new THREE.AmbientLight(0x404040); // Soft white light
        scene.add(ambientLight);
        var pointLight = new THREE.PointLight(0xffffff);
        pointLight.position.set(10, 10, 10);
        scene.add(pointLight);

        // Set camera position
        camera.position.z = 10;
        camera.position.y = 5;

        // Animation loop
        var animate = function () {
            requestAnimationFrame(animate);

            // Rotate the entire scene for better view
            scene.rotation.y += 0.01;

            renderer.render(scene, camera);
        };

        animate();
    </script>
</body>
</html>
"""

# Embed the HTML and JavaScript for the 3D bar plot in Streamlit
st.components.v1.html(html_code, height=600)
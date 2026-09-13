# PixelArt Weather Simulator

An interactive weather simulator built with Python and Pygame that translates live meteorological REST API data into real-time procedural pixel art animations and particle systems.

<img width="800" height="450" alt="pixelartSunGIF" src="https://github.com/user-attachments/assets/bf5faeda-aecb-4f9f-9ac8-0e4218afde57" />


---

## Technical Learnings & Architecture

Developing this application provided hands-on experience in decoupling network I/O, transforming dynamic data payloads, and architecting an extensible simulation engine:

### 1. API Ingestion & Data Transformation
* **REST Consumption:** Querying the Open-Meteo API to extract localized weather metrics, including temperature, precipitation volume, wind speed, cloud cover, and daily sunrise/sunset timings.
* **Time Serialization:** Parsing ISO-8601 timestamps into relative minute offsets from midnight. This enables direct mathematical comparisons with the local system clock to determine daylight bounds.
* **Unit Standardization:** Normalizing meteorological units (e.g., converting wind speed from km/h to m/s) to serve as baseline scalar constants for physics calculations.

### 2. Real-Time Animation & Particle Systems
* **Trigonometric Sun Trajectory:** Calculating the arc of the sun using a sinusoidal curve parameterized by the normalized elapsed daytime between sunrise and sunset.

  $$y = \text{horizon} - \left(\sin\left(\frac{t - t_{sunrise}}{t_{sunset} - t_{sunrise}} \cdot \pi\right) \cdot \text{arc height}\right)$$

* **Vectorized Rain & Particle Splashes:** Raindrops update based on vertical gravity and horizontal wind forces. The raindrop sprite is dynamically rotated using its motion vector angle. Upon collision with the ground boundary, a localized particle system is triggered with randomized trajectories and decaying lifespans to simulate splash physics.
* **Wind-Driven Sprite Animation:** Procedural tree swaying that dynamically changes state (idle, light wind, storm). Animation delay thresholds scale inversely with wind intensity, producing realistic cadence.

### 3. Resource Management & Performance
* **Centralized Asset Caching:** Implemented an `AssetManager` to preload image assets into memory at startup. This prevents redundant disk reads and file lookups during the render loop.
* **Surface Optimization:** Leveraged `pygame.Surface.convert_alpha()` during initialization to match pixel formats to the display context, accelerating blit operations across multiple particle and sprite layers.

---

## Day & Night Simulation

The environment dynamically transitions to night mode based on sunset calculations. The day sky shifts to a night palette, and procedural star fields are scattered across the upper atmosphere:

<img width="800" height="450" alt="pixelartNightGIF" src="https://github.com/user-attachments/assets/3ade97f6-f2a3-4b4c-a23c-ecc3441ceee5" />


---

## Project Structure

```text
├── assets/                  # Raw pixel art sprite sheets (trees, clouds, stars, wind)
├── rendering/
│   ├── asset_manager.py     # Centralized sprite preloading and dictionary cache
│   ├── cloud.py             # Procedural cloud drift and wrapping logic
│   ├── raindrop.py          # Rain physics and splash particle system
│   ├── renderer.py          # Main rendering pipeline, z-sorting, and scene state
│   ├── star.py              # Night sky star positioning and rendering
│   ├── sun.py               # Sinusoidal trajectory calculations for the sun
│   ├── tree.py              # Frame-based animation driven by wind thresholds
│   └── wind.py              # Ambient wind visualizer with circular wave offsets
├── weather_data/
│   └── weather_data_api.py  # HTTP client for the Open-Meteo REST endpoint
├── main.py                  # Pygame loop and application entrypoint
├── requirements.txt         # Project dependencies
└── README.md
```

---

## Getting Started

### Prerequisites
Make sure you have [Python](https://www.python.org/) (version 3.10 or higher) installed on your system.

### 1. Clone the repository
```bash
git clone https://github.com/KarlNoerskov/PixelArt-Weather-app.git
cd PixelArt-Weather-app
```

### 2. Create and activate a virtual environment
* **macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
* **Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
Install all required libraries recursively from the requirements manifest:
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python main.py
```

Author Karl Nørskov

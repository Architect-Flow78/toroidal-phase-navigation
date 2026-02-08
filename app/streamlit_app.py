import streamlit as st
import matplotlib.pyplot as plt

from phase.space import PhasePoint
from phase.bodies import PhaseBody
from engine.simulator import PhaseSimulator

st.set_page_config(layout="wide")
st.title("Toroidal Phase Navigation Engine")

# Bodies (demo)
bodies = [
    PhaseBody(0.2, 0.3, 1.0, "Sun"),
    PhaseBody(0.7, 0.6, 0.6, "Planet")
]

sim = PhaseSimulator(bodies)

st.sidebar.header("Initial Phase Position")
θ0 = st.sidebar.slider("θ", 0.0, 1.0, 0.1)
φ0 = st.sidebar.slider("φ", 0.0, 1.0, 0.1)

start = PhasePoint(θ0, φ0)

if st.button("Run Simulation"):
    nulls, traj = sim.analyze(start)

    fig, ax = plt.subplots(figsize=(6,6))

    if nulls:
        x, y, _ = zip(*nulls)
        ax.scatter(x, y, s=10, c="blue", label="Null zones")

    tx = [p.theta for p in traj]
    ty = [p.phi for p in traj]
    ax.plot(tx, ty, c="red", label="Trajectory")

    ax.set_xlabel("θ (cycle)")
    ax.set_ylabel("φ (rotation)")
    ax.legend()
    ax.set_title("Phase Space (π = 1)")
    st.pyplot(fig)
  

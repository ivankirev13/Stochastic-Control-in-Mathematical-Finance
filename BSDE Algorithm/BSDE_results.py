import tensorflow as tf
import matplotlib.pyplot as plt
from BSDE_Solver import BSDE_Solver

# Set parameters
parameters = {
    "Q": tf.constant([[0.0, 0.0], [0.0, 0.0]]),
    'R': tf.constant([[0.0, 0.0], [0.0, 0.0]]),
    'S': tf.constant([[0.0, 0.0], [0.0, 0.0]]),
    'A': tf.constant([[0.5, 0.3], [0.3, 0.5]]),
    'B': tf.constant([[0.5, 0.1], [0.1, 0.5]]),
    'C': tf.constant([[0.3, 0.1], [0.1, 0.3]]),
    'D': tf.constant([[0.6, 0.2], [0.2, 0.6]]),
    'G': -tf.constant([[0.2, 0.1], [0.1, 0.2]]),
    'L': -tf.constant([[0.3], [0.5]]),
    'N': 20,
    'batch_size': 1000,
    'iteration_steps': 1000,
    'x_0': tf.Variable([[0.3], [0.1]]),
    'lr_gamma': 1e-2,
    'lr_pi': 1e-3
}

# Define solver with the parameters
solver = BSDE_Solver(parameters)

# Train solver
solver.train(display_steps=True)

# Plot the loss functions
fig, axs = plt.subplots(1, 2, figsize=(20, 7.5))

# First plot
axs[0].plot(range(1, parameters["iteration_steps"]+1), solver.bsde_losses)
axs[0].set_yscale('log')
axs[0].set_title("Loss Function of the BSDE")
axs[0].set_xlabel("Iteration step")
axs[0].set_ylabel("BSDE Loss")

# Second plot
axs[1].plot(range(1, parameters["iteration_steps"]+1), solver.control_losses)
axs[1].set_yscale('log')
axs[1].set_title(r"Derivative of the Hamiltonian w.r.t $\pi$")
axs[1].set_xlabel("Iteration step")
axs[1].set_ylabel("Control Loss")

# Display
plt.show()

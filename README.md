# NumPy Student Marks Analysis

A modern, dark-themed desktop application to store and analyze student marks. Built using Python, Tkinter, NumPy, and Matplotlib.

## Features
- Add, view, and remove student marks.
- Validate inputs (Name cannot be empty, marks must be numeric and between 0-100).
- Dynamically calculate statistics using **NumPy** (Maximum, Minimum, Average, Total, Standard Deviation).
- Visualize data with a modern dark-themed Matplotlib bar chart.
- Simple, beginner-friendly UI with clean code architecture.

## Tech Stack
- **Python 3.x**
- **Tkinter** (GUI)
- **NumPy** (Calculations)
- **Matplotlib** (Graphing)

## Setup & Installation

1. Clone or download this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Project Structure
- `main.py`: Entry point for the application.
- `ui.py`: Contains the Tkinter GUI implementation.
- `analysis.py`: Contains the `MarksAnalysis` class with NumPy logic.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

# MazeSolver

MazeSolver is a web-based interactive application for visualizing and understanding maze-solving algorithms. Built with Django and featuring a modern front-end, it allows users to generate, edit, and solve mazes using multiple classic search algorithms, observing their behavior and performance in real time.

## Features

- **Interactive Maze Creation:** Design and edit the maze structure directly in the browser.
- **Multiple Solvers:** Choose from Breadth-First Search (BFS), Depth-First Search (DFS), Iterative Deepening DFS, A* Search, and Dijkstra's Algorithm.
- **Step-by-Step Visualization:** Watch how each algorithm explores the maze, including visited nodes and final path.
- **Custom Controls:** Adjust animation speed, clear the maze, and toggle between algorithms easily.
- **Statistics:** See real-time stats on nodes visited, path length, and which algorithm was used.
- **Responsive UI:** Designed for desktop and tablet, with a clean and intuitive interface.

## Technologies Used

- **Backend:** Django 5, Python 3.11
- **Frontend:** HTML, CSS, JavaScript
- **Containerization:** Docker support for easy deployment

## Getting Started

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/estside/mazesolver.git
   cd mazesolver
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

4. **Open your browser:**  
   Navigate to `http://localhost:8000` to start using MazeSolver.

### Docker

1. **Build and run using Docker:**
   ```bash
   docker build -t mazesolver .
   docker run -p 8000:8000 mazesolver
   ```

## Usage

- Use the grid to draw walls, set start (green) and end (red) points.
- Pick an algorithm from the dropdown.
- Click "Solve Maze" to visualize the solution.
- Adjust speed and clear the maze as needed.
- Statistics update live as the solver runs.

## License

This project is for educational and demonstration purposes. License details to be added.

## Author

- [Saurav Mandi](https://saurav-portfolio-mandi.vercel.app)

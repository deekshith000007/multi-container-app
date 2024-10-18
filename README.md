<h3>Multi-Container Flask & MySQL Application</h3>
<p></p>This project demonstrates how to build and deploy a simple multi-container web application using Docker Compose. The application consists of a Flask frontend and a MySQL backend database, with Docker Compose managing both services.</p>
</p>

<h5>Prerequisites</h5>h5>
- Docker installed on your system.
- Docker Compose installed.
- Basic knowledge of Python and MySQL.

The project includes two main services:

Flask (Frontend): A Python web framework that provides two routes:
/: Displays a welcome message.
/db: Connects to the MySQL database and displays tables.
MySQL (Backend): A MySQL 5.7 container serving as the database for the application.
Setup Instructions
1. Clone the repository:
bash
Copy code
git clone <repository-url>
cd multi-container-app
2. Build and run the application:
bash
Copy code
docker-compose build
docker-compose up
This will start the Flask app on http://localhost:5000 and the MySQL database on port 3306.

3. Access the Application:
Visit http://localhost:5000 for the Flask app.
Visit http://localhost:5000/db to check database connectivity.
Flask API Endpoints
/: Displays a welcome message.
/db: Connects to the MySQL database and returns the list of tables.
Cleanup
To stop and remove the containers:

bash
Copy code
docker-compose down
Technologies Used
Docker: Containerization of services.
Docker Compose: Orchestration for multi-container applications.
Flask: Web framework for the frontend.
MySQL: Database service.

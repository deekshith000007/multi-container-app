<h3>Multi-Container Flask & MySQL Application</h3>
<p></p>This project demonstrates how to build and deploy a simple multi-container web application using Docker Compose. The application consists of a Flask frontend and a MySQL backend database, with Docker Compose managing both services.</p>
</p>

<h4>Prerequisites</h4>
 Docker installed on your system.<br>
- Docker Compose installed.<br>
- Python and MySQL.<br>

<h4>The project includes two main services:</h4>
Flask (Frontend): A Python web framework that provides two routes:<br>
/: Displays a welcome message.<br>
/db: Connects to the MySQL database and displays tables.
MySQL (Backend): A MySQL 5.7 container serving as the database for the application.<br>
<br>
<h4>Setup Instructions</h4>
1. Clone the repository:<br>
git clone <repository-url><br>
cd multi-container-app<br>
<br>
2. Build and run the application:<br>
docker-compose build<br>
docker-compose up<br>
This will start the Flask app on http://localhost:5000 and the MySQL database on port 3306.<br>

3. Access the Application:<br>
Visit http://localhost:5000 for the Flask app.<br>
Visit http://localhost:5000/db to check database connectivity.<br>
Flask API Endpoints<br>
/: Displays a welcome message.<br>
/db: Connects to the MySQL database and returns the list of tables.<br>
<br>
<h4> Technologies Used </h4>
Docker: Containerization of services.<br>
Docker Compose: Orchestration for multi-container applications.<br>
Flask: Web framework for the frontend.<br>
MySQL: Database service.<br>

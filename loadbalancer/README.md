# Flask Load Balancer
This simple Flask application serves as a load balancer that distributes incoming requests among multiple servers. The goal is to enhance fault tolerance and distribute the load evenly across available servers.

##Prerequisites
Before running this application, make sure you have the following installed:

Python
Flask
Requests

You can install the required packages using the following command:
pip install Flask requests


# Getting started
1. Clone this repository to your local machine:
git clone https://github.com/your-username/flask-load-balancer.git

2. Navigate to the project directory:
cd flask-load-balancer

3. Run the Flask application:
python app.py

By default, the application will run on http://127.0.0.1:5000/.

# Configuration
In the app.py file, you can customize the list of server hosts in the HOSTS variable. Ensure that you replace the placeholder values with the actual server hosts you want to load balance requests to.

HOSTS = ['server1.example.com', 'server2.example.com', 'server3.example.com']

# Usage
Once the application is running, you can make GET requests to the /darian endpoint, and the load balancer will distribute the request among the configured servers.

curl http://127.0.0.1:5000/darian

# Error Handling
The application will attempt to forward the request to each server in the list until it succeeds or reaches the maximum number of attempts (3 by default). If all attempts fail, the response will indicate a failure.

# Contributing
Feel free to contribute to the development of this project by submitting issues or pull requests. Your feedback and suggestions are highly appreciated.

# License
This project is licensed under the APACHE 2.0 License - see the LICENSE file for details.
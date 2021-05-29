# anomaly_detection

This project is to build an end-to-end data demonstration that employs machine learning models for anomaly detection, various web services, and monitoring tools to find any unusual cases within the platform.

The data platform will consist of these components:

* A service that serves the anomaly detection models.
	* The anomaly detector will be an isolation forest model trained with a curated and real dataset.
	* As part of the model development, we will visualize the anomalous decision boundary to understand its decisions better.
	* Libraries to be used: scikit-learn and Plotly.
* Docker Compose will be used to define and run multiple Docker images:
	* The monitoring tools Prometheus, and Grafana, tools that excel at visualizing monitoring dashboards.
	* Jupyter Notebooks - a tool to train the model and analyze the data.


---
title: proj-information
date: 01-03-2023
tags:
  - cen
aliases: []
---

# Dataset: [Flight Data](https://www.kaggle.com/datasets/robikscube/flight-delay-dataset-20182022?select=Combined_Flights_2022.csv)

# What do we want to serve (Value + API):

### **Use Case 1:** 

User obtains statistics about flights according to certain criteria.

- **Endpoint:** `/flights/statistics`

- **REST Type:** `GET`

- **Use Case Diagram:**
```mermaid

sequenceDiagram

  Client->>API Gateway: Specifies criteria about <br> flights to the API
	API Gateway->>Flights Microservice: Sends request to <br> corresponding microservice
  Flights Microservice->>Database: Queries database <br> about flight data <br> using given criteria
	Database->>Flights Microservice: Sends result from <br> the previous query <br>
  Flights Microservice->>API Gateway: Calculates statistics and sends
  API Gateway->>Client: Sends result <br>

```

### **Use Case 2:** 

User obtains flight information by flight number.

- **Endpoint:** `/flights/{:flight-number}`

- **REST Type:** `GET`

- **Use Case Diagram:**
```mermaid

sequenceDiagram

  Client->>API Gateway: Requests for information <br> about flight $id
  API Gateway->>Flights Microservice: Sends request to <br> corresponding microservice
	Flights Microservice->>Database: Queries database <br> about information <br> regarding flight $id
  Database->>Flights Microservice: Sends result from <br> the previous query <br>
	Flights Microservice->>API Gateway: Sends result
  API Gateway->>Client: Sends result

```

### **Use Case 3:** 

User provides a future flight details and obtains a forecast on the probability of the flight being cancelled, diverted and delayed.

- **Endpoint:** `/flights/forecast`

- **REST Type:** `GET`

- **Use Case Diagram:**
```mermaid

sequenceDiagram

  Client->>API Gateway: Provides information about <br> the flight to be forecasted
  API Gateway->>Forecast Microservice: Route request to <br> corresponding microservice
	Forecast Microservice->>Prediction Model: Asks prediction model <br> for a forecast with <br> the given information
	Prediction Model->>Forecast Microservice: Sends result from the <br> prediction
  Forecast Microservice->>API Gateway: Sends result
  API Gateway->>Client: Sends result <br>

```

### **Use Case 4:** 

User obtains the ranking of airlines and their reliability

- **Endpoint:** `/airline/rank`

- **REST Type:** `GET`

- **Use Case Diagram:**
```mermaid

sequenceDiagram

  Client->>API Gateway: Requests ranking of airlines <br> and provides information about <br> ranking scope and priorities
  API Gateway->>Ranking Microservice: Route request to <br> corresponding microservice
	Ranking Microservice->>Flights Microservice: Requests statistics about <br> flights according to criteria
  Ranking Microservice->>Airlines Microservice: Requests airlines information
	Ranking Microservice->>API Gateway: Calculates ranking based <br> on obtain information <br> and returns the result
  API Gateway->>Client: Sends result <br>

```

### **Use Case 5:**

Admin adds information about a flight to the database.

- **Endpoint:** `/admin/flight`
  
- **REST Type:** `POST`
  
- **Use Case Diagram:**
```mermaid

sequenceDiagram

  Admin->>API Gateway: Provides information about <br> flight to be added
	API Gateway->>Flights Microservice: Route request to <br> corresponding microservice
  Flights Microservice->>Databases: Inserts data
	Databases-->>Flights Microservice: Sends status of insertion
  Flights Microservice->>API Gateway: Sends the newly created flight <br> or an error message
  API Gateway->>Admin: Sends result

```

### **Use Case 6:**

Admin updates the information of a flight on the database by flight number.

- **Endpoint:** `/admin/flight/{:flight-number}`
  
- **Use Case Diagram:**
```mermaid

sequenceDiagram

  Admin->>API Gateway: Provides information about <br> flight to be updated
	API Gateway->>Flights Microservice: Route request to <br> corresponding microservice
  Flights Microservice->>Databases: Updates data
	Databases-->>Flights Microservice: Sends status of insertion
  Flights Microservice->>API Gateway: Sends the updated flight <br> or an error message
  API Gateway->>Admin: Sends result

```

### **Use Case 7:**

Admin deletes the information of a flight from the database

- **Endpoint:** `/admin/flight/{flight-number}`
  
- **REST Type:** `DELETE`

- **Use Case Diagram:**
```mermaid

sequenceDiagram

  Admin->>API Gateway: Provides information about <br> flight to be deleted
	API Gateway->>Flights Microservice: Route request to <br> corresponding microservice
  Flights Microservice->>Databases: Deletes data
	Databases-->>Flights Microservice: Sends status of deletion
  Flights Microservice-->>API Gateway: Sends status of deletion
  API Gateway-->>Admin: Sends resultㅤ

```
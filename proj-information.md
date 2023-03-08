---
title: proj-information
date: 01-03-2023
tags:
  - cen
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

User obtains airline information by airline code.

- **Endpoint:** `/airline/{airline-code}`

- **REST Type:** `GET`

- **Use Case Diagram:**
```mermaid

sequenceDiagram

  Client->>API Gateway: Requests for information <br> about airline $id
  API Gateway->>Airlines Microservice: Sends request to <br> corresponding microservice
	Airlines Microservice->>Database: Queries database <br> about information <br> regarding airline $id
  Database->>Airlines Microservice: Sends result from <br> the previous query <br>
	Airlines Microservice->>API Gateway: Sends result
  API Gateway->>Client: Sends result

```

### **Use Case 6:**

Admin adds information about a flight to the database.

- **Endpoint:** `/admin/flights`
  
- **REST Type:** `POST`
  
- **Use Case Diagram:**
```mermaid

sequenceDiagram

  Admin->>API Gateway: Provides information about <br> flight to be added
	API Gateway->>Admin Microservice: Route request to <br> corresponding microservice
  Admin Microservice->>Databases: Inserts data
	Databases-->>Admin Microservice: Sends status of insertion
  Admin Microservice-->>API Gateway: Sends the newly created flight <br> or an error message
  API Gateway-->>Admin: Sends result

```

### **Use Case 7:**

Admin updates the information of a flight on the database by flight number.

- **Endpoint:** `/admin/flight/{:flight-number}`
  
- **Use Case Diagram:**
```mermaid

sequenceDiagram

  Admin->>API Gateway: Provides information about <br> flight to be updated
	API Gateway->>Admin Microservice: Route request to <br> corresponding microservice
  Admin Microservice->>Databases: Updates data
	Databases-->>Admin Microservice: Sends status of insertion
  Admin Microservice-->>API Gateway: Sends the updated flight <br> or an error message
  API Gateway-->>Admin: Sends result

```

### **Use Case 8:**

Admin deletes the information of a flight from the database

- **Endpoint:** `/admin/flight/{:flight-number}`
  
- **REST Type:** `DELETE`

- **Use Case Diagram:**
```mermaid

sequenceDiagram

  Admin->>API Gateway: Provides information about <br> flight to be deleted
	API Gateway->>Admin Microservice: Route request to <br> corresponding microservice
  Admin Microservice->>Databases: Deletes data
	Databases-->>Admin Microservice: Sends status of deletion
  Admin Microservice-->>API Gateway: Sends status of deletion
  API Gateway-->>Admin: Sends resultㅤ

```

<div style="page-break-after: always;"></div>

## Architecture and Functional Diagrams:

### Architecture:

![cloud-architecture-diagram](assets/cloud-architecture-diagram.png)

### Functional:

![functional-diagram](assets/functional-diagram.png)


## Group


Group 16:
- Robert Morosan - 54456
- Inês Fragoso - 54454
- Santiago Benites - 54392
- Diogo Ferreira - 54407
- João Ferreira - 55312
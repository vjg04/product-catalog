## Repository, Image, and API Access

### 1. Source Code Repository

GitHub / Code Repository Link:

https://github.com/vjg04/product-catalog.git

---

### 2. Container Image Repository

#### If using Azure Container Registry (current implementation)

Container images for the Product API are stored in **Azure Container Registry (ACR)**.

Registry Name:


acrproductcatalogvijay.azurecr.io/product-api

versions

acrproductcatalogvijay.azurecr.io/product-api:v1
acrproductcatalogvijay.azurecr.io/product-api:v2
acrproductcatalogvijay.azurecr.io/product-api:v3
acrproductcatalogvijay.azurecr.io/product-api:v4


---

#### If Docker Hub is mandatory for the assignment

Docker Hub repository URL:

I did not use docker hub or docker image as I could not install docker hub to upload image from local machine neither azure cloud shell support docker daemon

---

### 3. Service API URL

The Product API service is exposed through a Kubernetes `LoadBalancer` service.

Public API Base URL:


http://4.224.79.233

---

### 4. API Endpoints to View Backend Data

#### Get all products

http://4.224.79.233/products


This endpoint fetches records from the backend PostgreSQL database through the FastAPI service layer.

#### Health endpoint

http://4.224.79.233/health

#### Swagger API documentation

http://4.224.79.233/docs

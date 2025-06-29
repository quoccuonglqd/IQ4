# Acme Facilities MLOps Assessment Solution

This repository presents a full-stack solution to the 2025 Acme Facilities MLOps. It includes CI/CD automation, model training, Kubernetes deployment, monitoring, Airflow data pipeline, Linux ops, and an optional AWS infrastructure sketch.

---

## 📁 Project Structure

```text
├── azure-pipelines.yml         # CI/CD pipeline (Part A)
├── Dockerfile.train            # Docker image to retrain model.pkl (Part B)
├── Dockerfile.app              # Docker image for FastAPI inference (Part C)
├── Makefile                    # Command aliases for pipeline execution
├── app.py                      # FastAPI app serving predictions (Part C)
├── pyproject.toml              # Dependencies with Poetry
├── poetry.lock                 # Poetry lock file 
```

---

## 🚀 Setup Instructions

### 1. Clone and Install

```bash
git clone https://github.com/quoccuonglqd/IQ4
cd IQ4
```

### 2. Install Python Dependencies

```bash
python -m venv .venv
source venv/bin/activate # Linux
.venv\Scripts\activate   # Windows
pip install poetry==1.8.5
poetry install
```

### 3. Train the Model

```bash
make train
```

This builds the Docker image from `Dockerfile.train`, retrains the model using `sample_data.csv`, load `model.pkl` and write to `new_model.pkl`

### 4. Run FastAPI Locally
Update line 8 of `app.py` to `resources/model.pkl`

```bash
docker build -f Dockerfile.app -t acme-ml-api:latest .
docker run -p 5000:5000 acme-ml-api:latest
```

Test with:

```bash
curl -X POST http://localhost:5000/predict \
     -H 'Content-Type: application/json' \
    -d '{"job_id":0,"engineer_id":4,"job_type":"HVAC","job_priority":"High","engineer_skill_level":3,"engineer_experience_years":18,"distance_km":4.99}'
```

Runs all parts in order.

---

## 🛠️ Azure DevOps CI/CD (Part A)

### Prerequisites
- Azure DevOps account
- Azure Container Registry (ACR) set up

### Create service connection to Azure Container Registry (ACR)
- Go to your Azure DevOps project > Project Settings.

- Under Pipelines, click Service connections.

- Click New service connection > choose Docker Registry.

- Select Azure Container Registry, and then select Managed Service Identity as your Authentication Type.

- Enter your Subscription ID Subscription name, and your Azure container registry login server.

- Enter a name for your service connection

- Click Save.

### Configure variables in the Azure DevOps Pipeline UI:

* `ACR_NAME`: Azure Container Registry name
* `IMAGE_NAME`: Docker image name, e.g., `acme-ml-api`
* `DOCKER_REGISTRY_SERVICE_CONNECTION`: Service connection for ACR access defined above

## 📬 Contact

For any issues, please contact \[[quoccuonglqd123@gmail.com](mailto:quoccuonglqd123@gmail.com)] or open a GitHub issue.

---

## ✅ License

MIT License

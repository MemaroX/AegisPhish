# AegisPhish Project Plan

This document outlines the development roadmap for the AegisPhish application, based on the master blueprint. Our progress will be tracked here.

---

## Phase 1: Foundation & Setup

### Milestone 1: Project Setup & Environment

- [x] Initialize Git repository
- [x] Create `requirements.txt` with all dependencies
- [x] Set up `.gitignore` file
- [x] Create basic Flask app structure using the factory pattern
- [x] Configure a robust logging system for file and console output
- [x] Set up database schema (SQLite for MVP)
- [x] Configure and initialize the database with Flask-SQLAlchemy & Flask-Migrate
- [x] Define initial database models (`User`, `Email`, `AnalysisResult`)
- [x] Generate the initial database migration script
- [x] Apply the migration to create the database tables

### Milestone 2: Data Collection & Preparation

- [x] Identify and acquire public datasets
- [x] Develop a data preprocessing pipeline (`preprocess_email` function)
- [ ] Implement data validation (check missing values, balance classes)
- [ ] Create and document final train/validation/test splits

---

## Phase 2: Core Feature Development

### Milestone 3: Email Analysis Engine

- [x] Implement email loading from file/string
- [ ] Implement header parsing and validation (`parse_email_headers` function)
- [ ] Implement body content extraction (text, HTML, links)
- [ ] Implement attachment handling
- [ ] Implement error handling for malformed emails

### Milestone 4: Feature Engineering

- [ ] **URL-Based Features:**
    - [ ] Develop domain analysis functions (age, WHOIS, similarity)
    - [ ] Develop URL inspection functions (shorteners, length, special characters)
- [ ] **Text-Based Features:**
    - [ ] Develop keyword analysis functions (suspicious terms, grammar, case ratios)
    - [ ] Develop pattern recognition for social engineering cues
- [ ] **Sender-Based Features:**
    - [ ] Implement SPF/DKIM/DMARC validation checks
    - [ ] Develop functions to analyze sender reputation and behavior
- [ ] **Technical Features:**
    - [ ] Develop HTML structure analysis functions
    - [ ] Develop attachment analysis functions (file types, sizes)

### Milestone 5: Machine Learning Model Development

- [ ] Train baseline models (Logistic Regression, Random Forest)
- [ ] Develop a training and evaluation script
- [ ] Implement model evaluation using key metrics (Accuracy, Precision, Recall, F1)
- [ ] Implement K-Fold cross-validation
- [ ] Save the trained model to a file

---

## Phase 3: API & User Interface

### Milestone 6: API Development

- [ ] Create a secure API endpoint for email analysis (e.g., `/api/v1/analyze`)
- [ ] Implement input validation and sanitization
- [ ] Integrate the full analysis and prediction pipeline into the endpoint
- [ ] Define and return a structured JSON response

### Milestone 7: User Interface & Testing

- [ ] **Frontend:**
    - [ ] Create a simple HTML form to submit email content
    - [ ] Use JavaScript to fetch results from the API and display them
- [ ] **Testing:**
    - [ ] Write unit tests for key functions (parsing, feature extraction)
    - [ ] Write integration tests for the API endpoint

---

## Phase 4: Deployment & Finalization

### Milestone 8: System Integration & Deployment

- [ ] Create a `Dockerfile` for containerization
- [ ] Configure a production-ready WSGI server (e.g., Gunicorn)
- [ ] Implement security best practices (e.g., secret management)
- [ ] Set up application and model monitoring

### Milestone 9: Final Testing & Optimization

- [ ] Conduct performance optimization and benchmarking
- [ ] Perform final security audits and user acceptance testing
- [ ] Finalize all technical and user documentation
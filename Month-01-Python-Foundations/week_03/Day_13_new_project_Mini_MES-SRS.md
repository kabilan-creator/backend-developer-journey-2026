# Software Requirements Specification (SRS) creating a software application for a Mini MES System.

## Introduction
The purpose of this document is to outline the software requirements for a Mini Manufacturing Execution System (MES). This system will be designed to manage and monitor manufacturing processes, providing real-time data and insights to improve efficiency and productivity.

# 🏭 Barcode-Based Production Tracking System (Mini MES)

## 📌 1. Project Overview

This project is a **backend system** designed to simulate a **Manufacturing Execution System (MES)**.

It tracks parts using **unique barcodes**, manages their movement across different production stations, and handles quality checks, scrap, rework, and defect tracking.

---

## 🎯 2. Objectives

* Track each part using a **unique barcode**
* Simulate **real factory workflow**
* Manage **process movement between stations**
* Implement **quality control (pass/fail)**
* Handle **scrap and rework operations**
* Maintain **production history for traceability**

---

## 🏭 3. System Workflow

```text
Create Part (Barcode)
        ↓
DDG
        ↓
CNC1-1
        ↓
CNC1-2
        ↓
CNC2
        ↓
IM
        ↓
FA (Final Inspection)
        ↓
PASS → Completed
FAIL → Scrap / Rework
```

---

## 🧩 4. Core Features

### 4.1 Barcode-Based Tracking

* Each part has a **unique barcode**
* Barcode is used to identify and track the part

---

### 4.2 Scan & Move System

* User scans barcode (simulated input)
* System automatically moves part to next station
* Validates correct process flow

---

### 4.3 Workflow Validation

* Enforces correct sequence:

  * DDG → CNC1-1 → CNC1-2 → CNC2 → IM → FA
* Prevents invalid movement

---

### 4.4 Production History Tracking

* Stores each movement:

  * From station
  * To station
  * Timestamp
* Enables full traceability

---

### 4.5 Quality Check (Pass/Fail)

* At FA stage:

  * PASS → Completed
  * FAIL → Scrap or Rework

---

### 4.6 Scrap Management

* Mark defective parts as **SCRAPPED**
* Remove from production flow

---

### 4.7 Rework Process

* Failed parts can be sent for **rework**
* Re-enter workflow after correction

---

### 4.8 Lot Management (Optional)

* Group parts into batches (lots)
* Change lot codes if needed

---

### 4.9 NCM (Non-Conformance Management)

* Create defect record for failed parts
* Track disposal (scrap or rework)

---

## 🗄️ 5. Database Design

### Tables:

#### 1. parts

* id
* barcode (UNIQUE)
* lot_id
* current_station
* status

#### 2. stations

* id
* station_name
* sequence_order

#### 3. production_history

* id
* barcode
* from_station
* to_station
* timestamp

#### 4. lots (optional)

* id
* lot_code
* quantity

#### 5. defects (NCM)

* id
* barcode
* reason
* disposition

---

## 🔌 6. API Endpoints

### Core APIs

| Method | Endpoint           | Description                         |
| ------ | ------------------ | ----------------------------------- |
| POST   | /scan              | Scan barcode & move to next station |
| GET    | /part/{barcode}    | Get part details                    |
| POST   | /quality           | Pass/Fail check                     |
| POST   | /scrap             | Scrap part                          |
| POST   | /rework            | Rework part                         |
| GET    | /history/{barcode} | Get movement history                |

---

### Optional APIs

| Method | Endpoint    | Description          |
| ------ | ----------- | -------------------- |
| POST   | /lot        | Create lot           |
| POST   | /change-lot | Change lot code      |
| POST   | /group      | Group parts          |
| POST   | /ungroup    | Ungroup parts        |
| POST   | /ncm        | Create defect record |

---

## ⚙️ 7. Technology Stack

* Backend: **FastAPI (Python)**
* Database: **PostgreSQL / MySQL**
* ORM: **SQLAlchemy**
* Testing: **Postman**
* Optional Frontend: **Angular**

---

## 🔐 8. Validation & Error Handling

The system must handle:

* Invalid barcode
* Incorrect process flow
* Duplicate scan
* Already completed parts

---

## 📊 9. Future Enhancements

* Authentication (JWT)
* Dashboard (analytics)
* Real-time tracking
* Role-based access (Admin / Operator)

---

## 🏁 10. Expected Outcome

* Fully working backend system
* Real-world MES simulation
* Strong portfolio project for backend roles
* Demonstrates workflow logic + API design

---

## ⭐ 11. Key Learning Outcomes

* REST API design
* Backend architecture
* Database relationships
* Real-world business logic implementation
* Manufacturing system understanding

---


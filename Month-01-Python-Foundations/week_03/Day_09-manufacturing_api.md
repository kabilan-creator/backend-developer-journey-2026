# 📅 Day – Understanding Manufacturing APIs & Backend Architecture

## 📚 What I Learned Today

Today I studied a manufacturing API document and understood how APIs control production workflows in systems like MES (Manufacturing Execution Systems).

---

## 🔹 1️⃣ Understanding APIs in Manufacturing Systems

APIs are used to control and track the production flow of parts inside a factory.

These APIs help manage:

- Production lots
- Machine processes
- Quality inspection
- Scrap and rework
- Defect management

Example API concept:

```http
POST /move-next
```

Used to move parts from one process to the next machine.

---

## 🔹 2️⃣ Lot Management API

Lots represent **batches of parts produced together**.

Example operation:

```http
POST /change-lot
```

Example body:

```json
{
  "part_id": "1234",
  "new_lot_code": "LOT-002"
}
```

Purpose:

- Update production batch information
- Track parts across different processes

---

## 🔹 3️⃣ Move Next Process API

This API moves a part or batch to the **next manufacturing process**.

Example:

```http
POST /move-next
```

Example body:

```json
{
  "part_id": "1234",
  "quantity": 5,
  "next_process": "CNC2"
}
```

This helps track machine workflow transitions.

---

## 🔹 4️⃣ Quality Check API

Used to record inspection results.

Example:

```http
POST /quality-check
```

Example body:

```json
{
  "part_id": "1234",
  "result": "PASS"
}
```

If the part fails inspection, it may go to:

- Scrap
- Rework

---

## 🔹 5️⃣ Scrap API

Used to mark defective parts as waste.

Example:

```http
POST /scrap
```

Example body:

```json
{
  "part_id": "1234",
  "reason": "defect"
}
```

---

## 🔹 6️⃣ Rework API

Used when defective parts can be repaired and reprocessed.

Example:

```http
POST /rework
```

Example body:

```json
{
  "part_id": "1234"
}
```

---

## 🔹 7️⃣ Group & Ungroup APIs

Used to combine multiple parts into a batch or separate them.

Example APIs:

```http
POST /group
POST /ungroup
```

Used for packaging, transport, or assembly operations.

---

## 🔹 8️⃣ Get Lot Details API

Used to retrieve production information about a batch.

Example:

```http
GET /lot-details/{lot_id}
```

Response may contain:

- lot code
- quantity
- process stage
- production status

---

## 🔹 9️⃣ NCM (Non-Conformance Management)

Handles defective parts and quality issues.

Example APIs:

```http
POST /ncm/create
POST /ncm/dispose
```

Used to record and manage defect cases.

---

# 🏭 Complete Manufacturing Workflow

Typical production flow in the system:

```
Create Lot
   ↓
DDG Process
   ↓
CNC1-1
   ↓
CNC1-2
   ↓
CNC2
   ↓
Injection Molding (IM)
   ↓
Final Inspection (FA)
   ↓
PASS → Continue production
FAIL → Scrap or Rework
```

---

# 🧠 Backend Architecture Understanding

I also understood how backend systems handle API requests.

Basic system architecture:

```
Client (UI / Postman)
        ↓
API Server
        ↓
Database Server
```

### Responsibilities

Client  
→ Sends request

API Server  
→ Handles business logic and workflow

Database Server  
→ Stores and retrieves production data

Example request flow:

```
Client → API Server → Database → API Server → Client
```

---

# 💡 Key Concepts I Strengthened Today

- Understanding real manufacturing APIs
- Production workflow tracking
- Backend API architecture
- Lot management systems
- Quality control logic
- Scrap and rework processes
- MES system backend flow

---

# 🚀 How This Helps My Career

Since I work as an **MES Support Engineer**, understanding these APIs helps me learn:

- Manufacturing software architecture
- Production tracking systems
- Backend workflow logic
- Industrial software development

This knowledge is useful for moving toward roles like:

- MES Developer
- Backend Developer
- Manufacturing Software Engineer
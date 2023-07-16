# インストール手順

## 1. flask インストール

```python
pip install flask flask-socketio
or
python -m pip install flask flask-socketio
```

## 2. simple-websocket

`python -m pip install -U simple-websocket`

## 3. ファイル作成

```powershell
mkdir webapp
cd webapp
mkdir templates
new-item templates\index.html
new-item app.py

```

# 起動手順

` python .\app.py`

# ファイル構成

```scss
python_web
│
├─ app.py
│
└─ templates
   │
   └─ index.html


```

# 設計書

## DB

```mermaid
erDiagram
USERS ||--o{  MESSAGES:allows
  USERS {
    int id PK
    string name
    string Email UK
    string img
    timestamp created_at
    timestamp deleted_at
  }

  MESSAGES{
    message_id id PK
    string message
    timestamp created_at
    boolian delete_flag
  }

```

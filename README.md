# Health.me 🩺

A RESTful API that allows users to log, manage, and analyze their daily health data such as sleep, hydration, exercise, and mood. Built with Flask. Shows backend development skills including CRUD operations, API architecture, and data analysis.

## Features

- 📝 Create, Read, Update, Delete (CRUD) daily health entries
- 📊 Generate basic health insights (e.g. weekly sleep averages, mood trends)
- 🔐 Optional: User authentication with JWT
- 💾 MongoDB/PostgreSQL database integration
- 📦 Local deployement, cloud deployment in-progress!
- 🧪 Fully testable via Pytest

## Tech Stack

- Backend: Flask (Python)
- Database: MongoDB 
- Tools: Git, Pytest (SOON)
- Hosting: Local, cloud tbd

## API Endpoints

| Method | Endpoint         | Description                      |
|--------|------------------|----------------------------------|
| POST   | `/entries`       | Create a new health log entry    | DONE
| GET    | `/entries`       | Get all health entries           | DONE
| GET    | `/entries/:id`   | Get a specific entry             | WIP
| PUT    | `/entries/:id`   | Update an entry                  | WIP
| DELETE | `/entries/:id`   | Delete an entry                  | WIP
| GET    | `/insights`      | View summarized health statistics| WIP

## Getting Started



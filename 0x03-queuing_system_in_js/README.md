# 0x03-queuing_system_in_js — Message Queues with Kue & Redis

[![ALX](https://img.shields.io/badge/ALX-Backend%20Engineering-blue?style=flat-square&logo=linux&logoColor=white)](https://www.alxafrica.com/)
[![Node.js](https://img.shields.io/badge/node.js-12+-green.svg)]()
[![Redis](https://img.shields.io/badge/redis-required-red.svg)]()

> **Queuing System** — Asynchronous job processing with Kue (Redis-backed queue) and Express.js.

---

## 🎯 Overview

This project demonstrates message queue patterns for backend systems using **Kue** (a priority job queue for Node.js backed by Redis). Covers job creation, processing, concurrency, and monitoring.

**Note**: This directory contains the project configuration (`package.json`) but source files are not included. Implement the exercises per ALX curriculum requirements.

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| **Runtime** | Node.js 12+ |
| **Queue** | Kue (Redis-backed) |
| **Web Framework** | Express.js |
| **Database** | Redis |
| **Testing** | Mocha, Chai, Sinon |
| **Linting** | ESLint (Airbnb Base) |
| **Transpilation** | Babel 7 |

---

## 📦 Dependencies

```json
{
  "dependencies": {
    "express": "^4.17.1",
    "kue": "^0.11.6",
    "redis": "^2.8.0"
  },
  "devDependencies": {
    "@babel/cli": "^7.8.0",
    "@babel/core": "^7.8.0",
    "@babel/node": "^7.8.0",
    "@babel/preset-env": "^7.8.2",
    "@babel/register": "^7.8.0",
    "chai": "^4.2.0",
    "chai-http": "^4.3.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "mocha": "^6.2.2",
    "nodemon": "^2.0.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
  }
}
```

---

## 🚀 Quick Start

```bash
cd 0x03-queuing_system_in_js

# Install dependencies
npm install

# Start Redis (required)
redis-server

# Run linter
npm run check-lint

# Run tests
npm test

# Development mode
npm run dev
```

---

## 📋 Expected Implementation (Per Curriculum)

Typical exercises for this module:

| Exercise | Description |
|----------|-------------|
| `0-redis_client.js` | Create Redis client, handle connect/error events |
| `1-redis_op.js` | Basic Redis operations (SET, GET, DEL) |
| `2-redis_op_async.js` | Async Redis operations with promises |
| `3-redis_subscriber.js` | Pub/Sub subscriber pattern |
| `4-redis_publisher.js` | Pub/Sub publisher pattern |
| `5-subscriber.js` | Advanced subscriber with channels |
| `6-publisher.js` | Advanced publisher |
| `7-job_creator.js` | Create jobs in Kue queue |
| `8-job_processor.js` | Process jobs from Kue queue |
| `9-job_creator_express.js` | Express endpoint to create jobs |
| `10-job_processor_express.js` | Express + Kue job processing |

---

## 🔧 Kue Basics

```javascript
const kue = require('kue');
const queue = kue.createQueue({ redis: { host: '127.0.0.1', port: 6379 } });

// Create a job
const job = queue.create('email', {
  to: 'user@example.com',
  subject: 'Hello'
}).save();

// Process jobs
queue.process('email', (job, done) => {
  // Send email...
  done();
});

// Monitor queue
kue.app.listen(3000); // UI at http://localhost:3000
```

---

## 📚 Learning Outcomes

- ✅ Redis client operations (sync & async)
- ✅ Pub/Sub messaging patterns
- ✅ Job queues with Kue: creation, processing, priority
- ✅ Express integration for async job APIs
- ✅ Queue monitoring and debugging

---

## 📄 License

MIT License - see root [LICENSE](../LICENSE)
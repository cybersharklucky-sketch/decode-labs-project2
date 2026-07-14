# decode-labs-project2
Python expense tracker where users enter amounts (100, 50, 20). Uses accumulator pattern total = total + new_expense for real-time addition. Displays total spent with professional formatting, statistics, and transaction history. Includes input validation and graceful shutdown.


# 📊 Expense Tracker - Project 2

## A State-Preserving Backend Engine for Financial Data Processing

---

## 📋 Project Overview

Expense Tracker is a professional-grade Python application developed as Project 2 for the DecodeLabs Internship Program (Batch 2026). This project demonstrates fundamental backend engineering concepts through the implementation of a real-time expense tracking system with robust data accumulation and validation.

### 🎯 Project Goals
- Build a script that handles continuous data entry through mathematical and programmatic logic
- Implement the IPO Model (Input → Process → Output) for data processing
- Master accumulator patterns for real-time data accumulation
- Practice defensive coding and input validation
- Create a state-preserving application with graceful shutdown

---

## ✨ Features

### Core Functionality
- ✅ Continuous Data Entry - Add expenses one at a time
- ✅ Real-time Accumulation - Tracks running total instantly
- ✅ Professional Output - Formatted currency display with statistics
- ✅ Input Validation - Prevents string concatenation disasters
- ✅ State Management - Preserves expense history and metadata

### Advanced Features
- 🔒 The Gatekeeper - Robust input validation (Poka-Yoke)
- 🛑 Kill Switch - Graceful shutdown with 'DONE' sentinel
- 📊 Quality Validation - Data integrity verification
- 📈 Transaction History - Complete log of all expenses
- 📉 Statistical Analysis - Average, min, max calculations
- 🎨 Professional UI - Clean, formatted console output

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Installation

```bash
# Clone the repository
git clone https://github.com/cybershark-lucky/expense-tracker.git

# Navigate to project directory
cd decode-labs-project2

# Run the application
python expense_tracker.py

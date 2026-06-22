# 🔐 SOC Password Fortification Tool

A command-line security utility built with pure Python fundamentals that audits password strength and generates fortress-level alternatives.

## 🎯 The Problem
Most password tools are either too basic (just random characters) or too weak (allow common patterns like "password123"). Users need a tool that:
- Analyzes existing passwords for real vulnerabilities
- Generates strong passwords that are still memorable
- Uses cybersecurity terminology (relevant for SOC Analysts)

## ✅ What This Tool Does
| Feature | Description |
|---------|-------------|
| **Security Audit** | Checks length, character types, and weak patterns |
| **Scoring System** | 0–100 score with ratings: CRITICAL / MODERATE / FORTIFIED |
| **Pattern Detection** | Detects common weak strings like "123", "password", "qwerty" |
| **Fortress Generator** | Creates 20–25 character passwords using cyber-words with random case scrambling |
| **Entropy Injection** | Adds random digits and symbols, then shuffles everything |

## 🛠️ Built With
- **Python 3** — No external libraries
- **Concepts Used:** Variables, Input/Output, Type Conversion, f-Strings, Lists, Nested Lists, For Loops, Nested Loops, Random Module, Conditional Logic

## 🚀 How to Run
```bash
python soc-password-fortification.py

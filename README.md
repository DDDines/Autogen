# Autogen Project Setup Guide

This guide provides detailed steps to set up the Autogen project environment to explore examples including two-way chat functionalities using the OpenAI API.

## Prerequisites

Before you begin, make sure you have the following:

- A GitHub account
- An account on OpenAI to access API keys

## Setup Instructions

### 1. Obtain API Keys

- **OpenAI API Key**: You will need an API key from OpenAI to interact with their APIs. Obtain your API key [here](https://platform.openai.com/api-keys).

### 2. Autogen Documentation

- Before starting, familiarize yourself with the Autogen documentation available [here](https://microsoft.github.io/autogen/docs/installation/).

### 3. Environment Setup

Set up your Python environment using the following commands:

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment on Windows
.\.venv\Scripts\activate

# Activate the virtual environment on Unix/MacOS
source .venv/bin/activate
```

### 4. Install Required Packages

Install the necessary Python packages using pip:

```bash
pip install pyautogen
```

### 5. Configuration

Exploring the Examples
Once the setup is complete, you are ready to explore the files and run the examples:

Start with the 01-twoway-chat script to understand how to interact with the OpenAI API using Autogen.

### Conclusion

By following these instructions, you should have a functional setup to explore the Autogen examples. Dive into the scripts to learn more about how they work and what you can achieve with the tools provided.

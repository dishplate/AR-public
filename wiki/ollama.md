# Ollama cheatsheet

## Ollama setup
After installation via https://ollama.com
Look at the latest models and choose one that works for your system etc.
https://ollama.com/search

## List Models: List all available models using the command:
ollama list

## Remove a Model: Remove a model using the command
ollama rm model_name

## Download the model
ollama pull gpt-oss:latest
ollama pull deepseek-r1:8b

## Start Ollama
ollama serve

## List the models
ollama ls

## Run the model
ollama run gpt-oss:latest

## Check what is running
ollama ps

## Stop a model
ollama stop gpt-oss:latest

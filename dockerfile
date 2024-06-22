# Dockerfile
FROM python:3.8-slim
# Set the working directory in the container
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install accelerate==0.21.0
RUN pip install peft==0.4.0
RUN pip install bitsandbytes==0.40.2
RUN pip install transformers==4.31.0
RUN pip install trl==0.4.7
RUN pip install openai
RUN pip install pandas
RUN pip install langchain==0.0.299
RUN pip install torch
RUN pip install flask 
RUN pip install scipy 

# Make port 5000 available to the world outside this container
EXPOSE 5000
# Define environment variable
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV TF_ENABLE_ONEDNN_OPTS=0
ENV TF_CPP_MIN_LOG_LEVEL=1

# write the CMD command using python to run server.py
CMD ["python3", "server.py"]

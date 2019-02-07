# Use an official Python runtime as a parent image
FROM python:3.7.2-alpine3.9

# Set the working directory to /app
WORKDIR /myflix

# Copy the current directory contents into the container at /app
COPY . /myflix

# Install any needed packages specified in requirements.txt
RUN \
 pip install --trusted-host pypi.python.org -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
CMD ["python3", "video.py"]
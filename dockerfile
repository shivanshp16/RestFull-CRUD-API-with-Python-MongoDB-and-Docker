#Pulling required images 
FROM mongo:3.6.4             

FROM python:3

#Changing working directory
WORKDIR /app

#Coping requirements file to Docker Directory
COPY /requirements.txt /app

#Installing reuqired dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

#Exposing the default ports
EXPOSE 27017
EXPOSE 5000

#Coping everything in the same forlder to Docker Directory
COPY ["MongoDB API.py", "/app"]
COPY . .

#Executing MongoDB API.py with python3
CMD ["python3","MongoDB API.py"]
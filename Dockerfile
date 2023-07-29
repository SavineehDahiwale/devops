FROM 192.168.0.10:5000/python
WORKDIR /src
RUN pip install flask
COPY . .
EXPOSE 4001
CMD python app.py


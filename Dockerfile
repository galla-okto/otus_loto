FROM python:3.6
COPY main.py /main.py
RUN chmod +x /main.py
CMD python /main.py
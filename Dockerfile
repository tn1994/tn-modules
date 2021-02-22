FROM python:3.6

RUN pip install --upgrade pip
RUN pip install pandas \
                tabulate
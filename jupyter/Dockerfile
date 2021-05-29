# using python 3.7
FROM python:3.7-slim 

# create a source directory and change to that directory
RUN mkdir src
WORKDIR /src

# copy python requirements into docker container
COPY ./requirements.txt ./

# install jupyter notebook for data analysis
RUN pip3 install notebook

# install pandas, plotly, scikit-learn and matplotlib
RUN pip install -r requirements.txt

# run a notebook on port 8888 at address 0.0.0.0, no browser keeps the machine from opening a session,
# and allow root access boots from docker command line
CMD [ "jupyter", "notebook", "--port=8888", "--no-browser" , "--ip=0.0.0.0", "--allow-root"]

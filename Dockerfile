FROM python:3.9
LABEL Evgeny Kren <tikshike@gmail.com>

# Create parent directory and copy main project files
RUN mkdir -p g_task && cd g_task
WORKDIR /g_task
COPY ./src /g_task

# Setup virtual environment for python
ENV VENV=/g_venv
RUN python3 -m venv $VENV
ENV PATH="$VENV/Scripts:$PATH"

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt


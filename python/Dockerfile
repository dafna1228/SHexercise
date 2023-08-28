# Build the Python container
FROM python:3.10-slim@sha256:2bac43769ace90ebd3ad83e5392295e25dfc58e58543d3ab326c3330b505283d
RUN groupadd -g 999 fibi && \
    useradd -r -u 999 -g fibi fibi
USER 999
WORKDIR /usr/app
COPY . .
ENV PATH="/usr/app/venv/bin:$PATH"
CMD [ "python", "main.py" ]

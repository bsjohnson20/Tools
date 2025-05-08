FROM ubuntu:24.04


WORKDIR /app
RUN apt-get update && apt-get install -y wget cargo libxml2-dev libxslt-dev 7zip
COPY src/ /app
RUN rm -rf /app/.venv
RUN wget -qO- https://astral.sh/uv/install.sh | sh

# Update path
ENV PATH="/root/.local/bin:${PATH}"
RUN uv sync
# RUN pip install -r requirements.txt
# RUN source .venv/bin/activate
ENV PATH="/app/.venv/bin:$PATH"
ENTRYPOINT [ "bash","./run.sh" ]

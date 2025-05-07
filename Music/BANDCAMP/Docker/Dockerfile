FROM python:3.14-rc-slim-bookworm


WORKDIR /app
RUN apt-get update && apt-get install -y wget
COPY src/ /app
# COPY run.sh /app
# RUN wget -qO- https://astral.sh/uv/install.sh | sh

# Update path
# ENV PATH="/root/.local/bin:${PATH}"
# RUN uv sync
# RUN pip install -r requirements.txt
# RUN source .venv/bin/activate
ENV PATH="/app/.venv/bin:$PATH"
ENTRYPOINT [ "bash","./run.sh" ]

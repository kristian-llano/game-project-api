#!/bin/bash

curl "http://localhost:8000/characters/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "character": {
      "name": "'"${NAME}"'",
      "classes": "'"${CLASSES}"'",
      "level": "'"${LEVEL}"'"
    }
  }'

echo

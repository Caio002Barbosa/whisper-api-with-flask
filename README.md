# Whisper API with flask

## Description

This is a Python project that uses Flask and Flasgger to create a web API for transcribing audio files. The transcription is done using the `whisper` library.

## Installation

1. Clone this repository.
2. Install Docker and Docker Compose if you haven't already.
3. Build the Docker image by running `docker-compose build`.

## Usage

1. Start the server by running `docker-compose up`.
2. Send a POST request to `http://localhost:5000/transcribe` with an audio file in the form data under the key `audio`.

## API Endpoints

- `POST /transcribe`: Transcribes an audio file. The audio file should be included in the form data under the key `audio`.

### Example

Here's an example of how to use the `/transcribe` endpoint:

**Request:**

```bash
curl -X POST -F "audio=@path_to_your_audio_file.wav" http://localhost:5000/transcribe
```

**Response:**

```json
{
  "text": "transcribed text from the audio file"
}
```
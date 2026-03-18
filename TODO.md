# Gemini Sandbox Plan

- [x] **Phase 1: Dockerfile Creation**
    - [x] Create a `Dockerfile` for the Gemini Sandbox.
    - [x] Base Image: `ubuntu:24.04`.
    - [x] Install Core Tools: `git`, `curl`, `wget`, `sudo`, `ca-certificates`.
    - [x] Install Development Tools: `python3`, `python3-pip`, `nodejs`, `npm`.
    - [x] Install Gemini CLI & Agent Development Kit.
    - [x] Configure User: Create a user inside the container matching your UID/GID.
- [x] **Phase 2: Build & Start Sandbox**
    - [x] Build the image: `podman build -t gemini-sandbox .`.
    - [x] Create & Run the persistent container with volume mount: `~/projects` -> `/home/raytiong/projects`.
    - [x] Configure the container to auto-restart.
- [x] **Phase 3: Integration & Testing**
    - [x] Add a shell alias `gemini-shell` to easily enter the sandbox.
    - [x] Verify `git`, `node`, `python`, and volume access inside the sandbox.
    - [x] Test Gemini CLI and Agent Development Kit connectivity.

## Status: Complete
The sandbox is now ready! You can enter it by typing `gemini-shell` in your terminal. All your work in `~/projects` on your Mac will be synced with the sandbox.

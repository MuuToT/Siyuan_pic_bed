# SiYuan Picture Bed Controller

A FastAPI-based web application that serves as a controller for managing SiYuan notebook resources, particularly images, across different cloud storage services.

## Features

- **SiYuan Integration**: Seamlessly integrates with SiYuan notebooks
- **Multi-Cloud Support**: Upload resources to different cloud storage services:
    - 123 Cloud Drive (123云盘)
    - PicGo
    - SiYuan's native storage
- **Resource Management**:
    - Download resources from SiYuan notebooks
    - Upload resources from notebooks to cloud storage
    - Upload resources from specific blocks
    - Upload resources from databases
- **Cloud Optimization**:
    - Detect and remove duplicate resources in cloud storage
    - Identify and clean up unused resources
    - Maintain a cache of remote resources for better performance
- **Document Icon Management**: Replace document icons across notebooks

## Requirements

- Python 3.13 or higher
- Dependencies (automatically installed with pip):
    - FastAPI
    - Uvicorn
    - Aiohttp
    - Pydantic
    - And other dependencies listed in pyproject.toml

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/siyuan-pic-bed-ctl.git
   cd siyuan-pic-bed-ctl
   ```

2. Install the package and its dependencies:
   ```bash
   pip install -e .
   ```

3. Build:
   ```bash
   pyinstaller --onefile --name=py_server .\main.py
   ```

## Usage

### Starting the Server

Run the application:

```bash
python main.py
```

The server will start on the host and port specified in the settings module.

### API Endpoints

The application provides several API endpoints:

- **Base Endpoints**:
    - `/`: Root endpoint that returns a hello world message
    - `/exit`: Gracefully shuts down the server

- **SiYuan Endpoints** (`/siyuan`):
    - `/notebooks`: Manage notebook resources (download/upload)
    - `/blocks`: Manage block resources
    - `/database`: Manage database resources
    - `/icon`: Replace document icons

- **Remote Endpoints** (`/remote`):
    - `/repeat`: Check for duplicate resources in cloud storage
    - `/redundancy`: Identify unused resources in cloud storage
    - `/reload`: Refresh the cache for a specific remote service

- **Configuration Endpoints** (`/config`):
    - Configure connections to different services

### Authentication

API requests require a token for authentication. The token is validated to ensure the requested service is properly initialized.

## Configuration

The application uses a configuration manager to handle settings for different services. Each service (SiYuan, 123 Cloud Drive, PicGo) needs to be initialized before use.

## License

This project is licensed under the GNU General Public License v3.0 (GPLv3) - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

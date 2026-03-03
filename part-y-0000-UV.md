$env:UV_INSTALL_DIR = "D:\uvfile"

$env:UV_PYTHON_INSTALL_DIR = "D:\uvfile\python"

$env:UV_CACHE_DIR = "D:\uvfile\cache"

if (!(Test-Path "D:\uvfile")) { New-Item -ItemType Directory -Path "D:\uvfile" -Force }

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

uv --version

uv self update

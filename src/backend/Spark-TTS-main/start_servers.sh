#!/bin/bash

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Voice NFT Trading Platform - TTS Server${NC}"
echo "=================================================="

# Check if model exists
echo -e "${YELLOW}Checking Spark-TTS model...${NC}"
if [ ! -d "pretrained_models/Spark-TTS-0.5B" ]; then
    echo -e "${RED}❌ Spark-TTS model not found. Please download it first.${NC}"
    echo "Run: python download_model.py"
    exit 1
else
    echo -e "${GREEN}✅ Spark-TTS model ready${NC}"
fi

# Install dependencies
echo -e "${YELLOW}Installing Python dependencies...${NC}"
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to install dependencies${NC}"
    exit 1
fi

# Create necessary directories
echo -e "${YELLOW}Creating directories...${NC}"
mkdir -p results prompts

# Start TTS server
echo -e "${YELLOW}Starting TTS server...${NC}"
echo -e "${GREEN}✅ TTS server starting on http://localhost:5000${NC}"
echo "Press Ctrl+C to stop the server"
echo ""

python webui.py
#!/bin/bash

# Production startup script for AgenticSeek

echo "🚀 Starting AgenticSeek in Production Mode..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found. Please create one based on .env.production.example"
    exit 1
fi

# Check if OpenAI API key is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ OPENAI_API_KEY environment variable is not set"
    echo "Please set it in your .env file or export it:"
    echo "export OPENAI_API_KEY='your_api_key_here'"
    exit 1
fi

# Create necessary directories
mkdir -p workspace screenshots

# Load environment variables
export $(cat .env | xargs)

# Start services
echo "📦 Starting services with Docker Compose..."
docker-compose -f docker-compose.production.yml up -d

echo "⏳ Waiting for services to start..."
sleep 10

# Check if services are running
if docker-compose -f docker-compose.production.yml ps | grep -q "Up"; then
    echo "✅ Services started successfully!"
    echo ""
    echo "🌐 AgenticSeek is now running at:"
    echo "   Frontend: http://localhost:3000"
    echo "   Backend API: http://localhost:8000"
    echo "   SearXNG: http://localhost:8080"
    echo ""
    echo "📝 To view logs:"
    echo "   docker-compose -f docker-compose.production.yml logs -f"
    echo ""
    echo "🛑 To stop services:"
    echo "   docker-compose -f docker-compose.production.yml down"
else
    echo "❌ Failed to start services. Check logs:"
    docker-compose -f docker-compose.production.yml logs
    exit 1
fi
# AgenticSeek Deployment Guide

## Deploy to Render.com

### Prerequisites
1. GitHub account with agenticSeek_v1 repository
2. Render.com account
3. OpenAI API key

### Step-by-Step Deployment

#### 1. Connect Repository to Render
1. Go to [Render.com](https://render.com) and sign in
2. Click "New +" → "Web Service"
3. Connect your GitHub account if not already connected
4. Select the `vuhaininh/agenticSeek_v1` repository

#### 2. Configure Web Service
Use these settings:

**Basic Settings:**
- **Name**: `agenticseek-backend` (or your preferred name)
- **Environment**: `Docker`
- **Region**: Choose closest to your users
- **Branch**: `main`

**Build & Deploy:**
- **Dockerfile Path**: `Dockerfile.production`
- **Docker Command**: Leave empty (uses CMD from Dockerfile)

**Advanced Settings:**
- **Auto-Deploy**: Yes (recommended)

#### 3. Environment Variables
Add these environment variables in Render dashboard:

**Required:**
- `OPENAI_API_KEY`: Your OpenAI API key
- `ENVIRONMENT`: `production`

**Optional (for enhanced features):**
- `REDIS_URL`: Leave empty for now (Redis not required for basic functionality)
- `CELERY_BROKER_URL`: Leave empty for now

#### 4. Deploy
1. Click "Create Web Service"
2. Wait for the build to complete (5-10 minutes)
3. Your app will be available at the provided Render URL

### Configuration Files

The deployment uses these production-optimized files:

- **`render.yaml`**: Render.com service configuration
- **`Dockerfile.production`**: Production Docker configuration with Chromium
- **`requirements.production.txt`**: Python dependencies without audio packages
- **`config.production.ini`**: Production configuration with OpenAI provider

### Features Available in Production

✅ **Available:**
- Web search and scraping
- OpenAI integration (GPT models)
- Browser automation (Chromium)
- File processing
- API endpoints

❌ **Disabled in Production:**
- Audio recording (microphone input)
- Text-to-speech output
- Audio file processing

### Troubleshooting

#### Build Failures
If build fails, check the build logs for:
1. **ChromeDriver issues**: Fixed by using Chromium from Debian repos
2. **Audio package compilation errors**: Fixed by excluding from production requirements
3. **Memory issues**: Render free tier has limited resources

#### Runtime Issues
1. **OpenAI API errors**: Verify API key is set correctly
2. **Browser automation fails**: Check if Chromium is properly installed
3. **Import errors**: Audio packages are optional and should not crash the app

### Scaling and Performance

**Free Tier Limitations:**
- 512MB RAM
- Sleeps after 15 minutes of inactivity
- Limited CPU

**Paid Tier Benefits:**
- More RAM and CPU
- No sleep mode
- Better performance for browser automation

### Adding Redis (Optional)

For enhanced performance with background tasks:

1. Create Redis service on Render:
   - Go to "New +" → "Redis"
   - Note the Redis URL

2. Update environment variables:
   - `REDIS_URL`: Your Redis connection string
   - `CELERY_BROKER_URL`: Same as Redis URL

3. Redeploy the service

### Frontend Deployment (Future)

The current deployment only includes the backend API. To add the frontend:

1. Uncomment frontend service in `render.yaml`
2. Configure static site deployment
3. Update CORS settings in backend

### Support

If you encounter issues:
1. Check Render build/deploy logs
2. Verify environment variables
3. Test API endpoints manually
4. Check GitHub repository for latest updates

---

**Last Updated**: 2025-05-30
**Version**: Production-ready with Chromium and optional audio packages
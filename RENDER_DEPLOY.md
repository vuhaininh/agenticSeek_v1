# 🚀 Quick Deploy to Render.com

## 1. Create Web Service
1. Go to [Render.com](https://render.com) → "New +" → "Web Service"
2. Connect GitHub and select `vuhaininh/agenticSeek_v1`
3. Use these settings:
   - **Environment**: Docker
   - **Dockerfile Path**: `Dockerfile.production`
   - **Branch**: main

## 2. Set Environment Variables
Add in Render dashboard:
```
OPENAI_API_KEY=sk-your-openai-api-key-here
ENVIRONMENT=production
```

## 3. Deploy
Click "Create Web Service" and wait 5-10 minutes.

## 4. Test Your Deployment
Your API will be available at: `https://your-app-name.onrender.com`

Test endpoints:
- `GET /health` - Health check
- `POST /search` - Search functionality

## 📖 Full Guide
See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions and troubleshooting.

---
**Ready to deploy!** ✅ All deployment issues have been fixed:
- ✅ ChromeDriver → Chromium (no download issues)
- ✅ Audio packages → Optional (no build failures)  
- ✅ Redis/Celery → Optional (no runtime crashes)
- ✅ OpenAI integration → Ready for your API key
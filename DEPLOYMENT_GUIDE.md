# 🚀 Hướng dẫn Deploy AgenticSeek lên Cloud

## Chuẩn bị

### 1. Cấu hình OpenAI API Key

Tạo file `.env` từ template:
```bash
cp .env.production.example .env
```

Chỉnh sửa file `.env` và thêm OpenAI API key của bạn:
```
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
```

### 2. Test Local trước khi deploy

```bash
# Chạy production mode locally
./start_production.sh

# Kiểm tra tại http://localhost:3000
```

## Deploy lên Render.com

### Option 1: Deploy Backend + Frontend riêng biệt (Khuyến nghị)

#### A. Deploy Backend (Web Service)

1. **Tạo Web Service mới trên Render.com**
2. **Connect GitHub repository** của bạn
3. **Cấu hình Build & Deploy:**
   ```
   Build Command: pip install -r requirements.txt
   Start Command: python api.py
   ```
4. **Environment Variables:**
   ```
   ENVIRONMENT=production
   OPENAI_API_KEY=sk-your-actual-api-key
   REDIS_URL=redis://localhost:6379/0
   ```
5. **Advanced Settings:**
   - Docker: Enabled
   - Dockerfile Path: `Dockerfile.production`

#### B. Deploy Frontend (Static Site)

1. **Tạo Static Site mới**
2. **Connect repository** (same repo, folder: `frontend/agentic-seek-front`)
3. **Build Settings:**
   ```
   Build Command: npm install && npm run build
   Publish Directory: build
   ```
4. **Environment Variables:**
   ```
   REACT_APP_BACKEND_URL=https://your-backend-url.onrender.com
   ```

### Option 2: Deploy với Docker (Single Service)

1. **Tạo Web Service**
2. **Docker Configuration:**
   ```
   Dockerfile: Dockerfile.production
   ```
3. **Environment Variables:**
   ```
   ENVIRONMENT=production
   OPENAI_API_KEY=sk-your-actual-api-key
   ```

## Deploy lên các platform khác

### Heroku

1. **Tạo app mới:**
   ```bash
   heroku create your-app-name
   ```

2. **Set environment variables:**
   ```bash
   heroku config:set ENVIRONMENT=production
   heroku config:set OPENAI_API_KEY=sk-your-api-key
   ```

3. **Deploy:**
   ```bash
   git push heroku main
   ```

### Railway

1. **Connect GitHub repository**
2. **Set environment variables** trong dashboard
3. **Deploy automatically** từ main branch

### DigitalOcean App Platform

1. **Create App từ GitHub**
2. **Configure build settings:**
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `python api.py`
3. **Set environment variables**

## Cấu hình Domain và HTTPS

### Custom Domain
1. Thêm domain trong platform settings
2. Cập nhật DNS records
3. Enable HTTPS/SSL

### Environment Variables cho Production
```
ENVIRONMENT=production
OPENAI_API_KEY=sk-your-actual-api-key
REDIS_URL=redis://your-redis-url
SEARXNG_URL=http://your-searxng-url
```

## Monitoring và Logs

### Xem logs
```bash
# Render.com: Check logs trong dashboard
# Heroku: heroku logs --tail
# Railway: Check logs trong dashboard
```

### Health Check
- Backend: `https://your-app.onrender.com/health`
- Frontend: `https://your-frontend.onrender.com`

## Troubleshooting

### Common Issues

1. **ChromeDriver issues:**
   - Đảm bảo Dockerfile.production có cài đặt Chrome và ChromeDriver
   - Set `headless_browser = True` trong config

2. **API Key errors:**
   - Kiểm tra OPENAI_API_KEY đã set đúng
   - Verify API key còn valid và có credits

3. **CORS errors:**
   - Cập nhật allowed_origins trong api.py
   - Set CORS cho production domain

4. **Memory issues:**
   - Upgrade plan nếu cần
   - Optimize model usage

### Performance Tips

1. **Caching:** Enable Redis caching
2. **CDN:** Use CDN cho static assets
3. **Monitoring:** Setup monitoring alerts
4. **Scaling:** Configure auto-scaling

## Security Considerations

1. **API Keys:** Không commit API keys vào git
2. **CORS:** Restrict origins cho production
3. **Rate Limiting:** Implement rate limiting
4. **HTTPS:** Always use HTTPS trong production

## Cost Optimization

1. **OpenAI Usage:** Monitor API usage
2. **Server Resources:** Right-size your instances
3. **Caching:** Implement caching để giảm API calls
4. **Sleep Mode:** Use sleep mode cho dev environments
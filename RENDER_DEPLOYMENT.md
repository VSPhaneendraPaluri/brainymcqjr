# Render.com Deployment Guide - BrainyMCQ Junior

## Prerequisites
- GitHub account (repository must be hosted on GitHub)
- Render.com account (free tier available)
- Git installed locally

## Step-by-Step Deployment

### 1. Push to GitHub
```bash
git add .
git commit -m "Add Render deployment configuration"
git push origin main
```

### 2. Create Render Account & Connect GitHub
1. Visit [https://render.com](https://render.com)
2. Sign up with GitHub account (or sign in if you already have an account)
3. Click **"Connect GitHub"** and authorize Render to access your repositories
4. After authorization, return to Render dashboard

### 3. Deploy Using render.yaml (Recommended)

#### Option A: Automatic Deployment (Infrastructure as Code)
1. Go to [https://dashboard.render.com/blueprints](https://dashboard.render.com/blueprints)
2. Click **"New Blueprint"**
3. Select your GitHub repository
4. Choose the `render.yaml` file when prompted
5. Render will automatically:
   - Create a PostgreSQL database
   - Deploy the web service
   - Configure environment variables

#### Option B: Manual Deployment (Using Procfile)
1. In Render dashboard, click **"New+"** → **"Web Service"**
2. Select your GitHub repository
3. Configure:
   - **Name**: `brainymcq-junior` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --worker-class sync --workers 4 --bind 0.0.0.0:$PORT --timeout 120 "app:create_app()"`
   - **Plan**: Free (or paid as needed)

4. Click **"Create Web Service"**

### 4. Configure PostgreSQL Database

#### If Using Blueprint (render.yaml):
- Database is automatically created and connected

#### If Using Manual Deployment:
1. In Render dashboard, click **"New+"** → **"PostgreSQL"**
2. Configure:
   - **Name**: `brainymcq-db`
   - **Database**: `brainymcq`
   - **User**: `brainymcq`
   - **Plan**: Free
   - **Region**: Choose closest to you
3. Click **"Create Database"**

### 5. Set Environment Variables

Go to your Web Service settings → **"Environment"**

Add these variables:
| Variable | Value | Example |
|----------|-------|---------|
| `FLASK_ENV` | `production` | `production` |
| `DATABASE_URL` | Get from PostgreSQL service (Internal Database URL) | `postgresql://...` |
| `SECRET_KEY` | Generate a secure random string | (Use Render's "Generate" feature) |
| `PYTHON_VERSION` | `3.11` | `3.11` |

**To get DATABASE_URL from your PostgreSQL service:**
1. Go to your PostgreSQL database settings in Render
2. Copy the **"Internal Database URL"**
3. Paste into Web Service's `DATABASE_URL` environment variable

### 6. Deploy & Test

1. Once all variables are set, Render automatically deploys
2. Watch the **"Logs"** section for deployment progress
3. Once deployment completes, visit your service URL (e.g., `https://brainymcq-junior.onrender.com`)

### 7. First Run Database Setup

The app will:
- Automatically create database tables
- Seed questions on first run
- Create admin functionality

## Useful Render Commands

### View Logs
- Dashboard → Your Service → "Logs"
- Check for any errors during startup

### Redeploy
- Dashboard → Your Service → "Manual Deploy" → "Latest Commit"

### Database Access
- Connect to PostgreSQL using a client tool
- Dashboard → PostgreSQL → "Connect"
- Copy connection details

## Troubleshooting

### Common Issues

#### 1. **502 Bad Gateway or Deployment Fails**
**Check:**
- Logs for Python/Flask errors
- `DATABASE_URL` is correctly set
- `SECRET_KEY` is set
- Requirements.txt has all dependencies

**Solution:**
```bash
# Redeploy latest commit
# In Render dashboard → "Manual Deploy"
```

#### 2. **Database Connection Error**
**Check:**
- PostgreSQL service is running
- `DATABASE_URL` matches your PostgreSQL settings
- Database user has correct permissions

**Solution:**
- Verify "Internal Database URL" in PostgreSQL settings
- Update `DATABASE_URL` in Web Service environment

#### 3. **Static Files Not Loading**
- CSS/JS files appear broken
- Already handled by render.yaml and Procfile
- If issues persist, ensure `static/` folder is committed to Git

#### 4. **Authentication Issues**
- Users can't log in
- Check database tables are created
- Review application logs in Render dashboard

### Check Logs
```
Render Dashboard → Your Service → "Logs" tab
```

## Post-Deployment Configuration

### 1. Update Your Domain
- **Free domain**: `yoursvc.onrender.com` (automatic)
- **Custom domain**: 
  - Dashboard → Settings → Custom Domain
  - Add your domain (e.g., `brainymcqjunior.com`)
  - Follow DNS configuration instructions

### 2. Enable Auto-Deployment
- Dashboard → Settings → "Auto-Deploy"
- Select "Yes" for branch (usually `main`)
- Service auto-deploys on every push

### 3. Monitor Performance
- Dashboard → Metrics tab
- View CPU, Memory, Request rates

## Scaling Up

When free tier limits are reached:
1. Dashboard → Settings → Plan
2. Upgrade from Free to Starter ($7/month)
3. Includes 2.5GB RAM, 0.5 CPU

## Important Notes

⚠️ **Render Free Tier Limitations:**
- Services spin down after 15 minutes of inactivity
- First request after spin-down takes ~30 seconds
- Database has 100MB storage limit
- Consider upgrading for production use

✅ **What's Included:**
- Free SSL/HTTPS certificate (auto-renewed)
- PostgreSQL database
- Environment variable management
- Automatic deployments
- GitHub integration

## Support & Resources

- **Render Docs**: https://render.com/docs
- **Flask Deployment**: https://render.com/docs/deploy-flask
- **Environment Variables**: https://render.com/docs/environment-variables
- **GitHub Issues**: Check your repository issues

## Next Steps

1. Test all quiz functionality:
   - User registration
   - User login
   - Taking a quiz
   - Viewing results

2. Monitor first few days of logs for any runtime issues

3. Set up custom domain when ready

4. Consider upgrading plan for production workload

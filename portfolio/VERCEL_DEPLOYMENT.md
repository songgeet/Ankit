# Vercel Deployment Guide

## Prerequisites
- Vercel Account: https://vercel.com
- Git Repository connected to Vercel

## Setup Instructions

### 1. Configure Environment Variables in Vercel

Go to your Vercel project settings and add these environment variables:

```
SECRET_KEY=your-django-secret-key
DEBUG=False
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 2. Push to Git

```bash
git add .
git commit -m "Configure Vercel deployment"
git push origin main
```

### 3. Deploy to Vercel

Option A: Automatic (Recommended)
- Vercel will automatically deploy on every push to main

Option B: Manual Deploy
```bash
vercel --prod
```

## What Was Fixed

✅ Updated `vercel.json` with proper build configuration
✅ Added `buildCommand` to collect static files
✅ Configured environment variables support via python-decouple
✅ Added `.vercelignore` to exclude unnecessary files
✅ Updated `wsgi.py` for Vercel compatibility
✅ Updated `requirements.txt` with pinned versions
✅ Created `.env.example` for configuration template

## Important Notes

- Static files are served via WhiteNoise middleware
- Database is SQLite (stored in project)
- Email configuration uses Gmail SMTP
- All sensitive data should be in environment variables
- Max function duration set to 30 seconds (adjust if needed)

## Troubleshooting

If deployment fails:
1. Check Vercel logs: `vercel logs`
2. Ensure all dependencies are in `requirements.txt`
3. Verify environment variables are set
4. Check for missing migrations: `python manage.py migrate`

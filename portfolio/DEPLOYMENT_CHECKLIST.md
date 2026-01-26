# Deployment Checklist ✅

## Pre-Deployment Setup (Local)

### 1. Environment Variables
- [x] `.env` file created with all required variables
- [x] `.env.example` updated with template
- [x] `.gitignore` includes `.env` to prevent committing secrets
- [x] All sensitive credentials in `.env` (not in settings.py)

```bash
# Verify by running:
python manage.py check
```

### 2. Security Settings
- [x] SECRET_KEY - requires environment variable (no default)
- [x] DEBUG=False in production (set via .env)
- [x] ALLOWED_HOSTS configured for your domain
- [x] CSRF_TRUSTED_ORIGINS set for custom domain
- [x] SECURE_SSL_REDIRECT enabled in production
- [x] SESSION_COOKIE_SECURE enabled
- [x] CSRF_COOKIE_SECURE enabled
- [x] HSTS headers configured

### 3. Django App Setup
- [x] `home` app added to INSTALLED_APPS
- [x] Contact form (forms.py) created
- [x] Email configuration with Gmail SMTP
- [x] URLs properly included in main urls.py
- [x] Views handle both regular and AJAX requests
- [x] Static files configured with WhiteNoise

### 4. Vercel Configuration
- [x] `vercel.json` - build commands configured
- [x] `build.sh` - static files collection script
- [x] `.vercelignore` - unnecessary files excluded
- [x] `requirements.txt` - all dependencies pinned

### 5. Git & Version Control
- [x] `.gitignore` created and configured
- [ ] Git repository initialized: `git init`
- [ ] Remote added: `git remote add origin <repo-url>`
- [ ] Files staged: `git add .`
- [ ] Initial commit: `git commit -m "Initial portfolio project"`
- [ ] Pushed to GitHub: `git push -u origin main`

---

## Vercel Deployment Steps

### 1. Create Vercel Account & Link Repository
1. Go to https://vercel.com
2. Sign up / Login
3. Import your GitHub repository
4. Select "Django" as framework preset

### 2. Configure Environment Variables in Vercel Dashboard

Go to **Project Settings → Environment Variables** and add:

```
SECRET_KEY=<your-django-secret-key>
DEBUG=False
EMAIL_HOST_USER=<your-gmail>
EMAIL_HOST_PASSWORD=<your-app-password>
```

**⚠️ Important:** Use Gmail App Password, not regular password!

To generate Gmail App Password:
1. Enable 2-factor authentication on Google Account
2. Go to https://myaccount.google.com/apppasswords
3. Select Mail → Windows Computer
4. Copy the 16-character password

### 3. Deploy
- [x] Configure build command in Vercel: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- [x] Configure start command: (Vercel auto-detects WSGI)
- [x] Click "Deploy"

### 4. Post-Deployment Verification

After deployment completes:

```bash
# Test the deployment
curl https://your-vercel-domain.vercel.app
```

Check:
- [ ] Homepage loads without errors
- [ ] Images and CSS load correctly
- [ ] Contact form sends emails
- [ ] No 404 errors for static files

---

## Potential Issues & Solutions

### Issue: "SECRET_KEY not found"
**Solution:** Add `SECRET_KEY` to Vercel environment variables

### Issue: "Static files not loading (404)"
**Solution:** 
- Ensure `collectstatic` runs during build
- Check `STATIC_ROOT` and `STATICFILES_DIRS` in settings.py
- Verify WhiteNoise middleware is enabled

### Issue: "Email not sending"
**Solution:**
- Verify EMAIL credentials in Vercel environment
- Use Gmail App Password (not regular password)
- Check Gmail "Less secure apps" or enable App Passwords
- Test locally first with `.env` file

### Issue: "CSRF token missing" on custom domain
**Solution:**
- Add your domain to `CSRF_TRUSTED_ORIGINS` in settings.py
- Domain must match exactly (include www)

### Issue: "Database errors" on redeploy
**Solution:**
- SQLite doesn't persist on Vercel - this is expected
- Contact form data goes to email anyway (no database storage needed)
- If you need persistent storage, migrate to PostgreSQL

---

## Important Notes

⚠️ **Gmail 2FA Security:**
- Regular Gmail passwords won't work for SMTP
- You MUST use App Password from Google Account Settings
- Generate at: https://myaccount.google.com/apppasswords

⚠️ **Production Security:**
- Never commit `.env` file (it's in `.gitignore`)
- Always use environment variables for secrets
- Keep `DEBUG=False` in production
- Use HTTPS only (Vercel provides free SSL)

✅ **After Successful Deployment:**
1. Test all features (contact form, downloads, links)
2. Check Google PageSpeed Insights
3. Set up Vercel Analytics
4. Enable automatic deployments on Git push
5. Set up custom domain DNS records

---

## Quick Reference

```bash
# Local Development
python manage.py runserver

# Collect Static Files
python manage.py collectstatic --noinput

# Test Email Settings
python manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('Test', 'This is a test', 'from@example.com', ['to@example.com'])

# Check Settings
python manage.py check
python manage.py check --deploy
```

---

**Status:** Ready for deployment ✅

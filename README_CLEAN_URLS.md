# Clean URLs Implementation

This document describes the changes made to implement clean URLs for the Disaster Relief website.

## Changes Made

### 1. Updated All HTML Files
All HTML files have been updated to use clean URLs without `.html` extensions:

- **index.html**: Updated navigation links to use clean URLs
- **careers.html**: Updated all internal links and navigation
- **donations.html**: Updated all internal links and navigation
- **2nd-officer.html**: Updated navigation and breadcrumb links
- **purser.html**: Updated navigation and breadcrumb links
- **chief-engineer.html**: Updated navigation and breadcrumb links
- **chief-electro-technical-officer.html**: Updated navigation and breadcrumb links
- **web-designer.html**: Updated navigation and breadcrumb links

### 2. URL Changes
- `index.html` → `/` (root)
- `careers.html` → `/careers`
- `donations.html` → `/donations`
- `2nd-officer.html` → `/2nd-officer`
- `purser.html` → `/purser`
- `chief-engineer.html` → `/chief-engineer`
- `chief-electro-technical-officer.html` → `/chief-electro-technical-officer`
- `web-designer.html` → `/web-designer`

### 3. Server Configuration

#### Nginx Configuration (nginx.conf)
Created an nginx configuration file that:
- Handles clean URLs by automatically appending `.html` extension
- Serves `index.html` at the root path `/`
- Includes proper caching for static assets
- Handles 404 and 5xx error pages

#### Apache Configuration (.htaccess)
Created an `.htaccess` file for Apache servers that:
- Removes `.html` extensions from URLs
- Redirects old `.html` URLs to clean URLs (301 redirect)
- Includes security headers
- Handles static file caching

## Benefits

1. **SEO Friendly**: Clean URLs are better for search engine optimization
2. **User Friendly**: URLs are shorter and more memorable
3. **Professional**: Modern websites use clean URLs
4. **Maintainable**: Easier to manage and update

## Deployment

### For Nginx:
1. Copy the `nginx.conf` file to your nginx configuration directory
2. Restart nginx: `sudo systemctl restart nginx`

### For Apache:
1. Ensure mod_rewrite is enabled: `sudo a2enmod rewrite`
2. Copy the `.htaccess` file to your web root directory
3. Restart Apache: `sudo systemctl restart apache2`

### For Other Servers:
The HTML files will work with any server that supports URL rewriting. You may need to configure your server to handle the clean URL patterns.

## Testing

After deployment, test the following URLs:
- `/` (should show homepage)
- `/careers` (should show careers page)
- `/donations` (should show donations page)
- `/2nd-officer` (should show 2nd officer job page)
- `/purser` (should show purser job page)
- `/chief-engineer` (should show chief engineer job page)
- `/chief-electro-technical-officer` (should show chief electro-technical officer job page)
- `/web-designer` (should show web designer job page)

All navigation links should work seamlessly between pages. 
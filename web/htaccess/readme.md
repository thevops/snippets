# htaccess

block subpage
```
<IfModule mod_rewrite.c>
RewriteCond %{THE_REQUEST} \ /contact/
RewriteRule ^ - [L,F]
</IfModule>
```

redirect to https
```
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

block specific IP
```
order allow,deny
allow from all
deny from 123.123.123.123
```

block all except specific IP
```
order deny,allow
deny from all
allow from 127.0.0.1
```

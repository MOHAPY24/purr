#!/bin/sh

echo "info: Rebuilding package repositories..."
cd /etc/purr/purr.d || exit 1

cat > /etc/purr/purr.d/repositories.json << 'EOL'
{
    "$schema": "https://menory.site/pkgschema.json",
    "main_stable": {
        "url": "https://menory.site/",
        "author": "kma and momo",
        "version": "0.0.2",
        "license": "GPLv3",
        "active": true
    }
}
EOL

echo "info: Rebuilt repositories"
exit
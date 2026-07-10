[app]
title = Noflix
package.name = noflixapp
package.domain = org.hardcheck

source.dir = .

# Alle Dateitypen, die mit in die APK gepackt werden muessen:
# py = dein Code, png/jpg/jpeg = deine Icons in images/, kv = falls du mal .kv Dateien nutzt
source.include_exts = py,png,jpg,jpeg,kv,wav,mp3

# Stellt zusaetzlich sicher, dass der komplette images/ Ordner (egal wie tief)
# mit allen Bildern eingepackt wird - doppelt haelt hier besser.
source.include_patterns = images/*.png,images/*.jpg,images/*.jpeg

version = 1.0

# main.py nutzt: os, webbrowser, kivy -> beides os/webbrowser sind reine
# Python-Standardbibliothek, brauchen KEIN extra Requirement.
requirements = python3,kivy

# "all" statt "portrait": auf dem Handy bleibt die App nutzbar wie bisher,
# auf einem Fire TV / Android TV Geraet (immer Querformat) wird sie automatisch
# im Landscape-Modus dargestellt statt verzerrt im Hochformat.
orientation = all
fullscreen = 1

# App-Icon (wird zum Launcher-Icon der APK) und Splashscreen
icon.filename = %(source.dir)s/images/icon.png
presplash.filename = %(source.dir)s/images/presplash.png
presplash.color = #000000

# Wird gebraucht, damit die App Links im Browser oeffnen kann
android.permissions = android.permission.INTERNET

android.api = 34
android.minapi = 21
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# --- Fire TV / Android TV ---
# Zusaetzlicher Intent-Filter (LEANBACK_LAUNCHER), damit die App auch als
# "TV-App" erkannt wird und im Fire-TV-Launcher auftaucht.
android.manifest.intent_filters = tv_intent_filters.xml

# Erklaert Android, dass die App KEIN Touchscreen braucht (Fire TV hat keinen)
# und optional Leanback (TV-UI) unterstuetzt.
android.extra_manifest_xml = extra_manifest.xml

[buildozer]
log_level = 2
warn_on_root = 1

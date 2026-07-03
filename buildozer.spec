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

orientation = portrait
fullscreen = 1

# Wird gebraucht, damit die App Links im Browser oeffnen kann
android.permissions = android.permission.INTERNET

android.api = 34
android.minapi = 21
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1

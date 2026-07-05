
<img width="1024" height="1024" alt="Copilot_20260704_212619" src="https://github.com/user-attachments/assets/e1053da8-974b-4945-8794-272d101f7803" />


<div align="center">

<img src="https://github.com/user-attachments/assets/e1053da8-974b-4945-8794-272d101f7803" alt="Noflix Logo" width="150"/>

# Noflix

**Your all-in-one hub for Movies, TV Shows, and AI websites.**

[![Platform](https://img.shields.io/badge/platform-Android-3DDC84?logo=android&logoColor=white)](https://developer.android.com)
[![Release](https://img.shields.io/github/v/release/yourusername/noflix?color=blue)](https://github.com/yourusername/noflix/releases)
[![License](https://img.shields.io/github/license/yourusername/noflix)](LICENSE)
[![Min SDK](https://img.shields.io/badge/minSdk-24-orange)](https://developer.android.com/tools/releases/platforms)
[![Downloads](https://img.shields.io/github/downloads/yourusername/noflix/total)](https://github.com/yourusername/noflix/releases)

</div>

---

## 📖 About

**Noflix** is an Android app that helps you organize and manage your favorite **Movies**, **TV Shows**, and **AI websites** — all in one clean, unified interface. No more juggling bookmarks or switching between apps to track what you're watching or which AI tools you use.

## ✨ Features

- 🎬 Track and organize Movies & TV Shows
- 🤖 Manage and quick-access your favorite AI websites
- 🔍 Fast search and filtering
- 🎨 Clean, modern UI
- 📱 Lightweight and offline-friendly

## 📸 Screenshots

| Home | Movies | AI Websites |
|------|--------|-------------|
| _screenshot.png_ | _screenshot.png_ | _screenshot.png_ |

> Replace the placeholders above with actual screenshots (e.g. drag images into a GitHub issue/PR to get hosted URLs).

## 🚀 Getting Started

### Prerequisites

- [Android Studio](https://developer.android.com/studio) (Giraffe or newer recommended)
- JDK 17+
- Android SDK with:
  - **Min SDK:** 24 (Android 7.0 Nougat)
  - **Target SDK:** 34 (Android 14)

### Clone the repository

```bash
git clone https://github.com/yourusername/noflix.git
cd noflix
```

### Build the project

```bash
./gradlew build
```

### Run on a connected device/emulator

```bash
./gradlew installDebug
```

### Generate a release APK

```bash
./gradlew assembleRelease
```

The signed APK will be located at:
```
app/build/outputs/apk/release/app-release.apk
```

### Generate a release Android App Bundle (for Play Store)

```bash
./gradlew bundleRelease
```

Output location:
```
app/build/outputs/bundle/release/app-release.aab
```

## 📥 Installation

Download the latest APK directly from the [Releases](https://github.com/yourusername/noflix/releases) page and sideload it, or build from source using the steps above.

## 🛠️ Tech Stack

- **Language:** Kotlin
- **UI:** Jetpack Compose / XML _(update as applicable)_
- **Architecture:** MVVM
- **Build System:** Gradle (Kotlin DSL)

## 📱 Supported Android Versions

| Android Version | API Level | Supported |
|------------------|-----------|-----------|
| Android 7.0 (Nougat) | 24 | ✅ |
| Android 10 | 29 | ✅ |
| Android 12 | 31 | ✅ |
| Android 14 | 34 | ✅ |

## 🤝 Contributing

Contributions are welcome! Please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

## 📬 Contact

Have questions or suggestions? Open an [issue](https://github.com/yourusername/noflix/issues) or reach out directly.

---

<div align="center">
Made with ❤️ for movie, TV, and AI enthusiasts
</div>

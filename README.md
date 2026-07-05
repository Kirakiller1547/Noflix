<div align="center">

<img src="https://github.com/user-attachments/assets/e1053da8-974b-4945-8794-272d101f7803" alt="Noflix Logo" width="150"/>

# Noflix

**Your all-in-one hub for Movies, TV Shows, and AI websites.**

[![Platform](https://img.shields.io/badge/platform-Android-3DDC84?logo=android&logoColor=white)](https://developer.android.com)
[![Release](https://img.shields.io/github/v/release/Kirakiller1547/Noflix?color=blue)](https://github.com/Kirakiller1547/Noflix/releases/latest)
[![License](https://img.shields.io/github/license/Kirakiller1547/Noflix)](LICENSE)
[![Min SDK](https://img.shields.io/badge/minSdk-24-orange)](https://developer.android.com/tools/releases/platforms)
[![Downloads](https://img.shields.io/github/downloads/Kirakiller1547/Noflix/total)](https://github.com/Kirakiller1547/Noflix/releases)

**📦 [Download the latest release →](https://github.com/Kirakiller1547/Noflix/releases/latest)**

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
git clone https://github.com/Kirakiller1547/Noflix.git
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

1. Go to the [**Releases page**](https://github.com/Kirakiller1547/Noflix/releases)
2. Download the latest `.apk` file (e.g. [v1.0.0](https://github.com/Kirakiller1547/Noflix/releases/tag/v1.0.0))
3. Enable **Install from unknown sources** on your Android device (Settings → Security)
4. Open the downloaded APK and install

Alternatively, build the APK yourself from source using the steps above.

### 🏷️ Latest Release: v1.0.0

See the full changelog and assets on the [v1.0.0 release page](https://github.com/Kirakiller1547/Noflix/releases/tag/v1.0.0).

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

## ⚠️ Disclaimer & Terms of Use

This project is developed strictly for **educational, research, and self-learning purposes** (Weiterbildung / Proof of Concept). It is not intended for commercial use, nor is it meant to facilitate copyright infringement.

By using this application, you agree to the following:

- **No Content Hosting** — This app does not host, store, or distribute any media files or video streams. It acts only as a technical client that accesses publicly available third-party websites.
- **Third-Party Content** — The developer has no control over, and assumes no responsibility for, the content, privacy policies, or practices of any third-party websites. Accessing copyrighted material without permission may be illegal in your jurisdiction.
- **Use at Your Own Risk** — Use of this software is entirely at your own risk. You are solely responsible for complying with local laws and the terms of service of any websites accessed through this app.
- **As-Is Basis** — This software is provided "as is," without warranties of any kind, express or implied. The developer is not liable for any claims, damages, or legal issues arising from its use.

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

Have questions or suggestions? Open an [issue](https://github.com/Kirakiller1547/Noflix/issues) or reach out directly.

---

<div align="center">
Made with ❤️ for movie, TV, and AI enthusiasts
</div>

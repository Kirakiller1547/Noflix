<div align="center">

<img src="https://github.com/user-attachments/assets/e1053da8-974b-4945-8794-272d101f7803" alt="Noflix Logo" width="150"/>

# Noflix

**Your all-in-one hub for Movies, TV Shows, and AI websites.**

[![Platform](https://img.shields.io/badge/platform-Android-3DDC84?logo=android&logoColor=white)](https://developer.android.com)
[![Release](https://img.shields.io/github/v/release/Kirakiller1547/Noflix?color=blue)](https://github.com/Kirakiller1547/Noflix/releases/latest)
[![License](https://img.shields.io/github/license/Kirakiller1547/Noflix)](LICENSE)
[![Min SDK](https://img.shields.io/badge/minSdk-24-orange)](https://developer.android.com/tools/releases/platforms)
[![Downloads](https://img.shields.io/github/downloads/Kirakiller1547/Noflix/total)](https://github.com/Kirakiller1547/Noflix/releases)

**📦 [Download the latest release →]([https://github.com/Kirakiller1547/Noflix/releases/latest](https://github.com/Kirakiller1547/Noflix/releases/tag/v1.0.0))**

</div>

---

## 📖 About

**Noflix** is an Android app that helps you organize and manage bookmarks for **Movies**, **TV Shows**, and **AI websites** in one clean, unified interface — so you don't have to juggle browser bookmarks or switch between apps to keep track of what you're watching or which AI tools you use.

## ✨ Features

- 🎬 Organize bookmarks for Movies & TV Shows
- 🤖 Manage quick-access links to your favorite AI websites
- 🔍 Fast search and filtering
- 🎨 Clean, modern UI
- 📱 Lightweight and works offline

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
cd Noflix
```

### Build the project

```bash
./gradlew build
```

### Run on a connected device or emulator

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

1. Go to the [Releases page](https://github.com/Kirakiller1547/Noflix/releases).
2. Download the latest `.apk` file (e.g. [v1.0.0](https://github.com/Kirakiller1547/Noflix/releases/tag/v1.0.0)).
3. Enable **Install from unknown sources** on your Android device (Settings → Security).
4. Open the downloaded APK and install it.

Alternatively, build the APK yourself from source using the steps above.

### 🏷️ Latest Release: v1.0.0

See the full changelog and assets on the [v1.0.0 release page](https://github.com/Kirakiller1547/Noflix/releases/tag/v1.0.0).

## 🛠️ Tech Stack

- **Language:** Kotlin
- **UI:** Jetpack Compose
- **Architecture:** MVVM
- **Build System:** Gradle (Kotlin DSL)

## 📱 Supported Android Versions

| Android Version | API Level | Supported |
|---|---|---|
| Android 7.0 (Nougat) | 24 | ✅ |
| Android 10 | 29 | ✅ |
| Android 12 | 31 | ✅ |
| Android 14 | 34 | ✅ |

## ⚠️ Disclaimer & Terms of Use

This project is developed strictly for educational, research, and self-learning purposes. It is not intended for commercial use, and it is not meant to facilitate copyright infringement.

By using this application, you acknowledge and agree to the following:

- **No content hosting.** This application functions solely as a bookmark manager and launcher for websites specified by the user. It does not host, store, cache, stream, distribute, or otherwise provide any media files or content.
- **User-added links.** Website links and associated icons may be added or modified by users. The developer does not review, verify, endorse, or control user-added links or the content available through them.
- **Third-party websites.** All websites accessed through this application are operated by independent third parties. The developer has no control over, and assumes no responsibility for, the availability, accuracy, legality, privacy policies, practices, or content of any third-party website or service.
- **No affiliation.** The developer is not affiliated with, sponsored by, or endorsed by any third-party website accessible through this application.
- **User responsibility.** You are solely responsible for the websites you choose to access and for complying with all applicable laws, copyright laws, and the terms of service of those websites. Accessing copyrighted material without proper authorization may be illegal in your jurisdiction.
- **Use at your own risk.** Your use of this application is entirely at your own risk. The developer assumes no responsibility for how the application is used or for any consequences arising from its use.
- **As-is basis.** This application is provided "as is" and "as available," without warranties of any kind, whether express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, or non-infringement. To the fullest extent permitted by applicable law, the developer disclaims all liability for any claims, damages, losses, or legal consequences arising from use of this application or any third-party websites accessed through it.

## 🤝 Contributing

Contributions are welcome! Please open an issue first to discuss what you'd like to change.

1. Fork the repo.
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request.

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.

## 📬 Contact

Have questions or suggestions? Open an [issue](https://github.com/Kirakiller1547/Noflix/issues) or reach out directly.

---

<div align="center">
Made with ❤️ for movie, TV, and AI enthusiasts
</div>

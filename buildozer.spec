[app]
title = Black Jack
package.name = blackjack
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 23b
android.ndk_api = 21
android.arch = arm64-v8a
p4a.branch = master
android.accept_sdk_license = True
android.build_tools = 30.0.3
android.gradle_dependencies = androidx.core:core:1.6.0, androidx.appcompat:appcompat:1.3.1
android.add_aars = androidx.webkit:webkit:1.4.0

[buildozer]
log_level = 2
warn_on_root = 1
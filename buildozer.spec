[app]
title = HelloApp
package.name = helloapp
package.domain = org.kivy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
osx.kivy_version = 2.1.0

[buildozer]
log_level = 2
warn_on_root = 1
android.api = 31
android.sdk = 24
android.ndk = 23b
android.arch = armeabi-v7a

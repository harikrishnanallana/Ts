[app]

# (str) Title of your application
title = HelloKivy

# (str) Package name
package.name = hellokivy

# (str) Package domain (reverse domain)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py

# (str) Application version
version = 1.0

# (list) Application requirements (Kivy and any additional dependencies)
requirements = python3==3.7.6,kivy,pillow,hostpython3==3.7.6

# (str) Application icon (optional)
#icon.filename = path/to/your/icon.png

# (list) Application permissions (optional)
#android.permissions = INTERNET

# (list) Application orientation (portrait, landscape, all, or any combination)
orientation = portrait

# (list) Service to launch (in case you have any background services)
#services =

# (str) The name of the entry point to run
#android.entrypoint = your_app_name

# (int) Minimum API level for your application
#android.api = 21

# (int) Target API level for your application
#android.api = 29

# (int) Minimum API level to run your application
#android.minapi = 21

# (str) Android NDK version to use
#p4a.ndk = 21.1.6352462

# (str) Android SDK version to use
#p4a.sdk = 20

# (bool) Copy libgpg.so to libs/armeabi. This fixes a bug in distribution where the ARM version of the lib is stripped
#android.copy_libgpg = False

# (str) The Android architecture to build for (armeabi-v7a, arm64-v8a, x86, x86_64)
#android.arch = armeabi-v7a

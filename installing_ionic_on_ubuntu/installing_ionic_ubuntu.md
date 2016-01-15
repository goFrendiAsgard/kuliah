# Go Frendi's guide to install ionic framework in ubuntu 15.10

I can't believe I spend 2 days to finally able to build a blank android application by using ionic framework.

In case of you want to try ionic in your `ubuntu` box, This notes will probably useful.

## 1. Set up nodejs, ionic, cordova, and android sdk

Create a bash script (`install-ionic.sh`) contains:

```bash
#!/bin/bash
# Ubuntu Developer Script For Ionic Framework
# Created by Nic Raboy
# http://www.nraboy.com
#
# Minor modification regarded to android and node version
# was done by me :)
#
# Downloads and configures the following:
#
#   Java JDK
#   Apache Ant
#   Android
#   NPM
#   Apache Cordova
#   Ionic Framework

HOME_PATH=$(cd ~/ && pwd)
INSTALL_PATH=/opt
ANDROID_SDK_PATH=/opt/android-sdk
NODE_PATH=/opt/node

# x86_64 or i686
LINUX_ARCH="$(lscpu | grep 'Architecture' | awk -F\: '{ print $2 }' | tr -d ' ')"

# Latest Android Linux SDK for x64 and x86 as of 15-1-2016
ANDROID_SDK_X64="http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz"
ANDROID_SDK_X86="http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz"

# Latest NodeJS for x64 and x86 as of 15-1-2016
NODE_X64="https://nodejs.org/dist/v4.2.4/node-v4.2.4-linux-x64.tar.gz"
NODE_X86="https://nodejs.org/dist/v4.2.4/node-v4.2.4-linux-x86.tar.gz"

if [ "$LINUX_ARCH" == "x86_64" ]; then
    # Add i386 architecture
    dpkg --add-architecture i386
fi

# Update all Ubuntu software repository lists
apt-get update

cd ~/Desktop

if [ "$LINUX_ARCH" == "x86_64" ]; then

    wget "$NODE_X64" -O "nodejs.tgz"
    wget "$ANDROID_SDK_X64" -O "android-sdk.tgz"

    tar zxf "nodejs.tgz" -C "$INSTALL_PATH"
    tar zxf "android-sdk.tgz" -C "$INSTALL_PATH"

    cd "$INSTALL_PATH" && mv "android-sdk-linux" "android-sdk"
    cd "$INSTALL_PATH" && mv "node-v4.2.4-linux-x64" "node"

    # Android SDK requires some x86 architecture libraries even on x64 system
    apt-get install -qq -y libc6:i386 libgcc1:i386 libstdc++6:i386 libz1:i386

else

    wget "$NODE_X86" -O "nodejs.tgz"
    wget "$ANDROID_SDK_X86" -O "android-sdk.tgz"

    tar zxf "nodejs.tgz" -C "$INSTALL_PATH"
    tar zxf "android-sdk.tgz" -C "$INSTALL_PATH"

    cd "$INSTALL_PATH" && mv "android-sdk-linux" "android-sdk"
    cd "$INSTALL_PATH" && mv "node-v4.2.4-linux-x86" "node"

fi

cd "$INSTALL_PATH" && chown root:root "android-sdk" -R
cd "$INSTALL_PATH" && chmod 777 "android-sdk" -R

cd ~/

# Add Android and NPM paths to the profile to preserve settings on boot
echo "export PATH=\$PATH:$ANDROID_SDK_PATH/tools" >> ".profile"
echo "export PATH=\$PATH:$ANDROID_SDK_PATH/platform-tools" >> ".profile"
echo "export PATH=\$PATH:$NODE_PATH/bin" >> ".profile"

# Add Android and NPM paths to the temporary user path to complete installation
export PATH=$PATH:$ANDROID_SDK_PATH/tools
export PATH=$PATH:$ANDROID_SDK_PATH/platform-tools
export PATH=$PATH:$NODE_PATH/bin

# Install JDK and Apache Ant
apt-get -qq -y install default-jdk ant

# Set JAVA_HOME based on the default OpenJDK installed
export JAVA_HOME="$(find /usr -type l -name 'default-java')"
if [ "$JAVA_HOME" != "" ]; then
    echo "export JAVA_HOME=$JAVA_HOME" >> ".profile"
fi

# Install Apache Cordova and Ionic Framework
npm install -g cordova
npm install -g ionic

cd "$INSTALL_PATH" && chmod 777 "node" -R

# Clean up any files that were downloaded from the internet
cd ~/Desktop && rm "android-sdk.tgz"
cd ~/Desktop && rm "nodejs.tgz"

echo "----------------------------------"
echo "Restart your Ubuntu session for installation to complete..."

```

After creating the script (either by using gedit, nano or any text editor) do this:

* Change the script permission so that it is going to be executable: `chmod 755 install-ionic.sh`

* Execute the script `sudo ./install-ionic.sh`

__PS:__ You might need to modify these parts, always check for the newest version:

```bash
# Latest Android Linux SDK for x64 and x86 as of 15-1-2016
ANDROID_SDK_X64="http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz"
ANDROID_SDK_X86="http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz"

# Latest NodeJS for x64 and x86 as of 15-1-2016
NODE_X64="https://nodejs.org/dist/v4.2.4/node-v4.2.4-linux-x64.tar.gz"
NODE_X86="https://nodejs.org/dist/v4.2.4/node-v4.2.4-linux-x86.tar.gz"
```

## 2. Install several packages into your android sdk

* Run `sudo /opt/android-sdk/tools/android`
* Install `Android SDK Tools`, `Android SDK Platform-tools`, `Android SDK Build-tools`
* Click on `Android 5.1 (Api 22)`, install `SDK Platform`

Those packages are necessary to build or emulate android application.

## 3. Your graddle might probably corrupted, so replace it

* Try to open `/home/[your-user-name]/.gradle/wrapper/dists/gradle-2.2.1-all/2m8005s69iu8v0oiejfej094b/graddle-2.1.1.zip` by using any archive manager. Check whether it is corrupted or not.

* If it is corrupted, try to download from this site `http://gradle.org/gradle-download/`, and replace the file.

## 4. Check out your `.android` permission, is it readable?

* Run `chmod 777 .android -R`

## 5. Try out some basic commands and hack up

* `ionic start todo blank`
* `cd todo`
* `ionic platform add todo`
* `ionic build android`
* `ionic serve`
* `ionic emulate android`

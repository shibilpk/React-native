# Install nmp and node.js for react.js

    sudo apt install nodejs
    sudo apt install npm


# Install VS code and add some extentions
    Simple React by Burke Holland
    Prettier - Code formatter by Esben Petersen
    “editor.formateOnSave”: true,
# Update npm
    sudo npm cache clean -f
    sudo npm install -g n
    sudo n stable


#Install React Native CLI
    sudo npm install -g react-native-cli

    #If you get an error like Cannot find module ‘npmlog’ you can install npm directly using this command. If the above command run successfully then no need to run this command

        curl -0 -L https://npmjs.org/install.sh | sudo sh


		
~~~~~~~~~~~~Now install Oracle JDK (recommended) ~~~~~~~~~~~~~~~~~`
# Step 1:
#     Download the latest JDK(jdk-8u231-linux-x64.tar.gz) from this official site.

# Step 2: (Open the terminal (Ctrl + Alt + T))
    sudo mkdir /usr/lib/jvm

#    If the /usr/lib/jvm folder does not exist, this command will create the directory. If you already have this folder, you can ignore this step and move to next step.

#Step 3:
    cd /usr/lib/jvm

#Step 4: (Extract the jdk-8u231-linux-x64.tar.gz file in Download directory )
    sudo tar -xvzf ~/Downloads/jdk-8u231-linux-x64.tar.gz

#Step 5:
    #Enter the following command to open the environment variables file.
    sudo gedit /etc/environment

#Step 6:
    #In the opened file, add the following bin folders to the existing PATH variable.

        /usr/lib/jvm/jdk1.8.0_231/bin
        /usr/lib/jvm/jdk1.8.0_231/db/bin
        /usr/lib/jvm/jdk1.8.0_231/jre/bin

    The PATH variables have to be separated by semicolon.
    Notice that the installed JDK version is 1.8 update 231. Depending on your JDK version, the paths can be different.
    Add the following environment variables at the end of the file.

        J2SDKDIR="/usr/lib/jvm/jdk1.8.0_231"
        J2REDIR="/usr/lib/jvm/jdk1.8.0_231/jre"
        JAVA_HOME="/usr/lib/jvm/jdk1.8.0_231"
        DERBY_HOME="/usr/lib/jvm/jdk1.8.0_231/db"


    #The environment file after the modification:

        PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/jvm/jdk1.8.0_231/bin:/usr/lib/jvm/jdk1.8.0_231/db/bin:/usr/lib/jvm/jdk1.8.0_231/jre/bin"
        J2SDKDIR="/usr/lib/jvm/jdk1.8.0_231"
        J2REDIR="/usr/lib/jvm/jdk1.8.0_231/jre"
        JAVA_HOME="/usr/lib/jvm/jdk1.8.0_231"
        DERBY_HOME="/usr/lib/jvm/jdk1.8.0_231/db"

        #Save the changes and close the gedit.

#Step 7:
    #Enter the following commands to inform the system about the Java's location. Depending on your JDK version, the paths can be different.

    sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.8.0_231/bin/java" 0
    sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.8.0_231/bin/javac" 0
    sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_231/bin/java
    sudo update-alternatives --set javac /usr/lib/jvm/jdk1.8.0_231/bin/javac

#Step 8:
#To verify the setup enter the following commands and make sure that they print the location of java and javac as you have provided in the previous step.

    update-alternatives --list java
    update-alternatives --list javac

#Step 9:
    #Restart the computer (or just log-out and login) and open the terminal again.

#Step 10:
    java -version

#If you get the installed Java version as the output, you have successfully installed the Oracle JDK in your system

~~~~~~~~~~~~ or ~~~~~~~~~~~~~~~~~

    sudo apt install default-jre
    sudo apt install openjdk-11-jre-headless
    sudo apt install openjdk-8-jre-headless

~~~~~~~~~~~~~~~or~~~~~~~~~~~~~~~~~~
    sudo apt install openjdk-8-jdk
	
	update-java-alternatives --list
	sudo update-alternatives --config java
		<select>	/usr/lib/jvm/java-11-openjdk-amd64/bin/java   1101      manual mode
	sudo  update-alternatives --config javac
		<select>	/usr/lib/jvm/java-8-oracle/bin/javac   1081      manual mode
	export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")
	export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:jre/bin/java::")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#Install Android Studio

    sudo add-apt-repository ppa:maarten-fonville/android-studio sudo apt install android-studio
    sudo apt update

	# You can Choose a “Custom”
	# checked:(tick)
	# 	Android SDK
	# 	Android SDK Platform
	# 	AVD (Android Virtual Device)


#error permission denied for /dev/kvm

    sudo apt install qemu-kvm
    sudo adduser​ usernameofpc kvm
    sudo chown​ usernameofpc /dev/kvm

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
#Now, Configure the ANDROID_HOME environment variable`
	touch .bash_profile
	gedit $HOME/.bash_profile

	or #edit .bashrc 

	#paste the following 
		export ANDROID_HOME=$HOME/Android/Sdk
		export PATH=$PATH:$ANDROID_HOME/emulator
		export PATH=$PATH:$ANDROID_HOME/tools
		export PATH=$PATH:$ANDROID_HOME/tools/bin
		export PATH=$PATH:$ANDROID_HOME/platform-tools
	#add this line to open auto jdr
		export JAVA_HOME=/snap/android-studio/81/android-studio/jre
			#set jre location correctly
		
		#then save and exit

	source $HOME/.bash_profile
	echo $PATH

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create a new project
	react-native init ProjectName

#On another terminal
    source $HOME/.bash_profile
    react-native start

#on a tab
    source $HOME/.bash_profile
    react-native run-android


# Agree licence of skd
    $ANDROID_HOME/tools/bin/sdkmanager --licenses
                    or
    yes | sdkmanager --licenses


#Running on mobile phone
    On the folder 'Home/Android/Sdk/platform-tools' open terminal

    sudo apt-get install adb
    adb devices
    sudo adb reverse tcp:8081 tcp:8081  

    #error
    sudo usermod -aG plugdev $LOGNAME

#Killing a process on port
    sudo kill -9 `sudo lsof -t -i:8081`
    #If that doesn't work you could also use $() for command interpolation:
    sudo kill -9 $(sudo lsof -t -i:8081)

#file reach error problem
    echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p

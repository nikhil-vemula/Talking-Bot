# Talking-Bot
Things needed!
1. Python 2.x (will not work in python 3.x)

Can be downloaded from here

But I recommend you  to use Anaconda for setting up necessary dependencies and environmental variables automatically.
2. Pyttsx (Text to speech Module)

Install it using pip command. Open your console and type

pip install pyttsx

 

1
3. Aiml (python aiml module)

Install using

pip install aiml

2
Getting the work done!

Create three files named

    std-startup.xml – starting up the bot interface and learning from the basic-chat data
    basic-chat.aiml – contains our chat phrases
    bot.py – the main python script that does the work

Copy the following contents into each
Std-startup.xml

<aiml version="1.0.1" encoding="UTF-8">
    <!-- std-startup.xml -->
    <!-- Category is an atomic AIML unit -->
    <category>
        <!-- Pattern to match in user input -->
        <!-- If user enters "LOAD AIML B" -->
        <pattern>LOAD AIML B</pattern>
        <!-- Template is the response to the pattern -->
        <!-- This learn an aiml file -->
        <template>
            <learn>basic_chat.aiml</learn>
            <!-- You can add more aiml files here -->
            <!--<learn>more_aiml.aiml</learn>-->
        </template>        
    </category>
</aiml>

2. Basic-chat.aiml

<aiml version="1.0.1" encoding="UTF-8">
    <category>
    <pattern>HI</pattern>
    <template><srai>HELLO</srai></template>
    </category>
    
    <category>
    <pattern>WASS UP</pattern>
    <template>Nothing much</template>
    </category>
    
    <category>
    <pattern>HEHE</pattern>
    <template>I am pleased to see u happy</template>
    </category>
    
    <category>
    <pattern>HELLO</pattern>
    <template>hello, please to meet u</template>
    </category>
    
    <category>
    <pattern>WHO R U</pattern>
    <template><srai>WHO ARE YOU</srai></template>
    </category>
    
    <category>
    <pattern>NAME</pattern>
    <template><srai>WHO ARE YOU</srai></template>
    </category>
    
    <category>
    <pattern>WHAT IS YOUR NAME</pattern>
    <template><srai>WHO ARE YOU</srai></template>
    </category>
    
    <category>
        <pattern>WHO ARE YOU</pattern>
        <template>My name is J</template>
    </category>
    
    <category>
    <pattern>TELL ME ABOUT YOU</pattern>
    <template><srai>NAME</srai>. i am written by ncipher. i am written in python using pyttsx and aiml modules.</template>
    </category>
    <category>
        <pattern>*</pattern>
        <template>
        <random>
            <li>I didn't get u</li>
            <li>Sorry, I have limited responses</li>
        </random>
        </template>
    </category>
    
</aiml>

3. Bot.py

# setting up aiml
import aiml
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
# setting up pyttsx(talking)
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("hello, pleased to meet u")
engine.runAndWait()
while True:
    input = raw_input("Enter your message >> ")
    output = kernel.respond(input)
    print output
    engine.say(output)
    engine.runAndWait()

Run the bot.py file to fire up the bot….
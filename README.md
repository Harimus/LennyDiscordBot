My Humble try to create a discord bot with the Lenny face functionality
Based on the pattern found in [lenny-face-generator](https://lenny-face-generator.textsmilies.com/?cr=bW91dGh%2Bdy5udy5pZV9leWVzfncubzEuNHdfZWFyc34xNC0xNQ%3D%3D),

# Current functionality ( ͡° ͜ʖ ͡°)
- Set users nickname based on name / role. (only Lenny faces ofc) 
- Add/remove user for user authentication.
 
# Fetures to be added
  ## Currently under work
  - Audio playback using FFMPEGPCMAudio module. (Binary file needed for running)
  - Store Guild setup in a config file (including bot usage permission)
  - Record audio input from other users. 
  
  ## Todo
  The below todo:s might be a little bit harder than I thought, since the API this is based on still seems to not support listening to user audio [according to this](https://github.com/Rapptz/discord.py/issues/1094). It's either to implement it myself (huge learning curve regarding audio data), Use the not so stable yet implementation,(potential unknown issues popping up) or mode to javascript API.(Learning curve in JS)
  - Speech to text (voice recognition).
  - audio playback based on above.
  - playback of youtube URL.

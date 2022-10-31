
This bot is using to shutdown a local pc via telegram for using it u need:
1) type in console: python -m venv ./venv
2) Then type: pip3 install -r requirements. txt
3) add telegram account id at: src/cfg in ADMIN_ID list"
4) Start this script on your own local machine (you can do from this script a windows services by pyinstaller (make main.exe from src/main.py 
and create a windows service (linux users will figure it out themselves ha-ha):
  
	4.1 run cmd as administrator
  
	4.2 type: Sc create ShutDownPC_BOT binPath={enter a pass to main.exe} DisplayName=″ShutDownPC_BOT″ type=own start=auto
  
	4.3 rebot ur pc and use it!

5) P.S. for full use, preference get on the phone application "wake on lan" and setup it

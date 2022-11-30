# ShutDownPC
## This bot is using to shutdown a local pc via telegram bot


### Lets start:


- git clone https://github.com/gentoumashiro/ShutDownBot.git
- cd ShutDownBot
- python -m venv ./venv 
- venv\scripts\activate
- pip install -r requirements.txt
- notepad.exe src\cfg.py and add telegram account(s) id to: ADMIN_ID list
- Now we need to create a exe file from main.exe, so type:
	____
	- pyinstaller --noconfirm --onefile --console -n ShutDownPcBot "FULL PATH to \main.py"

	- Then u can delete ShutDownPc_bot folder EXCEPT ShutDownPcBot.exe in dist folder. Save it.
	____

- Now we need to create windows service (linux users will be do itt by themselves ha-ha)
	____
	- run cmd as administrator

	- type: sc create ShutDownPC_BOT binPath={enter a pass to main.exe} DisplayName=″ShutDownBotService″ type=own start=auto

	- rebot ur pc and use it!
	____

**P.S. for full use, preference get on the phone application "wake on lan" and setup it**

P.P.S for linux users creating service: https://gist.github.com/ewenchou/be496b2b73be801fd85267ef5471458c

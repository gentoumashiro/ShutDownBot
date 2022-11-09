
This bot is using to shutdown a local pc via telegram for using it u need:

1) git clone https://github.com/gentoumashiro/ShutDownPC_bot.git
2) cd ShutDownPC_bot
3) type in console: python -m venv ./venv
4) Then type: pip3 install -r requirements.txt
5) type in cmd notepade.exe src\cfg.py and add telegram account(s) id to: ADMIN_ID list
6) Now we need to create a exe file from main.exe, so type:
	____________________________
	6.1 pyinstaller --noconfirm --onefile --console "FULL PATH to \main.py"
	like: pyinstaller --noconfirm --onefile --console "D:\ShutDownPC_bot\src\main.py"

	6.2 Then u can delete ShutDownPc_bot folder EXCEPT main.exe in dist folder. Save it.
	____________________________

7) Now we need to create windows service (linux users will be do itt by themselves ha-ha)
	____________________________
	7.1 run cmd as administrator
	7.2 type: sc create ShutDownPC_BOT binPath={enter a pass to main.exe} DisplayName=″ShutDownBotService″ type=own start=auto
	7.3 rebot ur pc and use it!
	____________________________

5) P.S. for full use, preference get on the phone application "wake on lan" and setup it

P.P.S for linux users creating service: https://gist.github.com/ewenchou/be496b2b73be801fd85267ef5471458c

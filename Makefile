test:
	python3 -m pip install -r requirements.txt
	python3 mathmod/__init__.py #syntax check
	@echo Mathmod works\!
	echo "1\n+\n1\n2\n3\n\nexit\n" > engadd.txt
	@echo "DBG: $(cat engadd.txt)"
	echo "2\n+\n1\n2\n3\n\nexit\n" > fradd.txt
	@echo "DBG: $(cat fradd.txt)"
	python3 palc.py < engadd.txt
	sleep 5
	python3 palc.py < fradd.txt
	@echo Finished testing
# This code belongs on Reddit
binary:
	python3 -m pip install -r requirements.txt
	python3 -m pip install pyinstaller
	pyinstaller palc.spec
	@echo You can find your data in the \`dist\' folder!
clean:
	@rm -iR fradd.txt engadd.txt __pycache__ palc.log || echo "Some files failed to delete. This could be because of missing permissions, if the files still exist please check their perms." #infrared
	@echo Removing build folder...
	@rm -IR build || echo "build folder failed to delete."

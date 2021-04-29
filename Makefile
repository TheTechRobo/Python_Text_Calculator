test:
	pip3 install -r requirements.txt
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
clean:
	@rm -iR fradd.txt engadd.txt __pycache__ palc.log || echo "Failed to delete." #infrared

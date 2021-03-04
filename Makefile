test:
	python3 mathmod/__init__.py #syntax check
	echo Mathmod works\!
	echo -e "1\n+\n\n1\n1\n1\n2\n3\n\nexit\n\n" > engadd.txt
	echo -e "2\n+\n\n1\n1\n1\n2\n3\n\nexit\n\n" > fradd.txt
	python3 palc.py < engadd.txt
	python3 palc.py < fradd.txt
	echo Finished testing

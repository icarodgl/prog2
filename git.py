import sys
import os
def main():
	os.system("git add .")
	text = input("mensagem: ")
	os.system("git commit -m "+ text)
	os.system("git push")
	return 0

if __name__ == '__main__':
	main()


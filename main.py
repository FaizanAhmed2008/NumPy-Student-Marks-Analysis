import sys
from ui import App

def main():
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

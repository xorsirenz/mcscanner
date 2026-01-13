from src.main import main, shutdown

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        shutdown()

import sys
import router

if __name__ == "__main__":
    router.app.run(debug=False, host=sys.argv[1], port=sys.argv[2])
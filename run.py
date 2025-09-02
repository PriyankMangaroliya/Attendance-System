from app import app

if __name__ == "__main__":
    # Run only on localhost:5000
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True   # change to False in production
    )
from Core import Core


# Main
def main():
    # Core Class Instance
    _Core = Core()
    # Set Url
    _Core.Url("https://limon.kg/")

    for Email in _Core._Core__Emails:
        print(Email)


# Check
if __name__ == "__main__":
    main()

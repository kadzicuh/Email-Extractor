from Get_Links import Get_Links


# Main
def main():

    # Get_Links [Object]
    Link = Get_Links('http://akipress.org')

    # Search Links
    Link.Search_Links()


# Check
if __name__ == "__main__":
    main()
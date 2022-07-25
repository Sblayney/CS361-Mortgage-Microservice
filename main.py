"""
Example of main project. Main project calls get_items function, which
will communicate with the microservices pipe to request and receive
information.
"""
from get_rates import get_rates


def main():
    """Example of individual project."""
    # Get data from microservice
    data = get_rates()
    print(data)


if __name__ == "__main__":
    main()

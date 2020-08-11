import requests

def apache():
    url = 'http://ec2-15-206-93-70.ap-south-1.compute.amazonaws.com/'
    try:
        r = requests.get(url)
        r.raise_for_status()
        return ('Active')

    except requests.exceptions.HTTPError:
        return (" URL not found")
    
    except requests.exceptions.ConnectionError:
        return ("Inactive")
    


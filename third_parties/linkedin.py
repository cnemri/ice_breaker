import os
import requests


def scrape_linkedin_profile(linkedin_profile_url):
    """
    Scrapes the LinkedIn profile and returns the extracted data.

    Args:
        linkedin_profile_url (str): The LinkedIn profile URL to scrape.

    Returns:
        dict: A dictionary containing the extracted data.
    """
    # headers = {"Authorization": "Bearer " + os.environ.get("PROXYCURL_API_KEY")}
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # params = {
    #     "linkedin_profile_url": linkedin_profile_url,
    # }
    # response = requests.get(api_endpoint, params=params, headers=headers)

    # data = response.json()

    # data = {
    #     k: v
    #     for k, v in data.items()
    #     if v not in ([], "", None) and k not in ("people_also_viewed", "certifications")
    # }

    # if data.get("groups"):
    #     for group_dict in data.get("groups"):
    #         group_dict.pop("profile_pic_url")

    # return data

    data = requests.get(
        "https://gist.githubusercontent.com/cnemri/b3878e69aa203801a8e326d31c6a2e7c/raw/8d2644c54debd9224f14e52ee68002c51a9ecfba/chouaieb-nemri.json"
    ).json()
    return data

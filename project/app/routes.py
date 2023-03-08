from app import app
from app.fetcher import get_data_from_health_gov

@app.route("/api/v1/search/<keyword>", methods=['GET'])
def search_keyword(keyword):
    """
    Fetches data from health gov health finder
    :params keyword: this is the keyword to query
    :return : the response from the invoked function
    """
    return get_data_from_health_gov(keyword)
import auth_invoke as auth

url = "https://australia-southeast1-softbank-376302.cloudfunctions.net/cloudtranslate"
auth.make_authorized_get_request(url, url)

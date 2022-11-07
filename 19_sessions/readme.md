TBD's Adventures: Samantha Hua, Anjini Katari, and Emerson Gelobter
SoftDev
K19 -- Sessions Greetings
2022-11-03
time spent: 1.5hrs

DISCO:
 * Secret Key -> used for security purposes
 * The secret key needs to be made outside of @app.route
 * To redirect the user on the click of a button, you need a form and a button inside the form. We learned this through trial and error
 * auth is a key term. we tried to replace the route of the form submission and it gave us errors

QCC:
 * Is /auth the default redirect for forms?
 * We encountered url_for("blank") in our research. What does this do and how is it significant? We didn't end up using it though.
 * What does the b outside of the single quotes in the secret key stand for?
    - We think it means that the stuff inside the string is in bytes. the b standing for bytes
 * Are there other key terms like "/auth" that must be used in certain links? ie: we can write '/logout' as '/getout' but not '/auth' as '/a'
 * What is the significance of secret keys. Why are they needed?
 * We need a refresher on the difference between request.args and request.form

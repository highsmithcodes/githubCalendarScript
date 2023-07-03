import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/calendar')
def get_github_calendar():
    username = "YourGitHubUsername"
    url = f"https://github.com/users/highsmithcodes/contributions"

    response = requests.get(url)
    if response.status_code == 200:
        # Add CSS styles to mimic GitHub calendar colors
        css_styles = """
        <style>
            .day {
                width: 12px;
                height: 12px;
                display: inline-block;
                margin: 0 1px;
                background-color: #ebedf0;
                border-radius: 2px;
            }

            .day[data-level="1"] {
                background-color: #c6e48b;
            }

            .day[data-level="2"] {
                background-color: #7bc96f;
            }

            .day[data-level="3"] {
                background-color: #239a3b;
            }
            .ContributionCalendar-day[data-level="1"] {
                fill: #0e4429;
            }
            .ContributionCalendar-day[data-level="2"]{
                fill: #006d32;
            }
            .ContributionCalendar-day[data-level="3"]{
                fill:#26a641;
            }
            .ContributionCalendar-day[data-level="4"]{
                fill: #39d353;
            }
            .ContributionCalendar-day, .ContributionCalendar-day[data-level="0"]{
                fill: #ebedf0;
            }

            /* Add more styles for higher contribution levels as needed */

            /* Adjust overall calendar layout */
            .calendar-graph {
                display: inline-block;
            }
        </style>
        """

        # Inject CSS styles into the HTML response
        html_response = response.text.replace("<svg", f"{css_styles}<svg")
        return html_response
    else:
        return jsonify(error="Failed to fetch GitHub calendar data"), 500

if __name__ == '__main__':
    app.run()

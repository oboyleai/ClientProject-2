import csv
from datetime import datetime
from pathlib import Path
import os

def read_csv(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)

def parse_meet_info(data):
    meet_name = data[0][0]
    meet_date = data[1][0]
    team_results_link = data[2][0]
    team_summary = "\n".join(data[3:])  # Join all remaining lines for the summary
    return meet_name, meet_date, team_results_link, team_summary

def generate_team_results_html(data):
    html = ""
    for row in data[1:]:  # Skip header row
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>\n"
    return html

def generate_athlete_results_html(data):
    html = ""
    for row in data[1:]:  # Skip header row
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[4]}</td><td>{row[5]}</td></tr>\n"
    return html

def populate_template(template, meet_info, team_results, athlete_results):
    meet_name, meet_date, team_results_link, team_summary = meet_info
    
    template = template.replace('{meet_name}', meet_name)
    template = template.replace('{meet_date}', meet_date)
    template = template.replace('{team_results_link}', team_results_link)
    template = template.replace('{team_summary}', team_summary)
    template = template.replace('{current_year}', str(datetime.now().year))
    template = template.replace('{school_name}', "Ann Arbor Skyline")  # Replace with actual school name
    
    # Insert team results
    team_results_html = generate_team_results_html(team_results)
    template = template.replace('<!-- Team results will be inserted here -->', team_results_html)
    
    # Insert athlete results
    athlete_results_html = generate_athlete_results_html(athlete_results)
    template = template.replace('<!-- Athlete results will be inserted here -->', athlete_results_html)
    
    return template

def main():
    # Find CSV files in the current directory
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the current directory.")
        return

    # Use the first CSV file found
    csv_file = csv_files[0]
    print(f"Using file: {csv_file}")

    # Read CSV file
    data = read_csv(csv_file)
    
    # Parse meet info (assuming it's all in the same file)
    meet_info = parse_meet_info(data[:10])  # Use first 10 rows for meet info
    team_results_data = data[10:20]  # Use next 10 rows for team results
    athlete_results_data = data[20:]  # Use remaining rows for athlete results
    
    # Read HTML template
    with open('template.html', 'r') as file:
        template = file.read()
    
    # Populate template
    populated_html = populate_template(template, meet_info, team_results_data, athlete_results_data)
    
    # Write output HTML file
    output_file = Path(f"results_{meet_info[0].replace(' ', '_')}.html")
    with open(output_file, 'w') as file:
        file.write(populated_html)
    
    print(f"HTML file generated: {output_file}")

if __name__ == "__main__":
    main()
import csv

# File Locations
path = 'meets/'
meet_file = '37th_Early_Bird_Open_Mens_5000_Meters_HS_Open_5K_24.csv'
output_file = meet_file.rstrip('.csv') + '.html'

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader) 

        meet_name  = data[0][0]
        meet_date = data[1][0]
        meet_link = data[2][0]
        meet_summary = ""

        for i in range (0, len(data[3])):
            meet_summary = meet_summary + (data[3][i])

        #parse team results
        team_results = []
        for row in data[7]:
            if not row:
                break
            team_results.append(row)
            row += 1
        print(team_results)

        

        html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{meet_name}</title>
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h1>{meet_name}</h1>
        <h2>{meet_date}</h2>
        <a href="{meet_link}">Link</a>
        <p>Description: {meet_summary}</p>


        <nav>
            <ul>
                <li><a href="#team-results">Team Results</a></li>
                <li><a href="#athlete-results">Athlete Results</a></li>
                <li><a href="#gallery">Gallery</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="team-results">
            <h2>Team Results</h2>
            <p>TODO</p>
        </section>

        <section id="athlete-results">
            <h2>Athlete Results</h2>
            <p>TODO</p>
        </section>

        <section id="gallery">
            <h2>Photo Gallery</h2>
            <p>TODO</p>
        </section>
    </main>

    <footer>
    THIS IS FOOTER!
    </footer>
</body>
</html>
        '''

        with open(output_file, 'w') as ofile:
            ofile.write(html_content)

        

read_csv(path + meet_file)
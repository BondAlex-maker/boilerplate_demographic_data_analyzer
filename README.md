📊 Demographic Data Analyzer

A Python project that performs demographic analysis on the Adult Income dataset.
This project is part of the Data Analysis with Python
 certification on freeCodeCamp.

🧰 Features

The script analyzes the adult.data.csv dataset and calculates:

👥 Race count — number of each race represented in the dataset.

👨 Average age of men.

🎓 Percentage of people with a Bachelor's degree.

💼 Percentage of high earners (>50K) for:

People with higher education (Bachelors, Masters, Doctorate)

People without higher education

⏳ Minimum working hours per week and the percentage of rich people working that minimum.

🌍 Country with the highest percentage of people earning >50K and that percentage.

🇮🇳 Top occupation in India among people earning >50K.

🧠 Example Output
Number of each race:
 White                 27816
 Black                  3124
 Asian-Pac-Islander      1039
 Amer-Indian-Eskimo      311
 Other                   271
Name: race, dtype: int64
Average age of men: 39.4
Percentage with Bachelors degrees: 16.4%
Percentage with higher education that earn >50K: 46.5%
Percentage without higher education that earn >50K: 17.4%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 10.0%
Country with highest percentage of rich: Iran
Highest percentage of rich people in country: 41.9%
Top occupations in India: Prof-specialty

🧑‍💻 Project Structure
📁 demographic-data-analyzer
├── 📄 demographic_data_analyzer.py   # Main script
├── 📄 adult.data.csv                # Dataset
├── 📄 main.py                       # FCC test runner
├── 📄 test_module.py                # FCC test file
└── 📄 README.md

🚀 How to Run

Clone the repository:

git clone https://github.com/BondAlex-maker/demographic-data-analyzer.git
cd demographic-data-analyzer


Install dependencies:

pip install -r requirements.txt


(or make sure pandas is installed)

Run the script:

python demographic_data_analyzer.py

🧪 Testing

This project follows the official test suite provided by freeCodeCamp.

Run the tests:

python main.py


If all tests pass — ✅ you’ve successfully completed the task.

📝 Notes from the Author

The entire logic is implemented in demographic_data_analyzer.py.

All FCC test files remain unchanged for transparency.

The project focuses on data filtering, masking, grouping, and value counting using pandas.

📜 License

This project is open-source and available under the MIT License.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, jsonify

app = Flask(__name__)

def leetcode_scrape_data():
    driver_path = "D:/Chrome Driver/chromedriver.exe"
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    options.add_argument("--incognito")
    options.add_argument("--headless")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")

    try:
        browser = webdriver.Chrome(options=options)
        browser.get("https://leetcode.com/tanishq2505/")
        
        # Wait for the elements to be present
        wait = WebDriverWait(browser, 10)

        name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-label-1.dark\\:text-dark-label-1.break-all.text-base.font-semibold")))
        name = name_element.text

        usename_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-label-3.dark\\:text-dark-label-3.text-xs")))
        username = usename_element.text

        github_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[1]/a/div/span[2]/div/span')))
        github = github_element.text

        contest_rating_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]')))
        contest_rating = contest_rating_element.text

        problem_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div[1]')))
        problem_solved = problem_solved_element.text

        global_ranking_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]')))
        global_ranking = global_ranking_element.text

        top_percentage_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]')))
        top_percentage = top_percentage_element.text

        python_solutions_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[6]/div[1]/div[2]/span[1]')))
        python_solutions = python_solutions_element.text

        cpp_solution_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[6]/div[2]/div[2]/span[1]')))
        cpp_solution = cpp_solution_element.text

        return {
            "Name": name,
            "Username": username,
            "Github": github,
            "Contest_Rating": contest_rating,
            "Problem_Solved": problem_solved,
            "Global_Ranking": global_ranking,
            "Top_Percentage": top_percentage,
            "Python_Solutions": python_solutions,
            "C++_Solutions": cpp_solution
        }

    except Exception as e:
        print("An error occurred:", str(e))
        return {}

    finally:
        # Close the browser window regardless of any exceptions
        if 'browser' in locals():
            browser.quit()

def codeforces_scrape_data():
    driver_path = "D:/Chrome Driver/chromedriver.exe"
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    options.add_argument("--incognito")
    options.add_argument("--headless")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")

    try:
        browser = webdriver.Chrome(options=options)
        browser.get("https://codeforces.com/profile/tourist")
        
        # Wait for the elements to be present
        wait = WebDriverWait(browser, 10)

        username_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[2]/div/div[2]/div[2]/h1/a')))
        username = username_element.text

        contest_rating_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[2]/div/div[2]/ul/li[1]/span[1]')))
        contest_rating = contest_rating_element.text

        all_time_problem_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[4]/div/div[3]/div[1]/div[1]/div[1]')))
        all_time_problem_solved = all_time_problem_solved_element.text

        problems_solved_last_year_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[4]/div/div[3]/div[1]/div[2]/div[1]')))
        problems_solved_last_year = problems_solved_last_year_element.text

        problems_solved_last_month_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[4]/div/div[3]/div[1]/div[3]/div[1]')))
        problems_solved_last_month = problems_solved_last_month_element.text

        max_days_in_a_row_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div[4]/div/div[3]/div[2]/div[1]/div[1]')))
        max_days_in_a_row = max_days_in_a_row_element.text

        return {
            "Username": username,
            "Contest_Rating": contest_rating,
            "All_Time_Problem_Solved": all_time_problem_solved,
            "Problems_Solved_Last_Year": problems_solved_last_year,
            "Problems_Solved_Last_Month": problems_solved_last_month,
            "Max_Days_In_A_Row": max_days_in_a_row
        }

    except Exception as e:
        print("An error occurred:", str(e))
        return {}

    finally:
        # Close the browser window regardless of any exceptions
        if 'browser' in locals():
            browser.quit()
    
def codingninjas_scrape_data():
    driver_path = "D:/Chrome Driver/chromedriver.exe"
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    options.add_argument("--incognito")
    options.add_argument("--headless")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")

    try:
        browser = webdriver.Chrome(options=options)
        browser.get("https://www.codingninjas.com/studio/profile/Anish5665")
        
        # Wait for the elements to be present
        wait = WebDriverWait(browser, 10)

        username_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div/div[1]/codingninjas-profile-user-basic-info/div/div[1]/div[1]/div[1]/div[2]')))
        username = username_element.text

        total_problems_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div/div[2]/div[1]/codingninjas-profile-contribution-heatmap/div[1]/div[1]/div[1]')))
        total_problems_solved = total_problems_solved_element.text

        easy_problems_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div/div[2]/div[1]/codingninjas-profile-contribution-heatmap/div[1]/div[2]/div[1]/div[1]')))
        easy_problems_solved = easy_problems_solved_element.text

        moderate_problems_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div/div[2]/div[1]/codingninjas-profile-contribution-heatmap/div[1]/div[2]/div[2]/div[1]')))
        moderate_problems_solved = moderate_problems_solved_element.text

        hard_problems_solved_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div/div[2]/div[1]/codingninjas-profile-contribution-heatmap/div[1]/div[2]/div[3]/div[1]')))
        hard_problems_solved = hard_problems_solved_element.text

        current_streak_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div[1]/div[2]/div[1]/codingninjas-profile-contribution-heatmap/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/p')))
        current_streak = current_streak_element.text

        longest_streak_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/codingninjas-user-dashboard/codingninjas-profile/div[1]/div[2]/div[1]/codingninjas-profile-contribution-heatmap/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/p')))
        longest_streak = longest_streak_element.text

        return {
            "Username": username,
            "Total_Problems_Solved": total_problems_solved,
            "Easy_Problems_Solved": easy_problems_solved,
            "Moderate_Problems_Solved": moderate_problems_solved,
            "Hard_Problems_Solved": hard_problems_solved,
            "Current_Streak": current_streak,
            "Longest_Streak": longest_streak
        }

    except Exception as e:
        print("An error occurred:", str(e))
        return {}

    finally:
        # Close the browser window regardless of any exceptions
        if 'browser' in locals():
            browser.quit()


@app.route('/leetcode_data', methods=['GET'])
def get_leetcode_data():
    data = leetcode_scrape_data()
    return jsonify(data)

@app.route('/codeforces_data', methods=['GET'])
def get_codeforces_data():
    data = codeforces_scrape_data()
    return jsonify(data)

@app.route('/codingninjas_data', methods=['GET'])
def get_codingninjas_data():
    data = codingninjas_scrape_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

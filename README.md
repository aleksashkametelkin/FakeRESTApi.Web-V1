# imgur
Python + Pytest + TelegramBot report

For example, use ```$ pytest ./tests --telegram_id=CHANNEL_ID --telegram_token=TELEGRAM:TOKEN --telegram_custom_text="Test text"```

# Allure reports

pytest -s -v --alluredir=NAME_OF_CREATED_DIRECTORY
allure serve NAME_OF_CREATED_DIRECTORY
(If you will have an error on MAC: "allure command not found" you will need to install latest version of JDK)
+
Add this to .bash_profile 
````
# Setting PATH for Allure 2.10
PATH="path_to_your_allure_directory"/allure-2.10.0/bin:${PATH}"
export PATH
````
+
run command "allure serve NAME_OF_CREATED_DIRECTORY" to see beauty HTML report
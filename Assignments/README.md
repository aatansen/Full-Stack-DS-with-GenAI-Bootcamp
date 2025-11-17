<div align="center">
<h1>Full Stack DS with GenAI Bootcamp</h1>

> *Assignments of Full Stack DS with GenAI Bootcamp*
</div>

# **Context**
- [**Context**](#context)
- [**Assignments**](#assignments)
  - [**Assignment 01**](#assignment-01)
    - [Task 01 - Temperature Check](#task-01---temperature-check)
    - [Task 02 - ATM Withdrawal System](#task-02---atm-withdrawal-system)
    - [Task 03 - Student Grade Calculator](#task-03---student-grade-calculator)
    - [Task 04 - Bus Ticket Discount](#task-04---bus-ticket-discount)
    - [Task 05 - Restaurant Bill with Discount](#task-05---restaurant-bill-with-discount)
    - [Task 06 - Login Authentication](#task-06---login-authentication)
    - [Task 07 - Traffic Light System](#task-07---traffic-light-system)
    - [Task 08 - Leap Year Checker](#task-08---leap-year-checker)
    - [Task 09 - Job Eligibility Checker](#task-09---job-eligibility-checker)
    - [Task 10 - Electricity Bill Calculator](#task-10---electricity-bill-calculator)
    - [**Assignment 01 Result \& Correction**](#assignment-01-result--correction)
  - [**Assignment 02**](#assignment-02)
    - [Task 01 - Email Validator (String Filtering + Loops)](#task-01---email-validator-string-filtering--loops)
    - [Task 02 - Count Word Frequency in Customer Reviews](#task-02---count-word-frequency-in-customer-reviews)
    - [Task 03 - Password Strength Checker](#task-03---password-strength-checker)
    - [Task 04 - Username Generator](#task-04---username-generator)
    - [Task 05 - SMS Word Counter](#task-05---sms-word-counter)
    - [Task 06 - Remove Duplicates from Contact List](#task-06---remove-duplicates-from-contact-list)
    - [Task 07 - Detect Suspicious Words in Text (Moderation)](#task-07---detect-suspicious-words-in-text-moderation)
    - [Task 08 - Invoice Code Formatter](#task-08---invoice-code-formatter)
    - [Task 09 - Count Hashtags and Mentions (Social Media Analytics)](#task-09---count-hashtags-and-mentions-social-media-analytics)
    - [Task 10 - Word Reversal for Data Encryption](#task-10---word-reversal-for-data-encryption)

# **Assignments**

## [**Assignment 01**](./Assignment%2001/)

### Task 01 - Temperature Check

- Write a program that takes the current temperature as input and prints:
  - "`It's too cold!`" if below 10°C
  - "`It's cool outside`" if between 10°C and 25°C
  - "`It's hot outside!`" if above 25°C

> [Task 01 Solution](./Assignment%2001/Task%2001%20-%20Temperature%20Check.py)

[⬆️ Go to Context](#context)

### Task 02 - ATM Withdrawal System

- Ask the user for their account balance and the amount they want to withdraw.
  - If the withdrawal amount is greater than the balance → print "`Insufficient Balance`"
  - If the withdrawal amount is less than or equal to balance → print "`Transaction Successful`" and show the remaining balance.

> [Task 02 Solution](./Assignment%2001/Task%2002%20-%20ATM%20Withdrawal%20System.py)

[⬆️ Go to Context](#context)

### Task 03 - Student Grade Calculator

- Input marks (0-100) and print grade based on:
  - 90-100 → `A+`
  - 80-89 → `A`
  - 70-79 → `B`
  - 60-69 → `C`
  - Below 60 → `Fail`

> [Task 03 Solution](./Assignment%2001/Task%2003%20-%20Student%20Grade%20Calculator.py)

[⬆️ Go to Context](#context)

### Task 04 - Bus Ticket Discount

- Ask the user for `age` and print `ticket price`:
  - Below 5 → `Free`
  - 5-18 → `50% Discount`
  - 60 or above → `30% Discount`
  - Others → `Full Price`

> [Task 04 Solution](./Assignment%2001/Task%2004%20-%20Bus%20Ticket%20Discount.py)

[⬆️ Go to Context](#context)

### Task 05 - Restaurant Bill with Discount

- Take total bill amount from the user:
  - If the bill is above 1000 → apply `10% discount`
  - Otherwise → `no discount`
- Then print the `final bill amount`.

> [Task 05 Solution](./Assignment%2001/Task%2005%20-%20Restaurant%20Bill%20with%20Discount.py)

[⬆️ Go to Context](#context)

### Task 06 - Login Authentication

- Take a `username` and `password` input.
  - If `username == "admin"` and `password == "12345"` → print "`Login Successful`"
  - Else → print "`Invalid Credentials`"

> [Task 06 Solution](./Assignment%2001/Task%2006%20-%20Login%20Authentication.py)

[⬆️ Go to Context](#context)

### Task 07 - Traffic Light System

- Ask the user to input a color (`red`, `yellow`, or `green`).
Print:
  - "`Stop`" for `red`
  - "`Ready to go`" for `yellow`
  - "`Go`" for `green`
  - "`Invalid color`" otherwise

> [Task 07 Solution](./Assignment%2001/Task%2007%20-%20Traffic%20Light%20System.py)

[⬆️ Go to Context](#context)

### Task 08 - Leap Year Checker

- Take a year as input and check:
  - If it is divisible by `400` → `Leap Year`
  - Else if divisible by `4` but not by `100` → `Leap Year`
  - Otherwise → `Not a Leap Year`

> [Task 08 Solution](./Assignment%2001/Task%2008%20-%20Leap%20Year%20Checker.py)

[⬆️ Go to Context](#context)

### Task 09 - Job Eligibility Checker

- Input age and qualification.
- If `age ≥ 18` and qualification is "`graduate`" → print "`Eligible for Job`"
- Else → "`Not Eligible`"

> [Task 09 Solution](./Assignment%2001/Task%2009%20-%20Job%20Eligibility%20Checker.py)

[⬆️ Go to Context](#context)

### Task 10 - Electricity Bill Calculator

- Input number of units consumed and calculate bill:
  - Up to `100` units → `5` BDT per unit
  - `101-200` units → `7` BDT per unit
  - Above `200` units → `10` BDT per unit
- Print `total payable amount`.

> [Task 10 Solution](./Assignment%2001/Task%2010%20-%20Electricity%20Bill%20Calculator.py)

[⬆️ Go to Context](#context)

### **Assignment 01 Result & Correction**

- Task 01 - Temperature Check
  - Correction: Type conversion float
- Task 02 - ATM Withdrawal System
  - Correction: Type conversion float, need to handle negative withdraw
- Task 03 - Student Grade Calculator
  - Correction: Type conversion float
- Task 04 - Bus Ticket Discount
  - Correction: Negative check required
- Task 05 - Restaurant Bill with Discount
  - Correction: Type conversion float and Limiting floats to two decimal points
- Task 06 - Login Authentication
  - Correction: username lowercase convert
- Task 07 - Traffic Light System
  - Correction: color lowercase convert
- Task 08 - Leap Year Checker
  - Correct
- Task 09 - Job Eligibility Checker
  - Correction: qualification lowercase convert
- Task 10 - Electricity Bill Calculator
  - Correction: Type conversion float and negative unit check
- **Final result : `5.5`**

> [!NOTE]
>
> - Convert user inputs to **float** only when decimal values are needed (like temperature, money, bills)
> - Always check for **negative values** (withdraw amount, units, ticket price, etc.).
> - **Convert user input to lowercase** before comparing strings (e.g., username, color, qualification).
> - **Limit float outputs** to two decimal points when printing money or bill values.
> - Be consistent with **data validation** before performing calculations.
> - Review each task for **type conversion**, **case handling**, and **value checking**.

[⬆️ Go to Context](#context)

## [**Assignment 02**](./Assignment%2002/)

### Task 01 - Email Validator (String Filtering + Loops)

> 💼 **Real-world use:** Used in signup forms or data cleaning tasks.

- Check if a given email is valid — must contain “`@`” and end with “`.com`” or “`.org`”.
  - **Input**: `hello@inceptionbd.com`
  - **Output**: `Valid Email`

> [Task 01 Solution](./Assignment%2002/Task%2001%20-%20Email%20Validator.py)

[⬆️ Go to Context](#context)

### Task 02 - Count Word Frequency in Customer Reviews

> 💼 **Real-world use:** Analyzing reviews or comments in text analytics.

- Given a review text, count how many times each word appears (ignore case).
  - Input: "`This product is good and this service is excellent`"
  - Output: `{'this': 2, 'product': 1, 'is': 2, 'good': 1, 'and': 1, 'service': 1, 'excellent': 1}`

> [Task 02 Solution](./Assignment%2002/Task%2002%20-%20Count%20Word%20Frequency%20in%20Customer%20Reviews.py)

[⬆️ Go to Context](#context)

### Task 03 - Password Strength Checker

> 💼 **Real-world use:** Used in user authentication systems.

- Check if a password is strong — must have at least one uppercase, one lowercase, one digit, and one special character.
  - Input: "`Hello@123`"
  - Output: `Strong Password`

> [Task 03 Solution](./Assignment%2002/Task%2003%20-%20Password%20Strength%20Checker.py)

[⬆️ Go to Context](#context)

### Task 04 - Username Generator

> 💼 **Real-world use:** Automatically create usernames for users.

- Take user's full name and generate a short username.
- Rules: first 3 letters of first name + last 3 letters of last name + random number (use loops only).
  - Input: "`Mamun Malitha`"
  - Output: `mamitha57`

> [Task 04 Solution](./Assignment%2002/Task%2004%20-%20Username%20Generator.py)

[⬆️ Go to Context](#context)

### Task 05 - SMS Word Counter

> 💼 **Real-world use:** Used in messaging apps or social media post limit check.

- Count how many characters and words are in a message, and tell if it exceeds 160 characters (SMS limit).
  - Input: "`This is a demo message.`"
  - Output: `Words = 5, Characters = 23, Status = Within Limit`

> [Task 05 Solution](./Assignment%2002/Task%2005%20-%20SMS%20Word%20Counter.py)

[⬆️ Go to Context](#context)

### Task 06 - Remove Duplicates from Contact List

> 💼 **Real-world use:** Data cleaning in CRM or user databases.

- Given a list of names (comma separated), remove duplicates.
  - Input: "`Rahim, Karim, Rahim, Sultana`"
  - Output: `Rahim, Karim, Sultana`

> [Task 06 Solution](./Assignment%2002/Task%2006%20-%20Remove%20Duplicates%20from%20Contact%20List.py)

[⬆️ Go to Context](#context)

### Task 07 - Detect Suspicious Words in Text (Moderation)

> 💼 **Real-world use:** Used in chat moderation or email filtering.

- If any “banned” words like ['spam', 'scam', 'fake'] are found in a text, print “Warning”.
  - Input: "`This is a scam offer`"
  - Output: `Warning: Suspicious content detected`

> [Task 07 Solution](./Assignment%2002/Task%2007%20-%20Detect%20Suspicious%20Words%20in%20Text.py)

[⬆️ Go to Context](#context)

### Task 08 - Invoice Code Formatter

> 💼 **Real-world use:** Formatting IDs or codes in finance or ERP systems.

- Given an invoice number like 23, generate code in the format `INV00023`.
  - Input: "`23`"
  - Output: `Output: INV00023`

> [Task 08 Solution](./Assignment%2002/Task%2008%20-%20Invoice%20Code%20Formatter.py)

[⬆️ Go to Context](#context)

### Task 09 - Count Hashtags and Mentions (Social Media Analytics)

> 💼 **Real-world use:** Used in analyzing social media posts.

- Count how many hashtags (#) and mentions (@) appear in a post.
  - Input: "`Check out #AIWorkshop and follow @inceptionbd`"
  - Output: `Hashtags = 1, Mentions = 1`

> [Task 09 Solution](./Assignment%2002/Task%2009%20-%20Count%20Hashtags%20and%20Mentions.py)

[⬆️ Go to Context](#context)

### Task 10 - Word Reversal for Data Encryption

> 💼 **Real-world use:** Simple text obfuscation or playful encoding.

- Reverse each word in a sentence while keeping word order the same.
  - Input: "`AI is fun`"
  - Output: `IA si nuf`

> [Task 10 Solution](./Assignment%2002/Task%2010%20-%20Word%20Reversal%20for%20Data%20Encryption.py)

[⬆️ Go to Context](#context)

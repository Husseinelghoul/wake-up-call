# Wake up call :alarm_clock:
The algorithm works by calling a given number until the receiving end interacts with the call *(meaning that he/she woke up)* by either **answering** or **declining** the call, if the latter doesn't respond, the software will call them again until they get a **response**.

## How does it work ?
The software utilizes [Twillio voice API](https://www.twilio.com/docs/voice/make-calls) to initiate the calls and recursively checks for response and calls in case of no response.
## Requiremtns
If you want to use the software, you will require a computer with:
- [python3](https://www.python.org/downloads/)
- Twillio account **[SID]("https://www.twilio.com/docs/glossary/what-is-a-sid")** and **[AUTH token]("https://www.twilio.com/docs/iam/access-tokens")**

## Project Setup
After cloning the project, navigate to the project's directory and complete the following steps:
- run the following command `pip3 install -r requirements.txt`.
- create a `.env` file using the provided `.env.example` that includes your `AUTH token` , `account SID`, the `FROM` and `TO` fields that represent the calling and receiving end.
- finally, run the project using the following command `python3 wake_up.py`.
___
*Made with ♥️ for someone special*

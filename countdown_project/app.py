"""
When this app runs it prints in stout the length of time i have left at Siemens.
"""
import datetime

class Date:

    current_date = datetime.datetime.now()

    months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
    }

    ordinal_numbers = {
    1: "1st",
    2: "2nd",
    3: "3rd",
    }

    # Get day of the week, day, and month name
    day_of_week = current_date.strftime('%A')
    day = current_date.day
    month = months[current_date.month]

    # Check if the day should have an ordinal suffix
    if day in ordinal_numbers:
        day = ordinal_numbers[day]
    else:
        day = f"{day}th"

    # Format and display the date
    def print_date(self):
        formatted_date = f"Today is {self.day_of_week} the {self.day} of {self.month}"
        print(formatted_date)

    def count_weekdays_only(self, target_date):
        current_date = self.current_date
        count = 0

        while current_date < target_date:
            if current_date.weekday() < 5:
                count += 1
            current_date += datetime.timedelta(days=1)

        return count

    def print_all_info(self, target_date, days_of_holidays):

        time_remaining = target_date - self.current_date
        weeks_remaining = time_remaining.days // 7

        week_days_left = self.count_weekdays_only(target_date)

        print(f"We have {time_remaining.days} days left")
        print(f"Thats {weeks_remaining} weeks left")
        print(f"That includes {week_days_left} weekdays")
        print(f"Minus {days_of_holidays} days holidays leaves us with {week_days_left - days_of_holidays} days left ")


def main():
    """
    Display current date and time and then how long until
    the time I finish at Siemens.
    """

    today = Date()

    today.print_date()

    print("Our last day at Siemens is Thursday the 18th of January 2024")
    target_date = datetime.datetime(2024, 1, 18)

    today.print_all_info(target_date, 7) # 7 represents 7 days holiday removed from the count


if __name__ == "__main__":
    main()
